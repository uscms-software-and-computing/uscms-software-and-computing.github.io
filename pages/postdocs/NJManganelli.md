---
permalink: /postdocs/postdoc-nickmanganelli.html
layout: postdoc
pagetype: postdoc
active: false
title: Post-doctoral researcher
postdoc-name: Nick Manganelli
shortname: 
project_title: On Demand Column Joining with ServiceX (2024) and Advancing Machine Learning Inference with Columnar Analysis at CMS Analysis Facilities (2023)
dates:
  start: 2023-01-01
  end: 2025-01-01
photo: /assets/images/team/Nick-Manganelli.jpg
institution: University of Colorado Boulder
website:
e-mail: nmangane@cern.ch
mentors:
  - Keith Ulmer (University of Colorado Boulder)
project_goal:
  Column-Joining's purpose is to prototype on-demand column-joining leveraging tools like ServiceX, distributed SQL services (such as trino), dask, and kafka to serve needs of an envisioned HL-LHC computing model, ameliorating the need for permanent storage of augmented data from CMS NanoAOD and larger data tiers.
  The Triton inference project's purpose was to develop and benchmark the usage of rapid Machine Learning Inference-as-a-Service together with columnar analysis in the Fermilab Elastic Analysis Facility for the next generation HL-LHC computing model.
