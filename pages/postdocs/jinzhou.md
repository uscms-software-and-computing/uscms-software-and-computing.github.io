---
permalink: /postdocs/jinzhou.html
layout: postdoc
pagetype: postdoc
shortname: jinzhou
postdoc-name: Jin Zhou
title: PhD Student
active: False
dates:
  start: 2024-08-15
  end: 2025-09-15
photo: /assets/images/team/Jin_Zhou.png
institution: University of Notre Dame
e-mail: jzhou24@nd.edu
project_title: Scalable Data Analysis Applications for High Energy Physics
project_goal: >
  CMS analysis workflows that run on opportunistic clusters (e.g., HTCondor) often use node-local storage for intermediate data. At scale, worker failures and disk pressure make these runs unreliable. This project aimed to make such workflows manageable in practice—not to remove the trade-offs, but to control storage growth and recovery so that large campaigns finish predictably. We worked in the Coffea/Dask-on-TaskVine stack and developed SciWIND: mechanisms for storage minimization, efficient recovery, and resilience tuning. The goal was to reduce failed runs and turnaround time for HL-LHC-era analyses.

mentors:
  - Douglas Thain (Cooperative Computing Lab, University of Notre Dame)
  - Kevin Lannon (Physics department, University of Notre Dame)


presentations:
  - title: "Improving the Scalability and Reliability of CMS Data Analysis Workflows in Python"
    date: "May 25, 2025"
    url: https://docs.google.com/presentation/d/1N6ZYhrThoTdHjhl35eenNdW-0hMPX89Yy3cOQiM3FSg/edit?usp=sharing
    meeting: "HEP Weekly Meeting"
    meetingurl: null
  - title: "Effectively Exploiting Node-Local Storage for Data-Intensive Scientific Workflows"
    date: "May 8, 2025"
    url: https://docs.google.com/presentation/d/1pU2AKSimx8v5k0S4Ba28axxYclB_dXP63ZxRcSo-fP0/edit?usp=sharing
    meeting: "12th Greater Chicago Area Systems Research Workshop (GCASR)"
    meetingurl: https://gcasr.org/2025/
  - title: "Effectively Exploiting Node-Local Storage for Data-Intensive Scientific Workflows"
    date: "Feb 27, 2025"
    url: https://docs.google.com/presentation/d/1pU2AKSimx8v5k0S4Ba28axxYclB_dXP63ZxRcSo-fP0/edit?usp=sharing
    meeting: "17th Annual CSE Poster Presentation"
    meetingurl: null

