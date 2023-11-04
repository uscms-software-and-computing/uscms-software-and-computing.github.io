---
layout: postdoc
pagetype: postdoc
shortname: kmohrman
permalink: /postdocs/kmohrman.html
postdoc-name: Kelci Mohrman
title: Post-doctoral researcher
active: True
dates:
  start: 2023-07-01
  end: 2024-06-30
photo: /assets/images/team/Kelci-Mohrman.png
institution: University of Florida
e-mail: k.mohrman@ufl.edu
project_title: Deploying GPU algorithms through SONIC
project_goal: >
    The goal of the project is to demonstrate at a sufficiently large scale the reconstruction algorithm workflow within CMSSW to be processed, where the client jobs are running on one site, while the Line Segment Tracking (LST) algorithm will be executed on GPUs on computing nodes at another site connected through SONIC (Services for Optimized Network Inference on Co-processors) framework.
    LST (Line Segment Tracking) is a tracking algorithm that takes advantage of double-layer design of the HL-LHC outer tracker in order to perform hit correlations in a parallel way with GPUs.
    SONIC (Services for Optimized Network Inference on Co-processors) is a framework that provides GPUs as a service to clients running at different sites. 
    Combining the LST algorithm with the SONIC framework is the goal of the project, in which we aim to to demonstrate the execution of the LST algorithm on GPUs at an external site (apart from the site where the client jobs are run) via the SONIC framework.
mentors:
  - Philip Chang - (University of Florida)

proposal: /assets/pdfs/Kelci-Mohrman.pdf

presentations:
  - title: "Project introduction and plans: LST with the SONIC framework"
    date: "October 23, 2023"
    url: <https://indico.cern.ch/event/1337451/contributions/5630393/attachments/2738948/4763938/kmohrman_sonic_lst_intro_oct23_2023.pdf>
    meeting: <Tracking POG Meeting>
    meetingurl: <https://indico.cern.ch/event/1337451/>

current_status: 
  - The project is in progress
    - Learned to run the LST workflow in order to reproduce LST plots from Philip Chang's LST CHEP presentation
    - Have gotten set up at Purdue and run the test SONIC workflow (MAOD workflow) and successfully ran the setup where the cmsRun script runs on the login node, and the cmsTriton script runs on a different node
    - Have gotten the workflow (same one we got running at Purdue) running at UF (with cmsRun on one node without any GPUs and cmsTriton on a different node)
    - Tested with cmsRun at Purdue and cmsTriton at UF, but hit issue with nodes not being able to talk to each other, paused this direction for now
    - Currently working to adapt the LST workflow with SONIC (starting with the client side i.e. reworking the producer with SONIC)
---
