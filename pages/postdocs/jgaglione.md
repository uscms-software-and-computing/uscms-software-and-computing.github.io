---
layout: postdoc
pagetype: postdoc
shortname: jgaglione
permalink: /postdocs/jgaglione.html
postdoc-name: Jethro Gaglione
title: Post-doctoral researcher
active: True
dates:
  start: 2024-01-01
  end: 2024-12-31
photo: /assets/images/team/Jethro-Gaglione.jpg
institution: Vanderbilt University
e-mail: jethrogaglione@gmail.com
project_title: Development of a Distributed GPU Machine Learning Training Facility at Vanderbilt's ACCRE Cluster
project_goal: >
    The objective of this project is to leverage the knowledge and hardware available within the Vanderbilt research computing center (ACCRE) to develop a prototype distributed GPU machine learning training facility. We aim to provide the efficiency boost of training on a multi-GPU platform to CMS users and beyond, while abstracting away the highly technical details necessary to do so.  
mentors: >
  - Andrew Melo - (Vanderbilt University)

proposal: /assets/pdfs/Jethro-Gaglione.pdf
presentations:
  - title: "Machine Learning Training Facility at Vanderbilt"
    date: "April 8, 2024"
    url: <https://docs.google.com/presentation/d/1mK_AvZ3sJ9DhR1ZyzQk2NGb5MFS2VvprgtLx-k-gy3o/edit#slide=id.p>
    meeting: <Production Group Meeting>
    meetingurl: <https://indico.cern.ch/event/1400420/>

  - title: "Machine Learning Training Facility at Vanderbilt - A Prototype for Efficient and Reproducible ML Training"
    date: "July 19, 2024"
    url: <https://indico.cern.ch/event/1438068/>
    meeting: <Fast ML Co-processor Meeting>
    meetingurl: <https://indico.cern.ch/event/1438068/> 

current_status: >
  <br>
  <b>2024 Q3</b>
  <br>
  This quarter, we made significant progress integrating the btag POG ML training framework b-hive into an MLflow project which can be submitted to the Machine Learning Training Facility (MLTF). This work is very close to being merged, which will make it the first production CMS ML workflow integrated with the MLTF.

Work on hardware capabilities continues to hit delays due to issues with firmwares provided by the manufacturer. Engineers were unable to remotely diagnose the issue, leading Vanderbilt to ship the hardware back for hands-on inspection. This was successful, the engineers were able to find a subtle bug at the PCI-E layer, and updated/flashed the firmware to solve it. As of this writing, the hardware is being shipped back to Vanderbilt with the assertion from the manufacturer that it is fixed. This will, of course, push back hardware-related milestones.

Vanderbilt developers have completed a first draft of the MLflow “gateway” server, which provides a REST-based job submission infrastructure (similar to CMS’ CRAB functionality). This will allow automated submission of training tasks (e.g. for CI/CD) via REST, or CLI-based job submission using a MLflow plugin which users can install into their environments. The functionality is currently basic, stubbing out the API, but has token-based authentication enabled to the point that the service can be securely accessed. The next work is to implement the missing functions so this service can be opened to alpha users in Q4.



  <br>
  <b>2024 Q2</b>
  <br>
  While in more advanced stages of implementing and testing a variety of ML frameworks for training, logging metrics, hyperparameter optimization, and the deployment and reproducibility of these (via MLflow, Optuna, etc. see last quarter update), we have begun branching out to the ML community to gauge some of their needs and make them aware of the our facility (MLTF). We presented information on MLTF to the CMS ML production group on 4/8 (https://indico.cern.ch/event/1400420/), and we are set to give a talk on July 19th at Fermilab’s Fast Machine Learning Coprocessor meeting. We have been in touch with the BTV POG developers regarding their ongoing ML training framework project, B-hive, which currently trains the DeepFlavor tagging algorithm. We are exploring how we could best incorporate this framework and enhance its features with the frameworks we currently plan to encourage use of at MLTF. We continue to implement and test uses of our current frameworks to enhance productivity and efficiency, such as system usage metric tracking via MLflow.

  <br>
  <b>2024 Q1</b>
  <br>
  The last quarter we have incorporated and finalized testing on submission of jobs to the cluster via an mlflow-slurm interface that allows users to take advantage of cluster capabilities via MLflow projects. These nicely package the intended training project along with package and system requirements for easy reproducibility without having to explicitly learn Slurm scheduler directives and scripting. Work is ongoing to make a REST-based MLflow interface, which will allow CMS users without ACCRE accounts to submit training workflows remotely. We have also begun investigating the incorporating the use of Optuna as a suggested framework for hyperparameter optimization. This can work seamlessly with MLFlow and Slurm, and takes advantage of Bayesian optimization and pruning to efficiently run HPO.

  <br>
  <b>2023 Q3</b>
  <br>
  We have chosen appropriate hardware to purchase for the PoC, but delays in FNAL procurement have made it so we can’t order yet. Gaglione will join the effort on Oct 1 (as planned), and we will work with substitute hardware in the interim.

---
