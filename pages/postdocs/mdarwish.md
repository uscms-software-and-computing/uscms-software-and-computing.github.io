---
layout: postdoc
pagetype: postdoc
shortname: moanwar
permalink: /postdocs/Moanwar.html
postdoc-name: Mohamed Darwish
title: Post-doctoral researcher
active: True
dates:
  start: 2024-04-01
  end: 2027-03-31
photo: /assets/images/team/Mohamed-Darwish.jpg
institution: Baylor University
e-mail: mohamed.anwar@cern.ch
project_title: Machine learning based particle flow reconstruction for the CMS Phase 2 detector (2026) and Developing heterogeneous particle flow reconstruction for the CMS Phase 2 detector (2025)
project_goal: >
    <br>
    <b>2026-2027: Machine learning based particle flow reconstruction for the CMS Phase 2 detector </b>
    The goal of this project is to develop a machine learning-based approach for producing final particle-flow candidates under the high-pileup conditions expected at the High-Luminosity LHC (HL-LHC) with the Phase2 CMS detector. Inspired by the MLPF model developed during Run 3, the new approach builds directly on top of the existing Phase2 particle-flow reconstruction framework, TICL (The Iterative Clustering), using its tracksters and tracks as inputs to deliver well-optimized final particle-flow objects. Multiple architectures will be explored and benchmarked, including transformer-based models and hypergraph networks, with dedicated validation tools will be developed to ensure fair and rigorous performance comparisons across approaches. The final design will be fully integrated into the TICL algorithm and adapted to run on heterogeneous computing resources, enabling deployment on both CPU and GPU backends depending on available hardware.
    <br>
    <a href=https://mohamed.web.cern.ch/us_projects/proposals/USCMS_HLLHC_SC_2026.pdf>2026 Project proposal</a>
    <br>
    <br>
    <b>2024-2025: Developing heterogeneous particle flow reconstruction for the CMS Phase 2 detector </b>
    <br>
The goal of the project is to develop particle flow reconstruction for the CMS Phase 2, using 'The Iterative CLustering' (TICL) as a baseline, to improve physics performance, and to establish a coherent PF reconstruction across all calorimeters. TICL is a modular framework developed for heterogeneous infrastructure that provides particle shower reconstruction and particle flow candidate reconstruction. It was primarily developed for HGCAL but could also work well for other calorimeter regions, thus enabling coherent reconstruction across all calorimeter regions. Additionally, we will work on further completing the transition of the CUDA-based software-implemented PF modules to a portability library, 'Alpaka,' and deploy it not only for use at the high-level trigger (HLT) but also for offline reconstruction.
    <br>
    <a href=https://mohamed.web.cern.ch/us_projects/proposals/CMS_HLLHC_SC_2023.pdf>2024 Project proposal</a>
    <br>

mentors: >
  - Kenichi Hatakeyama - (Baylor University)

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
  - title: "Progress in updating PID and linking regression for TICLv5"
    date: "Jan 15, 2025"
    url: https://indico.cern.ch/event/1495693/#3-progress-in-updating-pid-and
    meeting: The HGCAL DPG meeting
  - title: "Study Track - Tracksters Linking in TICLv5"
    date: "June 19, 2025"
    url: https://indico.cern.ch/event/1520090/sessions/593673/attachments/3089837/5472010/meeting_19June.pdf
    meeting: TICL Reconstruction Working Meeting
  - title: "GNN Track-Trackster Linking"
    date: "Nov 13, 2025"
    url: https://indico.cern.ch/event/1511035/sessions/590339/attachments/3173213/5642244/GNN_link_updates_v2.pdf
    meeting: TICL Reconstruction Working Meeting
  - title: "Tracksters linking with GNNs for HGCAL reconstruction with TICL"
    date: "Nov 18, 2025"
    url: https://indico.cern.ch/event/1612036/#17-tracksters-linking-with-gnn
    meeting: Machine Learning for Reconstruction (ML4RECO)
  - title: "GNN-assisted trackster linking"
    date: "Dec 18, 2025"
    url: https://indico.cern.ch/event/1621802/#5-gnn-assisted-trackster-linki
    meeting: The HGCAL DPG meeting
  - title: "Overview of ML in TICL"
    date: "Feb 9, 2026"
    url: https://indico.cern.ch/event/1645749/#17-overview-of-ml-in-ticl
    meeting: CMS-Week (HGCAL DPG - Focus on reconstruction)


