---
layout: main-page
title: Home
bgimage: assets/images/USCMS_banner.png
---

# Mission
The mission of U.S. CMS Software and Computing is to develop and operate the software and computing resources necessary to process CMS data expeditiously and to enable U.S. physicists to fully participate in the physics of CMS.

# Areas
U.S. CMS Software and Computing is broken down into 5 areas:


{% assign areas = site.pages | where: "layout", "wbs-area" | sort_natural: 'wbs_no' %}
{% for mypage in areas %}
- [{{mypage.title}} (WBS {{mypage.wbs_no}})]({{mypage.permalink}})
{% endfor %}
