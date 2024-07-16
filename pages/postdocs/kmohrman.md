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
    LST is a tracking algorithm that takes advantage of double-layer design of the HL-LHC outer tracker in order to perform hit correlations in a parallel way with GPUs.
    SONIC is a framework that provides GPUs as a service to clients running at different sites. 
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

  - title: "Project status update: LST with the SONIC framework"
    date: "February 12, 2023"
    url: <https://indico.cern.ch/event/1374894/contributions/5778400/attachments/2799411/4883360/sonic_lst_update_feb12_2024.pdf>
    meeting: <Tracking POG Meeting>
    meetingurl: <https://indico.cern.ch/event/1374894/>


current_status: 
  - Preliminary work
    - First learned to run the LST workflow in order to reproduce LST plots from Philip Chang's LST CHEP presentation. Set up at Purdue and ran the test SONIC workflow (MAOD workflow) and successfully ran the setup where the cmsRun script runs on the login node, and the cmsTriton script runs on a different node. Have gotten the same workflow running at UF (with cmsRun on one node without any GPUs and cmsTriton on a different node). Tested with cmsRun at Purdue and cmsTriton at UF, but hit issue with nodes not being able to talk to each other, paused this direction for now.
  - Setting up LST backend
    - Successfully set up and ran example Patatrack as a service example at Purdue and at UF. Produced a draft version of SONIC compatible LST producer. Removed ROOT dependencies from LST in order to enable the successful compilation and running of the standalone TrackLooper LST within the server singularity environment from the SONIC PatatrackAAS example. Created a backend (modeled after the PatatrackAAS identity_backend example) that can compile and run LST (though currently the inputs to the evaluation are already hard coded within the backend) using the PatatrackAAS client as a standin to trigger the backend code to be run.
  - Next steps
    - Work on connecting the LST client side with the server side to enable the transfer LST inputs from the client to the backend, and to return the results back to the client

---
