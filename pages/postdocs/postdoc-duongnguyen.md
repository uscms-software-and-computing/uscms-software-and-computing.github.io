---
layout: postdoc
pagetype: postdoc
shortname: dnguyen
permalink: /postdocs/postdoc-duongnguyen.html
postdoc-name: Duong Nguyen
title: Post-doctoral researcher
active: True
dates:
  start: 2025-01-01
  end: 2027-02-28
photo: /assets/images/team/Duong_Nguyen.jpg
institution: University at Buffalo
e-mail: duongngu@buffalo.edu
project_title: Tape data quality of service and tape data carousel
proposal: https://drive.google.com/file/d/1drG8n_aeS6lSJG6cGM6ZyWGp9WPQkT5Z/view?usp=sharing
project_goal: >
    <br>
    <b>2025-2027:  </b>
    <br>
    
    This project aims to optimize tape access for various use cases, particularly in data reprocessing workflows. Typical examples include ReReco campaigns, where RAW data needs to be staged, and ReMINIAOD, which requires staging of AOD data. By analyzing current tape access patterns, the project seeks to enhance the quality of service for tape-based data access within the collaboration. Additionally, the project will prototype a production workflow using the "carousel" model, where a sliding buffer of tape data is staged to disk for processing and automatically removes it once processing is complete. The impact of this approach on CMS data production and reprocessing will be assessed, focusing on improving storage efficiency and reducing overall storage costs for the collaboration.
    
mentors:
  - Avto Kharchilava - (University at Buffalo)


presentations:

current_status: >
    <br>
    <b>2026 Q2 </b>
    <br>

      * Continued works on the input data deletion in the tape data carousel data processing
        * Implemented the new codes to separate the input data deletion CherryPy service from other workqueue services. This prevents interruption of those services in case there are crashes in the execution of input data deletion  
      * Completed implementation of codes to reduce the disk usage of output data in production workflow
      * Study of the tape archive metadata continued:
        * The results of data collocation of FNAL tape analysis are presented at CHEP which show that the tape recalls often request data that are poorly collocated. This reduced the performance of the data staging to disk 
        * Analyze the collocation hints using Rucio tape recall rules in CRAB user analysis jobs and tape recall data reported in FNAL dCache disk buffer: first schema was derived using physic process name as collocation hint
      * Planned to perform studies to quantify the performance of recall under different data collocation settings. The FNAL tape operation team will provide the layout of data on tapes and synthetic datasets are fabricated in Rucio to simulate different levels of data collocation. The tape recall metrics are measured to quantify the performance corresponding to these data collocation levels

    <br>
    <b>2026 Q1 </b>
    <br>

      * Further developed and tested the tape data carousel for continuous input-data deletion
        * Implemented and tested handling of workflows sharing the same input data
        * Tested single and multiple workflow scenarios to verify safe deletion of input data
        * Measured disk-storage reduction during workflow processing to demonstrate the benefit of the tape data carousel
        * Monitored the continuous deletion service running on the CMS Kubernetes integration cluster
      * Investigated strategies to reduce disk usage from output data in production workflows
        * Reviewed workflow management code and developed a prototype for output data deletion
        * Presented the status of the tape data carousel and output-data reduction studies at the CMS Computing Operations workshop
      * Initiated a study of CMS tape data collocation and tape archive metadata with the FNAL team
        * Analyzed FNAL CTA tape recall logs from February 2026
        * Developed metrics to quantify the read efficiency loss due to tape positioning and data collocation for tape recalls
        * Studied the relationship between tape positioning overhead and the amount of data read during each tape mount
    
    <br>
    <b>2025 Q4 </b>
    <br>

      * Deployed and tested the continuous input data deletion service in the CMS Kubernetes integration cluster
        * Verified stable operation of the service together with the Global WorkQueue services
        * Added datasets and submitted test workflows to the integration environment
        * Verified that completed data blocks are detected and the corresponding Rucio rules are automatically removed
      * Developed a simulation tool to demonstrate the potential disk storage savings from continuous input data deletion
      * Monitored the service for stability and unexpected data deletion
    
    <br>
    <b>2025 Q3</b>
    <br>

      * Focused the implementation of the tape data carousel in the WorkQueue CherryPy service running on the CMSWeb Kubernetes infrastructure
        * Integrated the implementation into WMCore and submitted a pull request
        * Discussed the implementation with the WMCore development and CMS Production and Processing teams
      * Initiated deployment attempts of the continuous data deletion service to the CMS integration testbed for validation in realistic production workflows
      * Investigated operational considerations for deploying continuous data deletion, including additional operational effort and safeguards against unintended data deletion
    
    <br>
    <b>2025 Q2</b>
    <br>

      * Completed an assessment of CMS tape performance using FTS transfer history and CMS monitoring tools
        * Developed scripts to analyze tape recall patterns and characterize recall performance over the previous year
        * Found no critical tape performance issues, but identified a significant contribution from user driven recalls compared with production workloads
      * Initiated development of the tape data carousel model for CMS production workflows
        * Explored implementations using a dedicated WMCore component or a WMCore microservice
        * Developed preliminary code for automatically removal of the Rucio rules to release the staged data after processing completion

---