current_status: >
    <br>
    <b>2024 Q2 </b>
    <br>

  *   Progress
      *   Integrated new ML models into TICLv5 within CMSSW; CNNs/DNNs selected as best performers for particle ID at CLUE3D and Linking steps.
      *   Built a new plugin system for conflict-free model integration; converted TICLv4 TensorFlow model to ONNX format.
      *   Merged PR #45821 and PR #6; HLT timing improved ~3.4% (5547 -> 5356 ms/event).
  *   Next Steps
      *   Extend model validation to 200 PU samples for robustness.

    <br>
    <b>2024 Q3 </b>
    <br>

  *   Progress
      *   Group presented TICL framework at CHEP24 conference (as contributing authors).
      *   Extended PID and energy regression models from 0 PU to 200 PU samples.
  *   Next Steps
      *   Finalise and integrate updated models into CMSSW.

    <br>
    <b>2024 Q4 </b>
    <br>

  *   Progress
      *   Finalised PFN-based models (PID at CLUE3D, PID at Linking, Regression at Linking) using 200 PU samples; presented at HGCAL DPG meeting with positive feedback.
      *   Integrated all three models into CMSSW as defaults in TICLv5.
  *   Next Steps
      *   Resolve mismatch: Regression/PID trained on TiclCandidate but applied at Linking step.
      *   Study trackster-track features to improve matching in TICL.

    <br>
    <b>2025 Q1 </b>
    <br>

  *   Progress
      *   Identified geometric matching (DeltaR) as the main source of track–trackster linking inefficiency.
      *   Developed a BDT model to dynamically predict optimal DeltaR per track; achieved ~10% efficiency improvement in CMSSW.
      *   Explored GNN-based linking: ~97% accuracy in preliminary results, presented at TICL meeting.
  *   Next Steps
      *   Validate GNN approach and prepare integration PR into TICL.

    <br>
    <b>2025 Q2 </b>
    <br>

  *   Progress
      *   GNN linking achieved >98% efficiency vs ~80% with previous cuts; presented at TICL meeting.
      *   Fixed ONNX interface bug for variable batch sizes (PR #48725, merged).
      *   Started PF jet validation to benchmark regression retraining.
  *   Next Steps
      *   Submit GNN linking PR; complete regression retraining.

    <br>
    <b>2025 Q3 </b>
    <br>

  *   Progress
      *   Fixed bug in recHitTools (missing geometry assignment) causing jet response distortion; submitted PR #49343 + training PR #10.
      *   Retrained PFN regression model post-fix; added geometry assignment protection in recHitTools.
      *   Optimised GNN: updated training samples, wider energy range, pion+kaon mixture, removed MTD features.
      *   Results: >98% efficiency, ~50% reduction in compute time vs standard TICL linking.
  *   Next Steps
      *   Submit ticlv5_GNN process modifier PR for HLT and step3 integration.

    <br>
    <b>2025 Q4 </b>
    <br>

  *   Progress
      *   Merged GNN linking model (PR #49652) via ticlv5_GNN modifier; >98% efficiency.
      *   Optimised PID models for faster inference; supported TICLv4→v5 transition.
      *   Presented ML-in-TICL summary at CMS Week, TICL meeting, and ML4Reco meeting.
  *   Next Steps
      *   Continue ML maintenance in TICLv5; monitor and optimise models in production.
---
