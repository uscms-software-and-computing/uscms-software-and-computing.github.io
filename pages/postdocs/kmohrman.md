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
  end: 2025-08-31
photo: /assets/images/team/Kelci-Mohrman.png
institution: University of Florida
e-mail: k.mohrman@ufl.edu
project_title: 
project_goal: >
    <br>
    <b>2024-2025: Benchmarking current capabilities and exploring the acceleration of columnar processing via heterogeneous architectures </b>
    <br> 
    This project aims to benchmark the performance of the step of late-stage data analysis (in which nanoAOD formatted data is transformed into histograms) for realistic CMS analyses in order to understand current capabilities, scaling, and bottlenecks for columnar analysis workflows; acceleration of the columnar processing via GPU offloading will also be explored. 
    The results of these studies will help to illuminate the challenges and opportunities that lie ahead as CMS pushes towards rapid and efficient turnarounds of HL-LHC physics analyses. 
    An ongoing CMS multi-boson analysis will be used as the example application for the proposed explorations. 
    The analysis is fairly representative of a mature CMS analysis studying Run 2 and early Run 3 data, and is implemented in the coffea framework. 
    We will aim to benchmark the performance that is able to be achieved under various configurations in order to understand where the bottlenecks lie and how the analysis scales towards skimming and processing larger data volumes. 
    We will also aim to demonstrate the feasibility of running a portion of the analysis on GPUs and to enumerate the developments that would remain in order to run the analysis fully on GPUs.
    <br> 
    <a href=http://uaf-10.t2.ucsd.edu/~kmohrman/for_uscms/uscms_r_and_d_proposal_2024_coffea/Kelci-Mohrman-2024.pdf>2024 Project proposal</a>
    <br>
    <br> 
    <b>2023-2024: Deploying GPU algorithms through SONIC </b>
    <br> 
    The goal of the project was to implement a version of the Line Segment Tracking (LST) algorithm with the SONIC framework in order to enable flexible and efficient GPU usage. 
    Because reconstruction tasks constitutes the largest fraction of CMS data processing, it is important to understand the resource requirements and to explore options for improving the efficiency of these steps. 
    To this end, CMS is exploring reconstruction algorithms that are designed to make use of GPU resources. 
    These include LST, which is a tracking algorithm that takes advantage of double-layer design of the HL-LHC outer tracker in order to perform hit correlations in a parallel way with GPUs.
    With more algorithms requiring GPU resources, it is important to understand the resource requirements and strategies for ensuring efficient deployment and usage. 
    The SONIC framework provides the ability to make use of GPUs "as a service", enabling GPUs to be factored out of CPU machines. 
    With this approach, the GPU-based servers may be remote from the CPU-based servers, potentially allowing for more flexibility in the usage of GPU resources.
    <br> 
    <a href=http://uaf-10.t2.ucsd.edu/~kmohrman/for_uscms/uscms_r_and_d_proposal_2023_soniclst/Kelci-Mohrman.pdf>2023 Project proposal</a>
    <br> 

mentors:
  - Philip Chang - (University of Florida)


presentations:
  - title: "LST with SONIC framework"
    date: "Sept 9, 2024"
    url: https://indico.cern.ch/event/1443183/contributions/6095381/attachments/2923974/5132502/sonic_lst_summary_sep09_2024.pdf
    meeting: Tracking POG Meeting
    meetingurl: https://indico.cern.ch/event/1443183/#50-update-on-soniclst-developm
  - title: "Line Segment Tracking using SONIC"
    date: "June 3, 2024"
    url: https://indico.cern.ch/event/1418266/contributions/5961841/attachments/2869550/5023598/sonic_lst_update_jun03_2024.pdf
    meeting: Tracking POG Meeting
    meetingurl: https://indico.cern.ch/event/1418266/#35-line-segment-tracking-using
  - title: "Project status update: LST with the SONIC framework"
    date: "February 12, 2024"
    url: https://indico.cern.ch/event/1374894/contributions/5778400/attachments/2799411/4883360/sonic_lst_update_feb12_2024.pdf
    meeting: Tracking POG Meeting
    meetingurl: https://indico.cern.ch/event/1374894/
  - title: "Project introduction and plans: LST with the SONIC framework"
    date: "October 23, 2023"
    url: https://indico.cern.ch/event/1337451/contributions/5630393/attachments/2738948/4763938/kmohrman_sonic_lst_intro_oct23_2023.pdf
    meeting: Tracking POG Meeting
    meetingurl: https://indico.cern.ch/event/1337451/


