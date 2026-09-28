#!/usr/bin/env python3
"""
Postdoc Research Update Freshness Report
-----------------------------------------
Analyzes GitHub commit history for the postdocs directory and reports
which markdown files were updated during the previous quarter.
The quarter window is calculated dynamically from today's date.

Usage:
    python postdoc_report.py
    python postdoc_report.py --token YOUR_GITHUB_TOKEN   # for higher rate limits
    python postdoc_report.py --output report.html        # save HTML report
    python postdoc_report.py --quarter 2025Q4            # override quarter manually
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from collections import defaultdict

# ── Config ──────────────────────────────────────────────────────────────────
REPO_OWNER  = "uscms-software-and-computing"
REPO_NAME   = "uscms-software-and-computing.github.io"
BASE_PATH   = "pages/postdocs"
BRANCH      = "master"
API_BASE    = "https://api.github.com"
# ─────────────────────────────────────────────────────────────────────────────


def previous_quarter(today=None):
    """Return (label, start, end) for the previous calendar quarter."""
    if today is None:
        today = datetime.now(tz=timezone.utc)
    q = (today.month - 1) // 3 + 1          # current quarter (1-4)
    if q == 1:
        pq, year = 4, today.year - 1
    else:
        pq, year = q - 1, today.year
    quarter_starts = {1: (1,1), 2: (4,1), 3: (7,1), 4: (10,1)}
    quarter_ends   = {1: (3,31), 2: (6,30), 3: (9,30), 4: (12,31)}
    sm, sd = quarter_starts[pq]
    em, ed = quarter_ends[pq]
    start = datetime(year, sm, sd, tzinfo=timezone.utc)
    end   = datetime(year, em, ed, 23, 59, 59, tzinfo=timezone.utc)
    label = f"Q{pq} {year}"
    return label, start, end


def parse_quarter_override(s):
    """Parse a manual override like '2025Q4' into (label, start, end)."""
    m = re.fullmatch(r"(\d{4})Q([1-4])", s.strip(), re.IGNORECASE)
    if not m:
        raise argparse.ArgumentTypeError(
            f"Invalid quarter format '{s}'. Use e.g. 2025Q4")
    year, pq = int(m.group(1)), int(m.group(2))
    quarter_starts = {1: (1,1), 2: (4,1), 3: (7,1), 4: (10,1)}
    quarter_ends   = {1: (3,31), 2: (6,30), 3: (9,30), 4: (12,31)}
    sm, sd = quarter_starts[pq]
    em, ed = quarter_ends[pq]
    start = datetime(year, sm, sd, tzinfo=timezone.utc)
    end   = datetime(year, em, ed, 23, 59, 59, tzinfo=timezone.utc)
    return f"Q{pq} {year}", start, end


def gh_get(url, token=None):
    """Make a GitHub API GET request, returning parsed JSON."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "postdoc-freshness-report/1.0")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode()), dict(resp.headers)


def paginate(url, token=None):
    """Yield items from all pages of a GitHub list endpoint."""
    while url:
        data, headers = gh_get(url, token)
        if isinstance(data, list):
            yield from data
        else:
            yield data
            break
        link = headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            part = part.strip()
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().strip("<>")
        url = next_url


def list_md_files(token=None):
    """Return all .md files recursively under BASE_PATH."""
    url = (f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}"
           f"?recursive=1")
    data, _ = gh_get(url, token)
    files = []
    for item in data.get("tree", []):
        path = item["path"]
        if path.startswith(BASE_PATH + "/") and path.endswith(".md"):
            files.append(path)
    return sorted(files)


def get_permalink(filepath, token=None):
    """Fetch file content and extract permalink from YAML front matter."""
    import base64, re
    url = (f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filepath}"
           f"?ref={BRANCH}")
    try:
        data, _ = gh_get(url, token)
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            pl_match = re.search(r"^permalink\s*:\s*(.+)$", fm, re.MULTILINE)
            if pl_match:
                permalink = pl_match.group(1).strip().strip('"\'')
                if not permalink.startswith("/"):
                    permalink = "/" + permalink
                return f"https://uscms-software-and-computing.github.io{permalink}"
    except Exception:
        pass
    return ("https://uscms-software-and-computing.github.io/"
            + filepath.replace("pages/", "").replace(".md", ".html"))


def get_file_commits(filepath, token=None):
    """Return all commits that touched a specific file (newest first)."""
    url = (f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/commits"
           f"?path={filepath}&sha={BRANCH}&per_page=100")
    return list(paginate(url, token))


def parse_date(date_str):
    return datetime.fromisoformat(date_str.replace("Z", "+00:00"))


