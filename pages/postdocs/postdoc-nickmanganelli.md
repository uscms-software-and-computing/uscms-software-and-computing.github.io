---
permalink: /postdocs/postdoc-nickmanganelli.html
layout: postdoc
pagetype: postdoc
active: true
title: Post-doctoral researcher
postdoc-name: Nick Manganelli
shortname: 
project_title: Advancing Machine Learning Inference with Columnar Analysis at CMS Analysis Facilities
dates:
  start: 2023-01-01
  end: 2025-01-01
photo: /assets/images/team/Nick-Manganelli.jpg
institution: University of Colorado Boulder
website:
e-mail: nmangane@cern.ch
mentors:
  - Keith Ulmer (University of Colorado Boulder)
project_goal: >
  Develop and benchmark the usage of rapid Machine Learning Inference-as-a-Service together with columnar analysis in the Fermilab Elastic Analysis Facility for the next generation HL-LHC computing model.
project_summary: >
  Benchmarks have been completed of the EAF's Scalable Nvidia Triton System. Simple scaling tests show that the simple comparison of serial requests for inference of a two-class ParticleNet model attain speedups of approximately 50x using Triton on a 2.20GB MIG slice of an A100 GPU at the EAF, relative to a typical worker node in the LPC interactive nodes. While benchmarking, we discovered inefficiencies in the scaling of the Triton system, which resulted in too many servers spinning up for the number of requests being received. After tuning, we attained linear scaling of net inference rate with Triton server instances, indicating near-ideal scale-up parameters for the models under test. Tests of the basic networking characteristics demonstrate that the kinds of models oftend deployed in analysis now, such as BDTs, can easily see slowdown using the Triton server infrastructure, due to the overhead of transmitting the inputs and outputs over the network. More compute-heavy models, such as ResNet50 and the aforementioned ParticleNet model, however, see notable and significant (respectively) gain due to the balance of computational (inference) time and network transmission time. Another result from our research is that the current default Triton behaviour with regards to simultaneously handling multiple models is not ideal. When multiple models are receiving inference requests on a given Triton server instance, each one builds and fills a request queue in main RAM. Due to contention for resources, whether it's in main RAM, over the PCIe Bus, for the GPU RAM, or compute, we see that inference efficiency can drop significantly, by approximately a factor of 5. This indicates that a better behaviour to orchestrate, when multiple models are being requested and when multiple servers are available, is to concentrate model requests of the same type (and potentially the same computation engine, such as torch or tensorflow) in the same server. Such capability is currently reserved for Nvidia AI Enterprise customers, however. Regardless, Triton proves to be a highly-efficienty ML Inference service, which is easy to use at the LPC/EAF, and can support requests from hundreds of worker nodes in parallel. The usage of this service by LPC analysts should be highly encouraged, in order to preserve other GPU usage for other tasks, such as model training.
proposal: /assets/pdfs/MLInfColumnar.pdf
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
---
