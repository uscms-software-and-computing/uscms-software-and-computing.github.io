---
layout: postdoc
pagetype: postdoc
shortname: kmohrman
permalink: /postdocs/kmohrman.html
postdoc-name: Kelci Mohrman
title: Post-doctoral researcher
project_title: Benchmarking current capabilities and exploring the acceleration of columnar processing via heterogeneous architectures (2025) and Deploying GPU algorithms through SONIC (2023)
active: True
dates:
  start: 2023-09-01
  end: 2025-08-31
photo: /assets/images/team/Kelci-Mohrman.png
institution: University of Florida
e-mail: k.mohrman@ufl.edu
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
  - title: "Benchmarking analysis workflows"
    date: "July 23, 2025"
    url: https://indico.cern.ch/event/1565053/#2-benchmarking-analysis-workfl
    meeting: CMS CAT general meeting
    meetingurl: https://indico.cern.ch/event/1565053
  - title: "Towards rapid and efficient columnar-based analyses at scale"
    date: "July 14, 2025"
    url: https://indico.cern.ch/event/1515852/timetable/?view=standard#9-towards-rapid-and-efficient
    meeting: PyHEP.dev 2025 - Python in HEP Developer's Workshop
    meetingurl: https://indico.cern.ch/event/1515852/
  - title: "Towards rapid and efficient analyses at scale"
    date: "May 21, 2025"
    url: https://indico.cern.ch/event/1499327/contributions/6510006/
    meeting: 2025 US CMS Annual Collaboration Meeting (poster session)
    meetingurl: https://indico.cern.ch/event/1499327/
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
    <b>2025 Q2 </b>
    <br>

    *   Testing the coffea202X skimming capabilities and benchmarking performance:
        *   Testing the skimming workflow (cortado) developed last quarter, now running at realistic R2+R3 scale, with unskimmed inputs from SMP-24-015 (200/fb) as the test case
        *   Encountered challenges when attempting to process datasets in parallel, working with TaskVine developers on handling this, using their new "dynamic data reduction" implementation with cortado
        *   Benchmarking wall time and Hz/core with varying numbers of CPU cores (at UF T2)
        *   Able to achieve processing of full 13 TB inputs in a few hours with a few thousand cores (at UF)
        *   Physics validation of output skim underway, debugging in progress
    *   Explore the acceleration of the columnar processing via GPU offloading:
        *   Working on implementing and testing 8 ADL Benchmark Queries on GPU
        *   Four Queries are successfully implemented and show agreement with CPU outputs
        *   Four Queries have uncovered bugs in the cuda backends, reported on the relevant repositories, with debugging is in progress
        *   Performance comparisons of the GPU implemented Queries show performance improvements (over CPU) of up to ~800x

    <br>
    <b>2025 Q1 </b>
    <br>

    *  Progress on testing the coffea202X skimming capabilities and benchmark performance:
        *   Set up a coffea 202X-based skimming workflow (cortado)
        *   Tested single file and single dataset (~4M events) runs locally and with the TaskVine scheduler, and documenting performance
        *   Working towards realistic R2+R3 scale tests: Transferred a realistic R2+R3 200/fb scale set of unskimmed samples to the UF T2 (~13.5 TB, ~12B events, ~400 datasets of data and MC, corresponding to the set used in the SMP-24-015 analysis)

    <br>
    <b>2024 Q4 </b>
    <br>

    *   Wrapped up project, prepared the project summary document, documented the code and setup
    *   Worked with SONIC team to help with the handoff of the project, helping to get another member of the team set up and successfully run the SONIC+LST workflow
    *   Transitioning into columnar R&D project (benchmark the performance of the step of end-user data analysis, and explore the acceleration of columnar processing with GPUs)
        *   Starting with the exploration of the the performance and scaling of the skimming step with coffea 202X
        *   Progress: successfully set up and ran a 202X skimmer on one file

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