current_status: >
    <br>
    <b>2024 Q3 </b>
    <br>

    *   Progress
        *   Set up the larger-scale "step3" LST workflow implemented with SONIC (previously had just been running a testing workflow) 
        *   Performed qualitative validation of SONICized LST implementation of the step3 workflow (by running producing the DQM plots and comparing with master branch SONIC)
            * Obtained qualitative agreement. (Exact agreement not expected because the versions of LST being used are slightly different between the master branch and the SONICized implementation. The SONIC LST backend is based on the outdated cuda_branch of LST because Alpaka is not yet available in the server environment for SONIC.)
        * Performed more detailed timing studies (at the Purdue T2)
            * Tested running with multiple concurrent instances of LST cmsRun jobs and measured the runtime and examined the GPU usage
            * Observed the scaling behavior (larger numbers of concurrent instances were taking disproportionately longer to run) but did not seem to be due to saturating the GPU (so there would likely be a bottleneck elsewhere)
            * Observed some differences in the run times between the master branch of LST and the SONICized LST
            * Encountered memory errors before we could saturate the GPU
            * Set up the SONICized LST implementation at a different site (UF T2) and demonstrated successful runs with the client at the Purdue T2 and the server at the UF T2 (and the other way around)

    <br>
    <b>2024 Q2 </b>
    <br>

    *   Progress
        *   Completed first working version of SONICized LST client and backend (where data is passed from client to server, LST evaluations are performed at the server, and outputs are sent back to the client)
        *   Demonstrated the ability to run the SONICized LST workflow with client and server on different nodes at the same site (Purdue)
        *   Performed preliminary timing studies of a simple testing workflow, obtained comparable performance to the standard non-SONIC LST
        *   Currently working on tracking down some differences between SONICized LST results and the main branch results
    *   Next steps
        *   Further timing studies to explore the behavior with multiple concurrent instances of the LST workflow (to understand the scaling and how many instances are required to saturate the GPU) 
        *   Depending on progress, potentially explore moving to Alpaka backend 
        *   Depending on progress, potentially attempt to execute the SONICized LST with client and server at different sites (e.g. UF and Purdue) 

    <br>
    <b>2024 Q1</b>
    <br>

    *   Progress
        *   Removed ROOT dependencies from LST in order to enable the successful compilation and running of the standalone TrackLooper LST within the server singularity environment from an existing example 
        *   Created a backend (modeled after the identity_backend example) that can compile and run LST (though currently the inputs to the evaluation are already hard coded within the backend) using an example client as a standin to trigger the backend code to be run 
    *   Next steps
        *   Work on connecting the LST client side with the server side to enable the transfer LST inputs from the client to the backend, and to return the results back to the client

    <br>
    <b>2023 Q4</b>
    <br>

    *   Progress
        *   Successfully set up and ran an example at Purdue and at UF
        *   Produced a draft version of SONIC compatible LST producer
        *   Using the server singularity environment, currently working to compile LST code within the singularity environment (involves extracting LST code from ROOT dependence and validating the changes)
    *   Next steps
        *   Validate the version of the LST code where the ROOT dependences have been removed (and create a PR)
        *   Once the LST code is independent from ROOT and able to be compiled within the singularity env, the next step will be to interface between the server side and client side

    <br>
    <b>2023 Q3</b>
    <br>

    *   Progress
        *   Learned to run the LST workflow in order to reproduce LST plots
        *   Have gotten set up at Purdue and run their test workflow (MAOD workflow) and successfully ran the setup where the cmsRun script runs on the login node, and the cmsTriton script runs on a different node
        *   Have gotten the workflow (same one we got running at Purdue) running at UF (with cmsRun on one node without any GPUs and cmsTriton on a different node)
        *   Tested with cmsRun at Purdue and cmsTriton at UF, but hit issue with nodes not being able to talk to each other, paused this direction for now
        *   Began working to adapt the LST workflow with SONIC, starting on the "client side" i.e. reworking the producer with SONIC
    *   Next steps
        *   Plan to continue to adapt the LST workflow with SONIC
        *   Will present an overview of the project at tracker meeting Oct 30, 2023


---
