---
permalink: /docs/org_chart.html
layout: default
title: Generate an Org Chart image
---

{% include new_org_chart.html %}

<!-- 2) Add a button near the chart -->
<button id="savePng">
  Download PNG
</button>

<!-- 3) Add this script block (after your existing <script> that renders the chart) -->
<script>
  // If your photos might be cross-origin, ensure images don't taint the capture:
  // (You already create <img> elements in addPhotos—this sets crossOrigin there.)
  const originalAddPhotos = addPhotos;
  addPhotos = function(key, div, names){
    names.forEach(p => { if (p && p.photo) { /* hint for CORS */ } });
    originalAddPhotos(key, div, names);
    // Set crossOrigin on any images we just appended
    div.querySelectorAll('img').forEach(img => {
      if (!img.crossOrigin) img.crossOrigin = 'anonymous';
      // If images are on a CDN you control, make sure it sends: Access-Control-Allow-Origin: *
    });
  };

  document.getElementById('savePng').addEventListener('click', async () => {
    const chartEl = document.getElementById('chart');

    // Ensure the connector canvas is up to date (your code already draws on load)
    // Optionally re-run your layout routine here if you draw on resize.

    // 2x scale = sharper export; increase to 3 for print quality
    const scale = 3;

    const canvas = await html2canvas(chartEl, {
      backgroundColor: '#fff',
      scale,
      useCORS: true,
      logging: false,
      windowWidth: chartEl.scrollWidth,
      windowHeight: chartEl.scrollHeight
    });

    const link = document.createElement('a');
    link.download = 'uscms-sc-org-chart.png';
    link.href = canvas.toDataURL('image/png');
    link.click();


  });
</script>
