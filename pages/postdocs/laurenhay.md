---
layout: postdoc
pagetype: postdoc
shortname: laurenhay
permalink: /postdocs/laurenhay.html
postdoc-name: Lauren Hay
title: Post-doctoral researcher
active: True
dates:
  start: 2026-04-01
  end: 2027-03-31
photo: /assets/images/team/Lauren-Hay.jpeg
institution: Brown University
e-mail: laurenhay@brown.edu
project_title: Reducing storage needs through negative weight mitigation in MC events and lossy compression
mentors:
  - Matt LeBlanc (Brown University)
project_goal: >
  Aim to reduce tape and disk storage needs through developing slimmer data formats  by removing or compressing redundant/and or unused information. Additionally reduce disk storage needs by improving efficiency of MC generators by mitigating negative weights after generation.

proposal: /assets/pdfs/Lauren-Hay.pdf

presentations:
  - title: "Cell Reweighting Algorithms for Pathological Weight Mitigation in LHC Simulations using Optimal Transport"
    date: "May 26, 2026"
    url: https://indico.cern.ch/event/1471803/contributions/6967988/attachments/3283390/5868173/NegWeights_CHEP2026_Hay.pdf
    meeting: CHEP 2026
    meetingurl: https://indico.cern.ch/event/1471803/contributions/6967988/
  - title: "Resampling Away Negative Weights with Optimal Transport"
    date: "July 17, 2026"
    url: https://indico.fnal.gov/event/73553/contributions/344375/attachments/199579/278158/Fermilab_FP_2026_NegWeights.pdf
    meeting: CHEP 2026
    meetingurl: https://indico.fnal.gov/event/73553/contributions/344375/
    
current_status: >
   <br>
   <b>2026 Q2 </b>
   <br>

   *   Progress
       *   Finalized studies of OT based cell-resampling of negative weights in generic herwig samples.
           *   Presented results at CHEP 2026.
       *   First attempt at training AE for compressing particle candidates.
           *   Tried MSE and sliced-Wasserstein based loss functions with some success.
           *   Still have issues in deconding constituent pT's -- this causes an underestimation of jet mass and pT.
           *   Likely need to try an alternative architecture
      *   Began investigating lossy compression implementation in CMSSW and it's physics performance.
---