current_status: >
  <br>
  <b>2025 Q4 </b>
  <br>

  *   Paper and final results
      *   Paper "Effectively Exploiting Node-Local Storage For Data-Intensive Scientific Workflows" accepted at IPDPS 2026 after revised submission and expanded evidence (following rejections at IPDPS 2025 and SC'25).
      *   Consolidated SciWIND framework (NLS minimization, efficient recovery, resilience reinforcement). Validated on TopEFT, RSTriPhoton, and DV5 under repeated failure conditions.
      *   Final results: up to 99.0% peak-NLS reduction, 70.1% makespan reduction, 99.8% recovery-task reduction. In the DV5 hero run, recovery tasks dropped from 2.45M to ~197K, makespan from ~37.9K s to ~10.9K s, total NLS footprint from ~8.1 TB to ~428 GB.
      *   Lightweight hybrid settings (e.g., PD2+RC2+CP10%) were the most reliable operating point in repeated runs. Heavier settings sometimes improved one axis but added noticeable pruning or metadata overhead.
  *   Lessons and recommendations
      *   Failure handling has to be treated as a normal execution path, not an exceptional case. Queue and storage traces during runtime are as important as final summary numbers.
      *   Keep figure-driven evaluation as standard practice: architecture, storage traces, concurrency traces, and full trade-off tables should be reported together.
  *   Next steps
      *   Build adaptive online tuning for PD/RC/CP based on observed DAG shape and failure patterns.
      *   Extend policy interfaces so similar mechanisms can be adopted by other workflow engines. Continue scaling studies on broader CMS workflows to validate transferability beyond the current three benchmarks.

  <br>
  <b>2025 Q3 </b>
  <br>

  *   After SC'25 rejection (submission was in Q2)
      *   Continued figure-driven evaluation: storage trajectories per worker, task concurrency dynamics (waiting vs executing), full trade-off tables for PD, RC, CP and hybrid policies across TopEFT, RSTriPhoton, and DV5.
      *   Several early policy variants looked good in aggregate metrics but still produced long scheduler stalls mid-run. Queue separation plus prioritized recovery was the first version that consistently removed those stalls.
  *   TaskVine runtime and tooling
      *   Significant runtime fixes: queue behavior under mixed runnable and non-runnable tasks, cache-state races, and transfer-path issues that only surfaced under heavy worker-to-worker traffic. Some failures looked like scheduler policy problems at first but were actually runtime bugs. Fixing those changed stability more than any single tuning knob.
      *   Expanded report toolchain so large logs are parsed once and reused for repeated analysis and plotting. That changed iteration speed a lot when runs were long and log volumes were huge.
  *   Next steps
      *   Improve scheduling efficiency by better handling pending and ready tasks—an issue that has caused severe slowdowns on unreliable clusters.
      *   Finalize stable Conda release for TaskVine so all users have a reliable build.

  <br>
  <b>2025 Q2 </b>
  <br>

  *   Paper and resilience mechanisms
      *   Paper "Effectively Exploiting Node-Local Storage For Data-Intensive Scientific Workflows" submitted to SC'25.
      *   Implemented checkpointing and replication strategies in TaskVine. Both significantly improve workflow performance on unreliable clusters. Parameter sweeps over Prune Depth (PD), Replication Count (RC), and Checkpoint Percentage (CP), plus hybrid settings (e.g., PD2+RC2+CP10%), used to evaluate practical operating points.
  *   NLS usage and storage control
      *   The shift from baseline to load shifting, then pruning, then LIF scheduling is clear in per-worker storage trajectories: peaks drop and worst-worker imbalance narrows. In practice, aggressive NLS usage is feasible only when cleanup and scheduling are coupled. Running either piece alone was usually not enough.
  *   TaskVine scale and tooling
      *   Resolved fundamental issues and inefficiencies in TaskVine. The scheduler now handles very large workflows efficiently. Our most recent success was completing an 8-million-task workflow in 20 hours.
      *   Developing a web-based visualization tool for TaskVine logs, optimized for fast log parsing, CSV generation, and displaying key statistics. Available on [GitHub](https://github.com/cooperative-computing-lab/taskvine-report-tool).
  *   Next steps
      *   Discussed with team members how to improve scheduling efficiency by better handling pending and ready tasks—an issue that has caused severe slowdowns on unreliable clusters and remained unresolved for over half a year.
      *   Finalize recent fixes and improvements in TaskVine and aim for a stable Conda release by the end of June so all users can rely on it.
      *   Study the implications and challenges when scheduling massive workflows with millions of tasks.

  <br>
  <b>2025 Q1 </b>
  <br>

  *   NLS minimization and recovery
      *   Developed the large-input first (LIF) algorithm and the pruning algorithm, which effectively reduce storage consumption by over 90% while running hundreds of thousands of tasks.
      *   Enhanced resource allocation and temp file replication on the task scheduler side. Work moved from ad hoc tuning toward a repeatable engineering loop.
      *   Established configuration names for experiments: No SciWIND (baseline), SciWIND-Min (lightweight reference), SciWIND-Core (reference for resilience analysis with PD=1, RC=1, CP=0%), and PD/RC/CP sweeps and hybrid settings for practical operating points.
  *   Paper and next submission
      *   Submitted paper to IPDPS 2025 though it was rejected. Plan to revise and submit to SC'25.
  *   Next steps
      *   Sketch a revised paper about effectively using limited storage to accomplish enormous computations, incorporating feedback from IPDPS 2025.
      *   Develop an algorithm that divides long-running tasks in DV5 into smaller ones to reduce rerun overhead on worker evictions while balancing the latency of scheduling many small tasks. Develop checkpointing of remote temp files on time to reduce the risk of losing critical files.

  <br>
  <b>2024 Q4 </b>
  <br>

  *   Project start and operating model
      *   Project start (August 2024). Set up operating model with TaskVine manager/scheduler, HTCondor workers, node-local storage (NLS), and shared parallel file system (PFS).
      *   Experiments run with TaskVine on HTCondor. Chose three workloads—TopEFT, RSTriPhoton, and DV5—as benchmarks with different depth, intermediate volume, and failure sensitivity so that a setting that looks good on one can fail on another.
  *   Experimental setup and metrics
      *   Injected worker losses in a controlled way so that comparisons were interpretable. Decided to track four metrics throughout: recovery task count, makespan, storage peak, and pruning overhead. Using only makespan repeatedly hid important regressions during development, so all four are needed.
      *   Began baseline studies and failure-injection experiments to pin down baseline behavior and naming (e.g., No SciWIND / Initial) before adding new mechanisms.
  *   Next steps
      *   Implement first SciWIND mechanisms: NLS minimization and recovery scheduling. Move from ad hoc tuning to a repeatable engineering loop.

---
