---
permalink: /wbs4-facilities.html
layout: wbs-area
wbs_no: 4
title: HL-LHC R&D
short_title: HL-LHC R&D
pagetype: wbs-area
---

## Overview

The HL-LHC area coordinates the centralized R&D effort for tackling the challenges in computing, data, and analysis during the HL-LHC era.  We see the HL-LHC challenges as the following:
- Reduce the resources required (such as CPU and disk) by the HL-LHC physics program to levels seen as supportable.
- Enable analysis of much larger datasets as existing tools are not seen to scale up with the event count.
- Grow our pool of resources by more efficiently using owned resources, leveraging new resource types (accelerators), and using new resources such as HPC centers.

This R&D area is organized into three sub-areas:

- *Analysis systems*: developing new facilities and approaches for analysis during the HL-LHC era.
- *Production infrastructure research*: evolving the existing grid infrastructure and systems to meet the challenges of HL-LHC.
- *Physics algorithms and tools*: provide infrastructure and software to address the issues related to code performance in order to reduce computational needs for HL-LHC.

The area consists of software professionals and postdocs working on targeted year-long projects; there are significant collaborations with other projects and entities such as [IRIS-HEP](https://iris-hep.org), [Open Science Grid](www.opensciencegrid.org), [HEP-CCE](https://hepcce.org/), [ESNet](http://es.net/), and [SLATE](https://slateci.io/).

## Project Organization

The detailed area organization is:
- *Analysis Systems*: Develop tools and analysis systems for HEP that enable both innovation and the adoption of “industry standard” analytic techniques. Enable rapid interactive analysis of PB datasets.
   - *Tools for Advanced Analysis* Provide interfaces and infrastructure to adapt HEP data in order to enable rapid analysis; projects include investments into columnar data such as [Awkward Array](https://github.com/scikit-hep/awkward-1.0#readme).
   - *Analysis Facilities*.  Prototype and put into production the infrastructure required for a multi-user analysis facility exploiting the newly-developed analysis tools.
- *Computing and Software Infrastructure*: Explore, evaluate, prototype, and build the infrastructure necessary for HL-LHC computing.
   - *Storage*: Evaluate storage technologies for performance; update data formats and data-handling for efficient use and rapid transfer.
   - *Provisioning of Compute Services*: Simplify and automate the deployment of computing services through tools like Kubernetes.
   - *HPC Integration & Development*: Develop workflow infrastructure to allow efficient use of LCF HPCs.
   - *Workflow Development*: Research/prototype alternatives to bespoke CMS workflow management.
   - *AI/ML Infrastructure*: Evaluate and construct methods of integrating AI training workflows for rapid development.
- *Physics Algorithms*: Provide infrastructure and software to address the issues related to code performance in order to reduce computational needs for HL-LHC.
   - *Adaptation for heterogeneous architectures*: Convert or extend existing algorithms to run on accelerators.
   - *Algorithm Development*: R&D into new algorithms, including those based on Machine Learning, that promise dramatic increases in processing speed.

