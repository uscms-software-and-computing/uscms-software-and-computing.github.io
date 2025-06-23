---
permalink: /postdocs/jinzhou.html
layout: postdoc
pagetype: postdoc
shortname: jinzhou
postdoc-name: Jin Zhou
title: PhD Student
active: True
dates:
  start: 2024-08-15
  end: 2025-09-15
photo: /assets/images/team/Jin_Zhou.png
institution: University of Notre Dame
e-mail: jzhou24@nd.edu
project_title: Scalable Data Analysis Applications for High Energy Physics
project_goal: >
  - Accelerate CMS analysis workflows, focusing on those using Coffea, Dask, and TaskVine.
  - Reduce storage usage in data-intensive workflows to support more ambitious computations.
  - Improve fault tolerance on unreliable clusters through replication and checkpointing.
  - Explore graph optimization strategies to minimize makespan using real-time information.

mentors:
  - Douglas Thain (Cooperative Computing Lab, University of Notre Dame)
  - Kevin Lannon (Physics department, University of Notre Dame)

current_status: >
  <br>
  <b>2025 Q1 </b>
  <br>

  *   Progress
      *   
      *   Developed the large-input first (LIF) algorithm and the pruning algorithm which effectively reduce the storage consumption by over 90% while running hundreds of thousands of tasks.
      *   Enhanced the resource allocation and temp file replication on the task scheduler side.
      *   Attempted to submit a paper to IPDPS 2025 though was rejected.
  *   Next steps
      *   Sketch a paper about effectively using limited storage to accomplish enormous computations.
      *   Develop an algorithm that divides long running tasks in DV5 into smaller ones, which reduces the overhead of rerunning tasks on worker evictions but increases the latency of scheduling a large number of small tasks, so the next plan would be trying to strike a balance between task scheduling and fault tolerance.
      *   Develop an algorithm that checkpoints remote temp files on time to reduce the risk of losing critical files.

  <br>
  <b>2025 Q2 </b>
  <br>

  *   Progress
      *   Paper “Effectively Exploiting Node-Local Storage For Data-Intensive Scientific Workflows” submitted to SC’ 25.
      *   Implemented checkpointing and replication strategies in TaskVine, both significantly improve workflow performance on unreliable clusters.
      *   Resolved fundamental issues and inefficiencies in TaskVine; the scheduler now handles very large workflows efficiently. Our most recent success was that we completed an 8-million-task workflow in 20 hours.
      *   Developing a web-based visualization tool for TaskVine logs, optimized for fast log parsing, CSV generation, and displaying key statistics. Available on [GitHub](https://github.com/cooperative-computing-lab/taskvine-report-tool).
  *   Next steps
      *   Discussed with team members how to improve scheduling efficiency by better handling pending and ready tasks—an issue that has caused severe slowdowns on unreliable clusters and remained unresolved for over half a year.
      *   Finalizing our recent fixes and improvements in TaskVine, make sure we have a stable Conda release by the end of June and all our users are happy to use it.
      *   Study the implications and challenges when scheduling massive workflows with millions of tasks.

---
