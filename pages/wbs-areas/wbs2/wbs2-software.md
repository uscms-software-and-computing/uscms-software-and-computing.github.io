---
permalink: /wbs2-software.html
layout: wbs-area
wbs_no: 2
title: Software
short_title: Software
pagetype: wbs-area
---

## Overview
The Software group develops and supports software that enables CMS data processing.  This software is roughly divided into two categories:  *Computing Infrastructure and Services* software facilitates data processing by moving data and scheduling computational tasks to distribute data processing across the globally distributed CMS computational resources. *Framework and Applications* software provides the physics algorithms, detector simulation, and the supporting framework that processes CMS data. 

### 2.1 Computing Infrastructure and Services
* **2.1.1 DBS/DAS/CMSWeb** provide web infrastructure to support CMS data processing.
    * **DBS** is the CMS *Data Bookeeping Service* while **DAS** stands for *Data Aggregation System*.  Both pieces of software provide facilities for locating data and tracking metadata.
    * **CMSWeb** is the infrastructure facilitating the deployment of web services in support of data processing, such as DBS and DAS as well as other services.  CMSWeb is in the process of transition from a VM-based infrastructure to a Kubernetes-based approach.
* **2.1.2 Monitoring** refers to the collection of software, web services, and infrastructure to facilitate monitoring, both in real time and historical, of CMS data processing.
* **2.1.3 Rucio** software manages data transfers across the globally distributed CMS computational infrastructure.  Rucio is community-supported software used across a number of HEP experiments.  U.S. CMS is leading the transition of CMS to Rucio to achieve more powerful and flexible data management capabilities.
* **2.1.4 GlideinWMS** is the software resposible for provisioning computing resources for CMS.  It creates a *global pool* of computational resources and handles matching of computational tasks with the appropriate resources on which to execute them.
* **2.1.5 Workflow Management** software converts abstract workflows into sets of computational tasks that can be executed with the CMS global pool.  This software is responsible for coordinating and controlling the computational work of data processing as well as tracking its progress.
* **2.1.6 XRootD** software provides the capability to stream data from storage at one computational site to a processing task at a different site.  This capability increases the flexibility of the CMS distributed computational infrastructure.
* **2.1.7 HEPCloud/HPC** \[TBD, pending decision on whether to move this to WBS 4\]

### 2.2 Framework and Applications
* **2.2.1 Framework** CMSSW framework provides the ability to write reconstruction and analysis applications in a multi-threaded-capable environment with an improved efficiency. 
* **2.2.2 FWLite** known as Framework-light enables users to write analysis code in ROOT sessions with CMS data formats and libraries available.
* **2.2.3 Profiling** refers to the effort related to  profiling automation of the workflows in collaboration with the CMS Computing Modernization working group, and ensuring that CMSSW code is compliant with modern C++ standards, and can compile and run on advanced hardware with new architectures.
* **2.2.4 ROOT** CMS uses ROOT to make data objects persistent. ROOT provides all the functionalities needed to deal with big data processing, statistical analysis, visualization and storage. 
* **2.2.5 Simulation Geometry** corresponds to the detector geometry maintenance and upgrades to provide detector geometry information to the simulation and reconstruction applications of CMS. The most critical ongoing work is migration to DD4HEP for Run3.
* **2.2.6 Visualization** project involves the development and maintenance and continued support of EVE for the ROOT community at large. Additionally, a web-based model of event visualization demonstrator is in the plans.
* 2.2.7 Reconstruction