current_status: >
  <br>
  <b>On Demand Column Joining with ServiceX</b>
  <br>

  *   Q1 2024 Progress Report
      *   Work with Ben Galewsky (NCSA - UIUC), developer of ServiceX, and Burt Holzman (Fermilab) has begun on this project.
      *   Ben and Burt have deployed ‘trino,’ a distributed SQL service, at Fermilabs Elastic Analysis Facility.
      *   I have set up pipelines to ingest CMS Open Data in a NanoAOD(-like) format and convert from root to parquet, run an advanced Machine Learning model (ParticleNet, a Graph Neural Net used throughout CMS for flavor tagging and other tasks), and stored these data (separately) in a server accessible by trino.
      *   Ben has tested running joins of these converted data and inference data together, on-demand, and found that O(10M) events can be zipped together by trino in less than a minute (when outputting approximately 3 dozen columns). I have tested ingesting the output joined data and running it through rudimentary analysis.
      *   Along the way, a few bugs have been found and fixed in various packages, and a few features requested
          *   <a href="https://github.com/scikit-hep/awkward/issues/3033">https://github.com/scikit-hep/awkward/issues/3033</a>
          *   <a href="https://github.com/dask-contrib/dask-awkward/issues/472">https://github.com/dask-contrib/dask-awkward/issues/472</a>
          *   <a href="https://github.com/scikit-hep/hepconvert/issues/72">https://github.com/scikit-hep/hepconvert/issues/72</a>
          *   <a href="https://github.com/scikit-hep/hepconvert/issues/73">https://github.com/scikit-hep/hepconvert/issues/73</a>
          *   <a href="https://github.com/CoffeaTeam/coffea/issues/1010">https://github.com/CoffeaTeam/coffea/issues/1010</a>
      *   The developments were presented at the IRIS-HEP March 1 Demo Days at <a href="https://indico.cern.ch/event/1367741/">https://indico.cern.ch/event/1367741/</a> (no presentation/recording; live demo)
      *   While Ben and Burt work on the ServiceX deployment at Fermilab’s Elastic Analysis Facility (which will enable the large-scale, on-demand conversion of root data to parquet, as required by trino before joining), I will work on several components necessary to create an analysis pipeline, including identifying which columns of data are needed from each set of columns to be joined, automatic creation of SQL queries to produce the desired output in a joined fashion, etc. Further benchmarking, at more and more demanding scales, is foreseen. There are many open questions, including what kind of storage cluster deployment will be needed, server resources required, whether trino should be addressed directly or indirectly (via ServiceX), and so on. These will be explored in the coming months, at the appropriate time (considering development timeline)
  *   Q2 2024 Progress Report
      *   Project is slightly ahead of milestone schedule, with some mix of objectives from later quarters already reached (detailed breakdown below with comments)
      *   Approximately 1.5 months of work (50% FTE) has been deferred to later in the year due to series of talks and trainings, including the Triton R&D Talk at USCMS and coffea tutorials at USCMS/IRIS-HEP event)
      *   Work has started on the work to chain together column-joining components from the March demonstrator into a cohesive, easy-to-use tool for end-user analysis. Several sub-components for this must be developed and have been identified, outlined separately as End-to-End Pipeline Elements
      *   Stakeholders believe the above can be accomplished end-to-end (fallback; being able to generate joined data with (super)set of necessary columns for an analysis and caching it for repeated use, as originally enivisioned for the project, should still be feasible should End-to-End not work)
      *   In parallel, larger-scale tests with more events will be done to test the scalability and robustness of trino for joining data and delivering it (promising event rates from March demonstrator; 10s of millions of events joined on the order of minutes)
      *   A move from MinIO storage to native Ceph (and potentially leveraging native Object Storage) is being considered for testing

  *   End-to-End Pipeline Elements
      *   Be able to instantiate typetracers for coffea/dask-awkward analysis using ‘two’ parallel sources (e.g. ROOT primary source and ROOT/parquet secondary source)  and push them through analysis code to generate the dask task-graphs
      *   Use the necessary_columns tooling of dask, in conjunction with above, as an input to a ServiceX query-builder to convert automatically any ROOT formatted data, and potentially leverage automatic skimming/slimming (i.e. predicate pushdown) on parquet sources
      *   Similarly, use the necessary_columns functionality as input to a joins-query builder, whose product will be sent to trino (distributed SQL service) in order to take data in parquet format and perform the actual data joins
      *   Any remaining code to ensure the output can be delivered to the user’s analysis when the task-graph is computed, ideally as dask tasks themselves

  *   Project Milestones
      *   Quarter 1
          *   Familiarization with ServiceX software, current deployments, and internal query language (func adl) - <i><b>Complete</b></i>
          *   Development of representative ServiceX code and input data for tests of column joining. - <i><b>Complete</b></i>
      *   Quarter 2
          *   Understand whether and how joining can be accomplished prior to delivery (as part of the ServiceX pipeline) - <i><b>Partially Complete</b></i>
          *   Prototype of the full chain (using manual conversions, join-queries, etc) has been demonstrated with both ordered and out-of-order joins
          *   ...and after delivery (as part of an analysis framework like coffea - <i><b>Incomplete</b></i>
          *   This may still be useful, but will be pursued after a full-chain/End-to-end approach, fully leveraging ServiceX, has been demonstrated
          *   Identify missing components for column joining, work with ServiceX, dask, coffea, and other scikit-hep experts to develop and test code. - <i><b>Partially Complete</b></i>
          *   Work has begun on the missing components to build a cohesive pipeline end-to-end, such that there will be no manual steps involved which would require expertise beyond the typical analysts’ repertoire
      *   Quarter 3
          *   Demonstrate feasibility of column joining between two aligned event trees. Representative data is preferentially CMS NanoAOD (similarly, may be from ATLAS DAOD PhysLite), in which events do not need to be re-grouped or re-ordered prior to joining (1-to-1 file and event order relationship). This is comparable to simple Friend Trees in ROOT. - <i><b>Complete</b></i>
          *   Demonstrated immediately out-of-order (but with no missing data) joins between parquet data from a full-conversion of stock NanoAOD + parquet files storing ParticleNet inference results, demonstrating a common modality of using ‘cached’ ML results instead of re-running or storing permanently in augmented NanoAOD format (with all other input variables from the ‘central’ dataset replicated)
      *   Quarter 4 - Float and Extended (Optional) Objectives
          *   Demonstrating multi-dataset combinations - <i><b>Incomplete</b></i>
          *   This will be useful for combining systematics-trees as is used in some CMS analyses and very commonly in ATLAS, and is ideally a natural extension of two-source joins already demonstrated. If multi-source joins are not feasible in the currently chosen service, a tree-reduction approach should be equivalent even if less performant, iteratively using two-source joins
          *   Non-trivial joins (i.e. Indexed Friend Trees) - <i><b>Partially Complete</b></i>
          *   Equivalent of one part of indexed joins has been demonstrated with March out-of-order demonstrator; handling unaligned (missing data) still to be shown. Tooling to do this automatically instead of manually running components still under development
          *   Non-trivial joins (... inner or outer joins) - <i><b>Incomplete</b></i>
          *   Still to be demonstrated, but no showstoppers known of with prospective tools
          *   Test combinations of disparate CMS data tiers in a deployment of ServiceX at an Analysis Facility - <i><b>Incomplete</b></i>

  *   Next Steps
       *   Prototype the first of the End-to-End Pipeline Elements, creating a join-aware typetracer to pass through dask_awkward/coffea analysis
       *   Scale up demonstrator to larger datasets, joining together more columns, and stress testing the distributed SQL infrastructure

  <br>
  <b>Advancing Machine Learning Inference with Columnar Analysis at CMS Analysis Facilities</b>
  <br>

  Paper <a href="https://doi.org/10.1007/s41781-024-00123-2">Optimizing High
  Throughput Inference on Graph Neural Networks at Shared Computing Facilities
  with the NVIDIA Triton Inference Server</a> published in Computing and
  Software for Big Science. Benchmarks have been completed of the EAF's
  Scalable Nvidia Triton System. Simple scaling tests show that the simple
  comparison of serial requests for inference of a two-class ParticleNet model
  attain speedups of approximately 50x using Triton on a 2.20GB MIG slice of an
  A100 GPU at the EAF, relative to a typical worker node in the LPC interactive
  nodes. While benchmarking, we discovered inefficiencies in the scaling of the
  Triton system, which resulted in too many servers spinning up for the number
  of requests being received. After tuning, we attained linear scaling of net
  inference rate with Triton server instances, indicating near-ideal scale-up
  parameters for the models under test. Tests of the basic networking
  characteristics demonstrate that the kinds of models oftend deployed in
  analysis now, such as BDTs, can easily see slowdown using the Triton server
  infrastructure, due to the overhead of transmitting the inputs and outputs
  over the network. More compute-heavy models, such as ResNet50 and the
  aforementioned ParticleNet model, however, see notable and significant
  (respectively) gain due to the balance of computational (inference) time and
  network transmission time. Another result from our research is that the
  current default Triton behaviour with regards to simultaneously handling
  multiple models is not ideal. When multiple models are receiving inference
  requests on a given Triton server instance, each one builds and fills a
  request queue in main RAM. Due to contention for resources, whether it's in
  main RAM, over the PCIe Bus, for the GPU RAM, or compute, we see that
  inference efficiency can drop significantly, by approximately a factor of 5.
  This indicates that a better behaviour to orchestrate, when multiple models
  are being requested and when multiple servers are available, is to
  concentrate model requests of the same type (and potentially the same
                                               computation engine, such as
                                               torch or tensorflow) in the same
  server. Such capability is currently reserved for Nvidia AI Enterprise
  customers, however. Regardless, Triton proves to be a highly-efficienty ML
  Inference service, which is easy to use at the LPC/EAF, and can support
  requests from hundreds of worker nodes in parallel. The usage of this service
  by LPC analysts should be highly encouraged, in order to preserve other GPU
  usage for other tasks, such as model training. The paper has been accepted
  for publication in CSBS and is available on the <a
  href="https://arxiv.org/abs/2312.06838">arXiv</a>

  *   Q2 2023 Progress Report
      *   We created a fork of the tests developed in the first quarter of the project, removing the reliance on CMS data and increasing the system stress to identify maximum throughput of the Elastic Analysis Facility Triton Server.
      *   We identified scaling behavior with multiple models that suggests a need for more advanced orchestration than is in the baseline software.
      *   We have submitted requests to Nvidia to gain access to beta software with features that may resolve most or all of our scaling performance (inventing the features ourselves would be a considerable investment).
      *   Claire Savard, Burt Holzman and I (with significant suggestions and review from Lindsey Grey, Kevin Pedro, Keith Ulmer, Kevin Stenson) completed and submitted a paper summarizing results of benchmarking the EAF Triton Server to NeurIPS 2023. We are expecting feedback soon, and acceptance/rejection by the end of the 3rd quarter.
  *   Q3 2023 Progress Report
      *   Our paper submission to NeurIPS 2023 received reviews which reflected a reluctance to accept the paper, mainly criticizing our choice of target journal; it was felt that others would be more appropriate for our results, which are benchmarking systems and testing interoperability rather than demonstrating novel algorithm development, for example. We withdrew the submission and are searching for a more appropriate journal.
      *   Amongst the results that went into our paper submission, we had found a notable bottleneck in usage of IaaS through Triton for multiple users (to be reported at a future R&D Meeting), resulting in some inefficiency for the system.
      *   Preliminary studies indicate we can remove this bottleneck through more intelligent model orchestration. The feature to do so existed in Nvidia as an alpha release feature, but multiple attempts to contact Nvidia and attain access were unsuccessful. The feature has recently come out of alpha, but is now exclusively available as part of an Nvidia Enterprise 4.0 service. Addressing this would lead to a desirable optimization, but in no way does it prevent us from delivering and supporting the service, which will still be the most efficient method of high-throughput ML inference for a multi-tenant Analysis Facility.
  *   Q4 2023 Progress Report
      *   The paper has been reworked and submitted to Computing and Software for Big Science and uploaded to the arXiv at <a href="https://arxiv.org/abs/2312.06838">https://arxiv.org/abs/2312.06838</a>.
      *   Several new results were added for different models, to demonstrate the scaling behavior with regard to different archetypes. Network-focused studies were added to appendices, and language was notably improved.
      *   Funding for the open-access submission was attained by our graduate student, Claire Savard (advisor Kevin Stenson).
      *   A tutorial on the usage of Nvidia Triton Inference was completed as part of a seminar at the <a href="https://indico.cern.ch/event/1299889/timetable/?view=standard_inline_minutes">COFI 2023 Winter School</a>
      *   The git repository holding the benchmark code is available at <a href="https://github.com/cgsavard/triton_multiuser_benchmarks">https://github.com/cgsavard/triton_multiuser_benchmarks</a>

  
proposal: /assets/pdfs/ColumnJoining_MLInfColumnar_Combined.pdf
presentations:
- title: "Triton Inference and Columnar Analysis"
  date: 2023-04-03
  url: https://indico.cern.ch/event/1272845/contributions/5344724/attachments/2623810/4537142/NickManganelli_HLLHCR&D_03_04_2023.pdf
  meeting: HL-LHC R&D Initiative Meeting
  meetingurl: https://indico.cern.ch/event/1272845/
  record:
  focus-area:
- title: "Basic tools and resources needed for machine learning"
  date: 2023-12-10
  url: https://github.com/nickmanganelli-sr/cofi-2023
  meeting: 2nd COFI Advanced Instrumentation and Analysis Techniques School
  meetingurl: https://indico.cern.ch/event/1299889
  record:
  focus-area:
- title: "ServiceX and column joining"
  date: 2024-03-01
  url: 
  meeting: IRIS-HEP / AGC Demo Day #4
  meetingurl: https://indico.cern.ch/event/1367741/#10-servicex-and-column-joining
  record:
  focus-area:
- title: "Benchmarking Scalable Triton Inference at Fermilab's Elastic Analysis Facility"
  date: 2024-06-18
  url: https://indico.cern.ch/event/1352950/contributions/5922016/attachments/2879607/5044412/NickManganelli_USCMS_TritonPySONIC_18_06_2024.pdf
  meeting: 2024 US CMS Annual Collaboration Meeting
  meetingurl: https://indico.cern.ch/event/1352950/
  record: https://indico.cern.ch/event/1352950/contributions/5922016/attachments/2879607/5051239/3_SW_RD.mp4
  focus-area:
---
