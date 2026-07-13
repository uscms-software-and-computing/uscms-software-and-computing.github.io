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
  end: 2027-06-30
photo: /assets/images/team/Matteo-Marchegiani.jpeg
institution: Carnegie Mellon University
e-mail: mmarcheg@andrew.cmu.edu
project_title: GNN-based End-to-End Reconstruction in the CMS Phase 2 High-Granularity Calorimeter
mentors:
  - Matteo Cremonesi - (Carnegie Mellon University)
project_goal: >
    <br>
    <b>2026-2027 Transformer-based End-to-End Reconstruction in the CMS Phase 2 High-Granularity Calorimeter</b>
    <br>
    Building on the GNN-based reconstruction developed in the first year, the goal of this second project is to study transformer-based architectures, and specifically MaskFormers, as an alternative approach to end-to-end reconstruction in the HGCAL. A transformer with full self-attention is equivalent to a fully-connected message-passing GNN, offering greater expressivity than the local graph connectivity used by GNNs, and masked attention mitigates the quadratic complexity that would otherwise result from attending over the up to 200k hits expected per event at 200 pile-up. The project starts by interfacing the existing HGCAL training datasets with a MaskFormer model, aggregating information from multiple detector hits into composed objects, the topoclusters, to keep the self-attention matrix computationally tractable. The model is then trained with progressively higher pile-up (0, 30, and 200 collisions), monitoring memory and compute costs against the CMS Phase-2 offline processing budget, before its energy, position and time resolution and response are benchmarked against the GNN baseline using the same performance-metric infrastructure developed in the prior award.
    <br>
    <a href=/assets/pdfs/Matteo-Marchegiani_proposal_2026.pdf>2026 Project proposal</a>
    <br>
    <br>
    <b>2025-2026 GNN-based End-to-End Reconstruction in the CMS Phase 2 High-Granularity Calorimeter</b>
    <br>
    The High-Luminosity LHC (HL-LHC) will deliver up to 200 simultaneous interactions per bunch crossing (pile-up), posing an exceptional challenge for particle-shower reconstruction in the CMS Phase 2 High-Granularity Calorimeter (HGCAL). The goal of this project is to develop Graph Neural Network (GNN) based algorithms for fast and efficient end-to-end reconstruction of particle showers in the HGCAL, capable of meeting this challenge. Building on an existing proof-of-concept model that uses GravConv layers together with the Object Condensation loss function to reconstruct energy clusters from simulated di-tau decays with zero pile-up, the project extends this approach to realistic HL-LHC pile-up conditions. This requires deriving a scalable, pile-up-aware training dataset by combining full-simulation truth information from FineCalo with a dedicated library of minimum-bias events and a merging algorithm that reconciles truth information between the hard-scatter and pile-up interactions, as well as re-engineering and optimizing the Object Condensation loss function to overcome GPU memory limitations at high pile-up and to improve physics performance, exploring alternatives such as the modified differential multiplier method and the influencer loss.
    <br>
    <a href=/assets/pdfs/Matteo-Marchegiani_proposal_2025.pdf>2025 Project proposal</a>
    <br>
proposal: /assets/pdfs/Matteo-Marchegiani_proposal_2026.pdf

presentations:
  - title: GNN-based end-to-end reconstruction in the CMS Phase-2 High-Granularity Calorimeter
    date: May 25, 2026
    url: https://indico.cern.ch/event/1471803/contributions/6967243/attachments/3281070/5863445/CHEP-2026_GNN-based_end-to-end_reconstruction_CMS-HGCAL.pdf
    meeting: CHEP 2026
    meetingurl: https://indico.cern.ch/event/1471803/
  - title: GNN-based end-to-end reconstruction in the CMS Phase-2 High-Granularity Calorimeter
    date: May 15, 2026
    url: https://indico.cern.ch/event/1686056/contributions/7087349/attachments/3275631/5853132/GNN-HGCAL-Reconstruction_DP-Note_final.pdf
    meeting: DPG Plot Approval Meeting
    meetingurl: https://indico.cern.ch/event/1686056/
  - title: GNN-based end-to-end reconstruction in the CMS Phase-2 High-Granularity Calorimeter
    date: May 7, 2026
    url: https://indico.cern.ch/event/1639406/contributions/7083113/attachments/3270778/5842725/GNN-DP-Note_v0.pdf
    meeting: TICL Reconstruction Working Meeting
    meetingurl: https://indico.cern.ch/event/1639406/
  - title: HGCAL reconstruction with Graph Neural Networks
    date: April 23, 2026
    url: https://indico.cern.ch/event/1639405/sessions/645094/attachments/3262322/5825235/26.04.23_HGCAL_GNN_offline_reconstruction.pdf
    meeting: TICL Reconstruction Working Meeting
    meetingurl: https://indico.cern.ch/event/1639405/
  - title: HGCAL reconstruction with Graph Neural Networks
    date: March 26, 2026
    url: https://indico.cern.ch/event/1639403/contributions/7016065/attachments/3246468/5792247/26.03.26_HGCAL_GNN_offline_reconstruction.pdf
    meeting: TICL Reconstruction Working Meeting
    meetingurl: https://indico.cern.ch/event/1639403/
  - title: HGCAL simulation with pileup and merging algorithm
    date: March 24, 2026
    url: https://indico.cern.ch/event/1667437/contributions/7010124/attachments/3244695/5788733/26.03.24_ML4reco_pileup_simulation.pdf
    meeting: ML4RECO
    meetingurl: https://indico.cern.ch/event/1667437/
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
    <b>2026 Q2 </b>
    <br>

    *   Working on training of GNN model with 200 pileup simulation
        *   First training with 30 PU using SimCluster features as input
    *   Study new alternative ML architectures for HGCAL reconstruction
        *   Generated large 0 PU dataset with RecHits and TICL objects to train a large model
        *   New training using recHits features as input on 1000 events: incidence matrix regression and regression of cluster properties
        *   Optimization of the model's architecture and parameters
    *   Publication of DP Note on GNN-based HGCAL reconstruction
        *   GravNet model trained with object condensation loss with 0 PU simulation
        *   MC truth: CMSSW-native SimClusters
        *   Presentation at CHEP 2026

    <br>
    <b>2026 Q1 </b>
    <br>

    *   Progress on optimized GNN model
        *   Study impact of pileup on the training of the GNN-based reconstruction algorithm
        *   GPU Memory profiling of GNN model trained on dataset with 5x more hits
        *   Integration of CUDA kernels from FastGraphCompute to speed up KNN and object condensation loss
    *   Working on training of GNN model with 200 pileup simulation
        *   First HGCAL simulation with FineCalo + merging algorithm in CMSSW_15_1_0
        *   Simulated 10 single-electron events + 30 PU interactions from minimum bias events
        *   Implementation of custom NANO step to save true clusters containing SimHits from primary interaction and pileup
        *   At 30 PU, the average number of RecHits is ~60k, with ~8k true clusters
        *   Study a dedicated implementation of the merging algorithm which is compatible with pileup
        *   Study a dedicated pileup mixing library to save the event history for minimum bias events in the merging
    *   Study new alternative ML architectures for HGCAL reconstruction
        *   Masked transformers to reduce the quadratic complexity of self-attention
        *   Generated 0 PU dataset with RecHits and TICL objects: 2D LayerClusters, 3D Tracksters and TICL Candidates
        *   Computing the incidence matrix between RecHits and true particles using sparse tensor representation
        *   First proof-of-concept training using recHits features as input: incidence matrix regression and regression of cluster properties

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
