---
permalink: /postdocs/postdoc-carlosericecid.html
layout: postdoc
pagetype: postdoc
active: False
title: Post-doctoral researcher
postdoc-name: Carlos Erice Cid
shortname: cericeci
project_title: Accelerating Pixel Unpacking and Vertex Reconstruction with GPUs
dates:
  start: 2021-10-01
  end: 2025-09-30
photo: /assets/images/team/Carlos-Erice-Cid.png
institution: Boston University
website:
e-mail: carlos.francisco.erice.cid@cern.ch
mentors:
  - David Sperka (Boston University)
  - Zeynep Demiragli (Boston University)	
project_goal: >
  The proposed project consists of two thrusts: (1) adapting pixel unpacking to execute on GPUs and (2) adapting the vertex reconstruction algorithm to execute on GPUs and, more in general, to generic heterogeneous architectures through the Alpaka libraries. These projects are synergistic and leverage existing expertise at Boston University in back-end readout electronics to expand the group's research program into the area of heterogeneous computing for the HL-LHC era. The pixel unpacking project will serve as an educational bridge project, and the vertex reconstruction effort will take advantage of the gained expertise to accelerate a resource-intensive portion of the HL-LHC reconstruction.
presentations:
  - title: "Update on heterogeneous vertexing: Alpaka migration"
    date: 2024-03-11
    url: https://indico.cern.ch/event/1387237/contributions/5851271/attachments/2817240/4918586/PV_forTRKPOG_Mar11-1.pdf
    meeting: TRK POG meeting 
    meetingurl: https://indico.cern.ch/event/1387237/
  - title: "Heterogeneous Primary Vertex reconstruction with Alpaka"
    date: 2023-12-18
    url: https://indico.cern.ch/event/1354273/contributions/5712248/attachments/2774247/4834397/PV_forTRKPOG_Dec18.pdf
    meeting: TRK POG meeting
    meetingurl: https://indico.cern.ch/event/1354273/
  - title: "GPU-based algorithms for primary vertex reconstruction at CMS"
    date: 2023-05-08
    url: https://indico.jlab.org/event/459/contributions/11412/
    meeting: "CHEP2023: 26th International Conference on Computing in High Energy Physics and Nuclear Physics"
    meetingurl: https://indico.jlab.org/event/459/
  - title: "Phase-2 Software Days"
    date: "2023-03-10"
    url: https://indico.cern.ch/event/1247039/contributions/5296624/subcontributions/415811/attachments/2608553/4506209/PV_forPhase2Software.pdf
    meeting: https://indico.cern.ch/event/1247039/
    meetingurl: https://indico.cern.ch/event/1247039/
  - title: "Update on the Deterministic Annealing PV reconstruction on GPU"
    date: "2022-09-12"
    url: https://indico.cern.ch/event/1192252/contributions/5037182/attachments/2506691/4307241/HLT%20GPU%20Offline%20Primary%20Vertex%20for%20Heterogeneous%20Architectures.pdf
    meeting: HLT developments with GPUs
    meetingurl: https://indico.cern.ch/event/1192252/
  - title: "GPU-based algorithms for the CMS track clustering and primary vertex reconstruction for the Run 3 and Phase II of the LHC"
    date: "2022-06-02"  
    url: https://indico.cern.ch/event/1103637/contributions/4821874/
    meeting: "CTD2022: 7th International Connecting the Dots Workshop"
    meetingurl: https://indico.cern.ch/event/1103637/
  - title: "Deterministic annealing vertex reconstruction on GPU"
    date: "2022-03-11"
    url: https://indico.cern.ch/event/1144949/contributions/4823046/attachments/2425113/4151697/PV_Apr11_HLTGPUmeeting.pdf
    meeting: HLT developments with GPUs
    meetingurl: https://indico.cern.ch/event/1144949/
  - title: "Primary Vertex Reconstruction on GPUs"
    date: "2023-05-01"
    url: https://indico.cern.ch/event/1281717/contributions/5384813/attachments/2638589/4565671/PV_forRD_May.pdf
    meeting: HL-LHC R&D Initiative Meeting
    meetingurl: https://indico.cern.ch/event/1281717/
  - title: "Primary Vertex Reconstruction"
    date: "2022-11-11"
    url: https://indico.cern.ch/event/1196991/contributions/5091775/attachments/2526591/4345864/PV_forRD_Oct.pdf
    meeting: HL-LHC R&D Initiative Meeting
    meetingurl: https://indico.cern.ch/event/1196991/
  - title: "Vertex Reconstruction on GPUs"
    date: "2022-03-19"
    url: https://indico.cern.ch/event/1152278/contributions/4835901/attachments/2428318/4157635/PV_Apr19_PVGPU_PhaseIIR&D.pdf
    meeting: HL-LHC R&D Initiative Meeting
    meetingurl: https://indico.cern.ch/event/1152278/
  - title: "Primary Vertex Reconstruction on GPUs"
    date: "2021-11-16"
    url: https://indico.cern.ch/event/1097778/contributions/4619034/attachments/2347253/4002840/HL-LHC_R&D_Carlos_v2.pdf
    meeting: HL-LHC R&D Initiative Meeting
    meetingurl: https://indico.cern.ch/event/1097778/

proposal: /assets/pdfs/USCMS_CarlosEriceCid.pdf


current_status: >

  <br>
  <b>2024 Q2</b>
  <br>

  After the porting of the vertexing to Alpaka we worked to solve a significant issue related that was causing a significant compilation time (2+ hours) to make it something usable at the central production level and applied some additional recommendations to other parts of the code (including the usage of common objects for other items shared by the reco chain, such as BeamSpot). To discuss this with experts we presented it into the HLT development with [GPUs meeting](https://indico.cern.ch/event/1350959/contributions/6008868/attachments/2879300/5043707/PV_forHLTGPU_June17-4.pdf) and got some additional feedback for its validation. We also presented a summary of the status and plans in the [US-CMS All-Hands workshop](https://indico.cern.ch/event/1406858/contributions/5913032/subcontributions/486559/attachments/2877545/5039820/PV_forHandsOnMeeting_June13-1.pdf) including our short terms and longer plans for the inclusion of timing.


  <br>
  <b>2024 Q1</b>
  <br>

  We finished the migration to Alpaka of the 3D vertex clustering (Deterministic Annealing in Blocks) with weighted means fitter. The validation and timing measurements were presented at the Tracking POG meeting
  We got several comments since and are now in the process of incorporating them and opening the official PR into CMSSW. We will now begin to explore the inclusion of timing information in the Alpaka/GPU implementation.
      
  <br>
  <b>2023 Q4</b>
  <br>

  In this quarter we continued with the implementation of the vertexing code as an Alpaka  plugin for cms-sw and started measuring its performance. We currently have a working version of the whole 3D vertexing (clusterizing + fitting) working both as a standalone CUDA and an Alpaka version. Our most immediate plans are to show the current setup on the TRK POG (we are scheduled for a presentation late December) and start the process of a PR to central cms-sw to make available with the collaboration. In parallel we plan on working  version of the code for 4D vertexing (including timing) for the next quarter.
      
  <br>
  <b>2023 Q3</b>
  <br>

  This quarter we finalized a CUDA version of the vertex fitting code and provided improvements in the internal GPU dataformat so the CPU-GPU copying time is reduced. We provided a first comparison of the full on-GPU algorithm with the equivalent full on-CPU ones and progressed in the Alpaka porting of the code. For the later we plan to take part in the incoming Hackathon in October to further discuss its possibilities with Alpaka experts.
      

---