def classify(commits, q_start, q_end):
    """
    Return (last_commit_date, in_quarter, quarter_commit_count, all_time_commits).
    """
    if not commits:
        return None, False, 0, 0

    dates = []
    for c in commits:
        raw = (c.get("commit", {}).get("committer", {}).get("date") or
               c.get("commit", {}).get("author", {}).get("date"))
        if raw:
            dates.append(parse_date(raw))

    if not dates:
        return None, False, 0, len(commits)

    dates.sort(reverse=True)
    last = dates[0]
    q_dates = [d for d in dates if q_start <= d <= q_end]
    return last, bool(q_dates), len(q_dates), len(dates)


# ── HTML report ───────────────────────────────────────────────────────────────
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Postdoc Update Freshness Report – {quarter}</title>
<style>
  :root {{ --green:#22c55e; --red:#ef4444; --yellow:#f59e0b; --bg:#f8fafc; --card:#fff; --border:#e2e8f0; }}
  body {{ font-family: system-ui, sans-serif; background:var(--bg); color:#1e293b; margin:0; padding:24px; }}
  h1 {{ font-size:1.6rem; margin-bottom:4px; }}
  .subtitle {{ color:#64748b; margin-bottom:24px; font-size:.95rem; }}
  .summary {{ display:flex; gap:16px; flex-wrap:wrap; margin-bottom:28px; }}
  .stat {{ background:var(--card); border:1px solid var(--border); border-radius:10px; padding:16px 24px; min-width:140px; }}
  .stat .num {{ font-size:2rem; font-weight:700; }}
  .stat .label {{ font-size:.8rem; color:#64748b; margin-top:2px; }}
  .green {{ color:var(--green); }} .red {{ color:var(--red); }} .yellow {{ color:var(--yellow); }}
  table {{ width:100%; border-collapse:collapse; background:var(--card); border-radius:10px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,.07); }}
  th {{ background:#f1f5f9; text-align:left; padding:10px 14px; font-size:.8rem; text-transform:uppercase; letter-spacing:.05em; color:#475569; }}
  td {{ padding:9px 14px; border-top:1px solid var(--border); font-size:.88rem; vertical-align:middle; }}
  tr:hover td {{ background:#f8fafc; }}
  .badge {{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:.78rem; font-weight:600; }}
  .badge-up-to-date {{ background:#dcfce7; color:#166534; }}
  .badge-outdated   {{ background:#fee2e2; color:#991b1b; }}
  .badge-no-commits {{ background:#fef9c3; color:#854d0e; }}
  .filename {{ font-family:monospace; font-size:.82rem; }}
  .gh-link {{ color:#3b82f6; text-decoration:none; font-size:.8rem; }}
  .gh-link:hover {{ text-decoration:underline; }}
  footer {{ margin-top:24px; font-size:.78rem; color:#94a3b8; }}
</style>
</head>
<body>
<h1>📋 Postdoc Research Update – Freshness Report</h1>
<p class="subtitle">Repository: <strong>{repo}</strong> &nbsp;|&nbsp; Path: <code>{path}</code> &nbsp;|&nbsp;
  Reporting quarter: <strong>{quarter}</strong> ({q_start} – {q_end}) &nbsp;|&nbsp; Generated: <strong>{generated}</strong></p>

<div class="summary">
  <div class="stat"><div class="num">{total}</div><div class="label">Total files</div></div>
  <div class="stat"><div class="num green">{up_to_date}</div><div class="label">Updated in {quarter}</div></div>
  <div class="stat"><div class="num red">{outdated}</div><div class="label">Not updated in {quarter}</div></div>
  <div class="stat"><div class="num yellow">{no_commits}</div><div class="label">No commits found</div></div>
</div>

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>File</th>
      <th>Status</th>
      <th>Last Commit</th>
      <th>{quarter} Commits</th>
      <th>Total Commits</th>
      <th>Page</th>
      <th>Commits</th>
    </tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>

<footer>Report generated by postdoc_report.py &nbsp;•&nbsp; Data source: GitHub Commits API</footer>
</body>
</html>
"""

ROW_TEMPLATE = """    <tr>
      <td>{i}</td>
      <td class="filename">{filename}</td>
      <td><span class="badge {badge_class}">{status}</span></td>
      <td>{last_commit}</td>
      <td>{q_count}</td>
      <td>{total_count}</td>
      <td><a class="gh-link" href="{web_url}" target="_blank" rel="noopener noreferrer">page ↗</a></td>
      <td><a class="gh-link" href="{gh_url}" target="_blank" rel="noopener noreferrer">commits ↗</a></td>
    </tr>"""


def build_html(results, repo_slug, base_path, quarter, q_start, q_end):
    total      = len(results)
    up_to_date = sum(1 for r in results if r["in_quarter"])
    outdated   = sum(1 for r in results if not r["in_quarter"] and r["total_commits"] > 0)
    no_commits = sum(1 for r in results if r["total_commits"] == 0)

    rows = []
    for i, r in enumerate(results, 1):
        if r["in_quarter"]:
            badge_class, status = "badge-up-to-date", "✅ Updated"
        elif r["total_commits"] == 0:
            badge_class, status = "badge-no-commits", "⚠️ No commits"
        else:
            badge_class, status = "badge-outdated", "❌ Not updated"

        last    = r["last_commit_date"].strftime("%Y-%m-%d") if r["last_commit_date"] else "—"
        fname   = r["path"].replace(base_path + "/", "")
        gh_url  = f"https://github.com/{repo_slug}/commits/{BRANCH}/{r['path']}"
        web_url = r["permalink"]
        rows.append(ROW_TEMPLATE.format(
            i=i, filename=fname, badge_class=badge_class, status=status,
            last_commit=last, q_count=r["quarter_commits"] or "—",
            total_count=r["total_commits"] or "—", gh_url=gh_url, web_url=web_url
        ))

    return HTML_TEMPLATE.format(
        repo=repo_slug, path=base_path, quarter=quarter,
        q_start=q_start.strftime("%b %d, %Y"), q_end=q_end.strftime("%b %d, %Y"),
        generated=datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        total=total, up_to_date=up_to_date, outdated=outdated, no_commits=no_commits,
        rows="\n".join(rows)
    )


def build_pdf(results, repo_slug, base_path, quarter, q_start, q_end, output_path):
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

    doc = SimpleDocTemplate(
        output_path, pagesize=landscape(letter),
        leftMargin=0.5*inch, rightMargin=0.5*inch,
        topMargin=0.5*inch, bottomMargin=0.5*inch
    )
    styles = getSampleStyleSheet()
    story  = []

    title_style = ParagraphStyle("title", parent=styles["Title"], fontSize=16, spaceAfter=4)
    sub_style   = ParagraphStyle("sub", parent=styles["Normal"], fontSize=8,
                                 textColor=colors.grey, spaceAfter=12)
    story.append(Paragraph("Postdoc Research Update – Freshness Report", title_style))
    story.append(Paragraph(
        f"Repo: {repo_slug} &nbsp;|&nbsp; Path: {base_path} &nbsp;|&nbsp; "
        f"Quarter: {quarter} ({q_start.strftime('%b %d, %Y')} – {q_end.strftime('%b %d, %Y')}) "
        f"&nbsp;|&nbsp; Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}",
        sub_style
    ))

    total      = len(results)
    up_to_date = sum(1 for r in results if r["in_quarter"])
    outdated   = sum(1 for r in results if not r["in_quarter"] and r["total_commits"] > 0)
    no_commits = sum(1 for r in results if r["total_commits"] == 0)

    summary_data = [
        ["Total Files", f"Updated ({quarter})", "Not Updated", "No Commits"],
        [str(total), str(up_to_date), str(outdated), str(no_commits)]
    ]
    summary_table = Table(summary_data, colWidths=[2*inch]*4)
    summary_table.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 9),
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("FONTNAME",     (0,1), (-1,1), "Helvetica-Bold"),
        ("FONTSIZE",     (0,1), (-1,1), 16),
        ("TEXTCOLOR",    (1,1), (1,1), colors.HexColor("#16a34a")),
        ("TEXTCOLOR",    (2,1), (2,1), colors.HexColor("#dc2626")),
        ("TEXTCOLOR",    (3,1), (3,1), colors.HexColor("#d97706")),
        ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("INNERGRID",    (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("TOPPADDING",   (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0), (-1,-1), 8),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 16))

    url_style  = ParagraphStyle("url",  parent=styles["Normal"], fontSize=7,
                                textColor=colors.HexColor("#3b82f6"))
    file_style = ParagraphStyle("file", parent=styles["Normal"], fontSize=7,
                                fontName="Courier")

    header     = ["#", "File", "Status", "Last Commit", f"{quarter} Commits", "Total", "Page URL", "Commits URL"]
    col_widths = [0.3*inch, 2.2*inch, 0.9*inch, 0.85*inch, 0.8*inch, 0.5*inch, 2.0*inch, 2.0*inch]

    table_data = [header]
    row_colors = []
    for i, r in enumerate(results, 1):
        if r["in_quarter"]:
            status, bg = "Updated",    colors.HexColor("#dcfce7")
        elif r["total_commits"] == 0:
            status, bg = "No commits", colors.HexColor("#fef9c3")
        else:
            status, bg = "Not updated", colors.HexColor("#fee2e2")
        row_colors.append(bg)

        fname   = r["path"].replace(base_path + "/", "")
        last    = r["last_commit_date"].strftime("%Y-%m-%d") if r["last_commit_date"] else "—"
        gh_url  = f"https://github.com/{repo_slug}/commits/{BRANCH}/{r['path']}"
        web_url = r["permalink"]
        table_data.append([
            str(i),
            Paragraph(fname, file_style),
            status, last,
            str(r["quarter_commits"]) if r["quarter_commits"] else "—",
            str(r["total_commits"])   if r["total_commits"]   else "—",
            Paragraph(f'<link href="{web_url}">{web_url}</link>', url_style),
            Paragraph(f'<link href="{gh_url}">commits ↗</link>', url_style),
        ])

    bg_cmds = [("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f1f5f9"))]
    for idx, bg in enumerate(row_colors, 1):
        bg_cmds.append(("BACKGROUND", (0, idx), (-1, idx), bg))

    main_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    main_table.setStyle(TableStyle([
        *bg_cmds,
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 7),
        ("ALIGN",        (0,0), (0,-1), "CENTER"),
        ("ALIGN",        (3,0), (5,-1), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("INNERGRID",    (0,0), (-1,-1), 0.25, colors.HexColor("#e2e8f0")),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
    ]))
    story.append(main_table)
    doc.build(story)
    print(f"📄 PDF report written to: {output_path}")


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Postdoc freshness report")
    parser.add_argument("--token",   help="GitHub personal access token")
    parser.add_argument("--output",  default="postdoc_freshness_report.html",
                        help="Output HTML file")
    parser.add_argument("--quarter", help="Override quarter, e.g. 2025Q4 (default: previous quarter)")
    parser.add_argument("--json",    action="store_true", help="Also write JSON results")
    parser.add_argument("--pdf",     action="store_true", help="Also write a PDF report")
    args = parser.parse_args()

    # Resolve quarter window
    if args.quarter:
        quarter, q_start, q_end = parse_quarter_override(args.quarter)
    else:
        quarter, q_start, q_end = previous_quarter()

    token     = args.token
    repo_slug = f"{REPO_OWNER}/{REPO_NAME}"

    print(f"📅 Reporting quarter: {quarter}  ({q_start.date()} – {q_end.date()})")
    print(f"🔍 Listing markdown files in {BASE_PATH} ...")
    md_files = list_md_files(token)
    print(f"   Found {len(md_files)} markdown files.\n")

    results = []
    for idx, filepath in enumerate(md_files, 1):
        short = filepath.replace(BASE_PATH + "/", "")
        print(f"  [{idx:>3}/{len(md_files)}] {short}", end="", flush=True)
        commits   = get_file_commits(filepath, token)
        permalink = get_permalink(filepath, token)
        last_date, in_quarter, q_count, total = classify(commits, q_start, q_end)
        marker = "✅" if in_quarter else ("⚠️ " if total == 0 else "❌")
        print(f"  {marker}  last: {last_date.strftime('%Y-%m-%d') if last_date else 'n/a'}"
              f"  quarter_commits: {q_count}  total: {total}")
        results.append({
            "path":             filepath,
            "permalink":        permalink,
            "last_commit_date": last_date,
            "in_quarter":       in_quarter,
            "quarter_commits":  q_count,
            "total_commits":    total,
        })

    results.sort(key=lambda r: (not r["in_quarter"],
                                -(r["last_commit_date"].timestamp() if r["last_commit_date"] else 0)))

    up_to_date = sum(1 for r in results if r["in_quarter"])
    print(f"\n{'='*55}")
    print(f"  Quarter     : {quarter}")
    print(f"  Total files : {len(results)}")
    print(f"  ✅ Updated in quarter  : {up_to_date}")
    print(f"  ❌ Not updated         : {sum(1 for r in results if not r['in_quarter'] and r['total_commits']>0)}")
    print(f"  ⚠️  No commits found   : {sum(1 for r in results if r['total_commits']==0)}")
    print(f"{'='*55}\n")

    html = build_html(results, repo_slug, BASE_PATH, quarter, q_start, q_end)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"📄 HTML report written to: {args.output}")

    if args.pdf:
        pdf_path = args.output.replace(".html", ".pdf")
        build_pdf(results, repo_slug, BASE_PATH, quarter, q_start, q_end, pdf_path)

    if args.json:
        json_path = args.output.replace(".html", ".json")
        serial = [{**r, "last_commit_date": r["last_commit_date"].isoformat() if r["last_commit_date"] else None}
                  for r in results]
        with open(json_path, "w") as f:
            json.dump(serial, f, indent=2)
        print(f"📄 JSON results written to: {json_path}")


if __name__ == "__main__":
    main()
