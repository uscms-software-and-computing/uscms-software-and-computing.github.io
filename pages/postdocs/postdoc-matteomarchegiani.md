---
layout: postdoc
pagetype: postdoc
shortname: mmarcheg
permalink: /postdocs/postdoc-matteomarchegiani.html
postdoc-name: Matteo Marchegiani
title: Post-doctoral researcher
active: True
dates:
  start: 2025-07-01
  end: 2026-06-30
photo: /assets/images/team/Matteo-Marchegiani.jpeg
institution: Carnegie Mellon University
e-mail: mmarcheg@andrew.cmu.edu
project_title: GNN-based End-to-End Reconstruction in the CMS Phase 2 High-Granularity Calorimeter
mentors:
  - Matteo Cremonesi - (Carnegie Mellon University)
project_goal: >
  The goal of the project is to develop new machine learning based algorithms for fast and efficient reconstruction of the High-Granularity Calorimeter at the High-Luminosity LHC.
proposal: /assets/pdfs/Matteo-Marchegiani_proposal_2025.pdf

presentations:
  - title: Maskformers for offline reconstruction
    date: February 10, 2026
    url: https://indico.cern.ch/event/1649883/contributions/6935005/attachments/3217627/5732543/26.02.10_ML4reco_maskformers_offline.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1649883/
  - title: Studies on time resolution in GNN-based reco
    date: December 3, 2025
    url: https://indico.cern.ch/event/1617166/contributions/6819529/attachments/3185911/5668415/hgcal-dpg_gnn-time-resolution.pdf
    meeting: HGCAL DPG
    meetingurl: https://indico.cern.ch/event/1617166/
  - title: Studies on time resolution with the latest HGCAL GNN model
    date: December 2, 2025
    url: https://indico.cern.ch/event/1615761/contributions/6818543/attachments/3184951/5666518/ml4reco_gnn-time-resolution-update.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1615761/
  - title: "Update on performance of the latest HGCAL GNN model"
    date: "November 18, 2025"
    url: https://indico.cern.ch/event/1612036/contributions/6792820/attachments/3176426/5649043/ml4reco_gnn-based-particle-reconstruction_update.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1612036/
  - title: "ML4RECO: GNN and Transformer Based HGCAL Reconstruction"
    date: "October 13, 2025"
    url: https://indico.cern.ch/event/1593611/contributions/6737584/attachments/3153545/5600652/25.10.13_MLG_TownHall_HGCAL_reco.pdf
    meeting: CMS Machine Learning Town Hall
    meetingurl: https://indico.cern.ch/event/1593611/contributions/6737584/
  - title: Single-particle energy resolution with latest GNN model
    date: "September 17, 2025"
    url: https://indico.cern.ch/event/1587360/contributions/6689475/attachments/3137672/5567817/ml4reco-gnn-new-training-physics-metrics-update.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1587360/
  - title: Updated GNN training after bugfixes in CMSSW 15_0_X
    date: "August 27, 2025"
    url: https://indico.cern.ch/event/1579980/contributions/6658969/attachments/3124101/5540514/ml4reco-gnn-finecalo-simtrack-error-fix-training-update.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1579980/
  - title: FineCalo SimTrack Reconstruction Error
    date: "July 16, 2025"
    url: https://indico.cern.ch/event/1569687/contributions/6612371/attachments/3105373/5503441/ml4reco-gnn-finecalo-simtrack-error.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1569687/

current_status: >
    <br>
    <b>2025 Q4 </b>
    <br>

    *   Progress
        *   Study energy, position and time resolution of the GNN clustering using simulated photons, pions and tau leptons
        *   Study issue in time resolution in CMSSW_15_X: change in the timing simulation with respect to CMSSW_11_X
        *   Finalize publication on performance metrics of GNN clustering with 0 pileup simulation
        *   Study the impact of increased pileup on the GNN training
        *   Memory profiling of the training with a dataset including ~250k reconstructed hits
        *   Working on pileup simulation: generate hard process alongside minimum bias events

    <br>
    <b>2025 Q3 </b>
    <br>

    *   Progress
        *   Learned how to train the GNN employing GravConv layers in combination with the object condensation loss for the reconstruction of energy clusters in the HGCAL
        *   Studied the performance and energy resolution of the GNN-based reconstruction in zero-pileup environments, considering simulated photons, pions and tau leptons
        *   Ported the training datasets production to CMSSW_15_1_X, making use of the FineCalo simulation
        *   Ported the GNN training to Pytorch 2.6.0 and CUDA 12.4
        *   Study memory profiling of the model on GPU

---
