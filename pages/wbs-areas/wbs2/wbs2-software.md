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
* 2.2.1 Framework
* 2.2.2 FWLite
* 2.2.3 Profiling
* 2.2.4 ROOT
* 2.2.5 Simulation Geometry
* 2.2.6 Visualization
* 2.2.7 Reconstruction
