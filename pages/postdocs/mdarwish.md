---
layout: postdoc
pagetype: postdoc
shortname: moanwar
permalink: /postdocs/Moanwar.html
postdoc-name: Mohamed Darwish
title: Post-doctoral researcher
active: False
dates:
  start: 2024-03-01
  end: 2025-11-30
photo: /assets/images/team/Mohamed-Darwish.jpg
institution: Baylor University
e-mail: mohamed.anwar@cern.ch
project_title: Developing heterogeneous particle flow reconstruction for the CMS Phase 2 detector
project_goal: >
    The goal of the project is to develop particle flow reconstruction for the CMS Phase 2, using 'The Iterative CLustering' (TICL) as a baseline, to improve physics performance, and to establish a coherent PF reconstruction across all calorimeters. TICL is a modular framework developed for heterogeneous infrastructure that provides particle shower reconstruction and particle flow candidate reconstruction. It was primarily developed for HGCAL but could also work well for other calorimeter regions, thus enabling coherent reconstruction across all calorimeter regions. Additionally, we will work on further completing the transition of the CUDA-based software-implemented PF modules to a portability library, 'Alpaka,' and deploy it not only for use at the high-level trigger (HLT) but also for offline reconstruction.
mentors: >
  - Kenichi Hatakeyama - (Baylor University)

proposal: /assets/pdfs/Mohamed-Darwish.pdf
presentations:
  - title: "Energy regression and PID"
    date: "June 6, 2024"
    url: https://indico.cern.ch/event/1414106/sessions/547218/attachments/2872414/5029541/Ticl_Meeting_6Jun.pdf
    meeting: TICL Reconstruction Working Meeting
    meetingurl: https://indico.cern.ch/event/1414106/
  - title: "Upates on Energy regression and PID"
    date: "June 13, 2024"
    url: https://indico.cern.ch/event/1414122/sessions/547234/attachments/2876913/5038451/Ticl_Meeting_13Jun.pdf
    meeting: TICL Reconstruction Working Meeting
    meetingurl: https://indico.cern.ch/event/1414122/

current_status: >

  <br>
  <b>2024 Q2 </b>
  <br>
  
  *   Progress
      *   Our first task is participating in updating TICLv4 to TICLv5, which is responsible for object reconstruction in the HGCAL. We started by working on the linking between the tracksters and tracks within TICLv5.
      *   While working on the linking, we identified a group of bugs within the code. Fortunately, thanks to the prompt response from the team, all the reported issues have been successfully resolved.
      *   We started updating the DNN model responsible for energy regression and particle identification (PID). First, we retrained the model to account for the improvements in the code that will be included in v5. Additionally, we split the model into two separate models: one for energy regression and one for PID.
      *   We then updated and optimized the models to enhance their efficiency, saving them in ONNX format. Additionally, we optimized them for prediction time to ensure faster evaluation times.
      *   We successfully integrated the new models within TICLv5 in CMSSW.
  
  *   Next steps
      *   We are looking forward to merging the updates into the official CMSSW releases
      *   Try using GNN (Graph Neural Network) for energy regression and PID instead of CNN.
      *   We will proceed to enhance the linking between tracksters and tracks within the code.
---
