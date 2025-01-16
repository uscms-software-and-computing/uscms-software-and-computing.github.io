---
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
  - Accelerate the execution of CMS analysis applications.
  - Reduce storage consumption to enable more ambitious computations.
  - Enhance fault tolerance by breaking long tasks into smaller ones and implementing effective checkpointing strategies.

mentors:
  - Douglas Thain (Cooperative Computing Lab, University of Notre Dame)
  - Kevin Lannon (Physics department, University of Notre Dame)


current_status: >
  <br>
  <b>2025 Q1 </b>
  <br>

  *   Progress
      *   
      *   Developed the large-input first (LIF) algorithm and the pruning algorithm which effectively reduce the storage consumption for over 90% while running hundreds of thousands of tasks.
      *   Enhanced the resource allocation and temp file replication on the task scheduler side.
      *   Attempted to submit a paper to IPDPS 2025 though was rejected.
  *   Next steps
      *   Sketch a paper aobut effectively using limited storage to accomplish enormous computations.
      *   Develop an algorithm that divides long running tasks in DV5 into smaller ones, which reduces the overhead of rerunning tasks on worker evictions but increases the latency of scheduling a large number of small tasks, so the next plan would be trying to strike a balance between task scheduling and fault tolerance.
      *   Develop an algorithm that checkpoints remote temp files on time to reduce the risk of losign critical files.

---
