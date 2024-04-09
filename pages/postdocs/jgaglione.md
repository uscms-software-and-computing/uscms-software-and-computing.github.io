---
layout: postdoc
pagetype: postdoc
shortname: jgaglione
permalink: /postdocs/jgaglione.html
postdoc-name: Jethro Gaglione
title: Post-doctoral researcher
active: True
dates:
  start: 2023-10-01
  end: 2024-09-30
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
current_status: >
  The last quarter we have incorporated and finalized testing on submission of jobs to the cluster via an mlflow-slurm interface that allows users to take advantage of cluster capabilities via MLflow projects. These nicely package the intended training project along with package and system requirements for easy reproducibility without having to explicitly learn Slurm scheduler directives and scripting. Work is ongoing to make a REST-based MLflow interface, which will allow CMS users without ACCRE accounts to submit training workflows remotely. We have also begun investigating the incorporating the use of Optuna as a suggested framework for hyperparameter optimization. This can work seamlessly with MLFlow and Slurm, and takes advantage of Bayesian optimization and pruning to efficiently run HPO.

---
