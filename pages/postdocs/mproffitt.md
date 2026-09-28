---
layout: postdoc
pagetype: postdoc
shortname: mproffitt
permalink: /postdocs/mproffitt.html
postdoc-name: Mason Proffitt
title: Post-doctoral researcher
active: true
dates:
  start: 2026-06-01
  end: 2027-05-31
photo: /assets/images/team/mproffitt.jpg
institution: Texas Tech University
e-mail: mason.proffitt@cern.ch
project_title: Streamlining inference with SONIC
project_goal: >
  This project aims to develop, test, and improve SONIC (Services for Optimized Network Inference on Coprocessors).
  SONIC provides a way to offload and batch processing of algorithms that can be processed much faster and more efficiently on heterogeneous resources beyond general-purpose CPUs (e.g., GPUs).
  This work includes facilitating the use of new models, optimization and performance benchmarking, and new server builds on AlmaLinux.


mentors:
  - Yongbin Feng (Texas Tech University)


current_status: >
    <br>
    <b>2026 Q3</b>
    <br>

    *   Isolated reconstruction step in MLPF performance tests to investigate discrepancy in producer execution time between cases with and without SONIC
        *   Determined that difference was due to how times are reported for SONIC’s asynchronous mode (difference disappears in synchronous mode)
    *   Prepared the GitHub branches needed for implementing the MLPF SONIC producer
    *   Created pull request in FastML fork of CMSSW for review
        *   Cleaned up code and factored out some common functionality between standard MLPF producer and SONIC version

    <br>
    <b>2026 Q2</b>
    <br>

    *   Followed tutorial from Yao to get acquainted with SONIC and CMSSW
    *   Tested new MLPF model with perf_analyzer and in CMSSW
        *   Testing with perf_analyzer suggested that performance could be modestly improved with concurrency greater than 1 and with multiple model instances
        *   CMSSW timing tests showed discrepancy when running with SONIC versus without, to be investigated


---
