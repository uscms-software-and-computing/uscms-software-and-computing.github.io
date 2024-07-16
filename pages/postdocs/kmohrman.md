---
layout: postdoc
pagetype: postdoc
shortname: kmohrman
permalink: /postdocs/kmohrman.html
postdoc-name: Kelci Mohrman
title: Post-doctoral researcher
active: True
dates:
  start: 2023-09-01
  end: 2024-08-31
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
  - title: "Line Segment Tracking using SONIC"
    date: "June 3, 2024"
    url: <https://indico.cern.ch/event/1418266/contributions/5961841/attachments/2869550/5023598/sonic_lst_update_jun03_2024.pdf>
    meeting: <Tracking POG Meeting>
    meetingurl: <https://indico.cern.ch/event/1418266/#35-line-segment-tracking-using>

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
    <br>
    <b>2024 Q2 </b>
    <br>
    Progress
    <ul>
        <li>
        Completed first working version of SONICized LST client and backend (where data is passed from client to server, LST evaluations are performed at the server, and outputs are sent back to the client)
        </li>
        <li>
        Demonstrated the ability to run the SONICized LST workflow with client and server on different nodes at the same site (Purdue)
        </li>
        <li>
        Performed preliminary timing studies of a simple testing workflow, obtained comparable performance to the standard non-SONIC LST
        </li>
        <li>
        Currently working on tracking down some differences between SONICized LST results and the main branch results
        </li>
    </ul>
    Next steps
    <ul>
        <li>
        Further timing studies to explore the behavior with multiple concurrent instances of the LST workflow (to understand the scaling and how many instances are required to saturate the GPU) 
        </li>
        <li>
        Depending on progress, potentially explore moving to Alpaka backend 
        </li>
        <li>
        Depending on progress, potentially attempt to execute the SONICized LST with client and server at different sites (e.g. UF and Purdue) 
        </li>
    </ul>

    <br>
    <b>2024 Q1</b>
    <br>
    Progress
    <ul>
        <li>
        Removed ROOT dependencies from LST in order to enable the successful compilation and running of the standalone TrackLooper LST within the server singularity environment from an existing example 
        </li>
        <li>
        Created a backend (modeled after the identity_backend example) that can compile and run LST (though currently the inputs to the evaluation are already hard coded within the backend) using an example client as a standin to trigger the backend code to be run 
        </li>
    </ul>
    Next steps
    <ul>
        <li>Work on connecting the LST client side with the server side to enable the transfer LST inputs from the client to the backend, and to return the results back to the client </li>
    </ul>

    <br>
    <b>2023 Q4</b>
    <br>
    Progress
    <ul>
        <li>
        Successfully set up and ran an example at Purdue and at UF
        </li>
        <li>
        Produced a draft version of SONIC compatible LST producer
        </li>
        <li>
        Using the server singularity environment, currently working to compile LST code within the singularity environment (involves extracting LST code from ROOT dependence and validating the changes)
        </li>
    </ul>
    Next steps
    <ul>
        <li>
        Validate the version of the LST code where the ROOT dependences have been removed (and create a PR)
        </li>
        <li>
        Once the LST code is independent from ROOT and able to be compiled within the singularity env, the next step will be to interface between the server side and client side
        </li>
    </ul>

    <br>
    <b>2023 Q3</b>
    <br>
    Progress
    <ul>
        <li>
        Learned to run the LST workflow in order to reproduce LST plots
        </li>
        <li>
        Have gotten set up at Purdue and run their test workflow (MAOD workflow) and successfully ran the setup where the cmsRun script runs on the login node, and the cmsTriton script runs on a different node
        </li>
        <li>
        Have gotten the workflow (same one we got running at Purdue) running at UF (with cmsRun on one node without any GPUs and cmsTriton on a different node)
        </li>
        <li>
        Tested with cmsRun at Purdue and cmsTriton at UF, but hit issue with nodes not being able to talk to each other, paused this direction for now
        </li>
        <li>
        Began working to adapt the LST workflow with SONIC, starting on the "client side" i.e. reworking the producer with SONIC
        </li>
    </ul>
    Next steps
    <ul>
        <li>
        Plan to continue to adapt the LST workflow with SONIC
        </li>
        <li>
        Will present an overview of the project at tracker meeting Oct 30, 2023
        </li>
    </ul>


---
