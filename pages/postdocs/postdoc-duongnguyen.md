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
    
    * Continued works on the input data deletion in the tape data carousel data processing
      * Implemented the new codes to separate the input data deletion CherryPy service from other workqueue services. This prevents interruption of those services in case there are crashes in the execution of input data deletion  
    * Completed implementation of codes to reduce the disk usage of output data in production workflow
    * Study of the tape archive metadata continued:
      * The results of data collocation of FNAL tape analysis are presented at CHEP which show that the tape recalls often request data that are poorly collocated. This reduced the performance of the data staging to disk 
      * Analyze the collocation hints using Rucio tape recall rules in CRAB user analysis jobs and tape recall data reported in FNAL dCache disk buffer: first schema was derived using physic process name as collocation hint
    * Planned to perform studies to quantify the performance of recall under different data collocation settings. The FNAL tape operation team will provide the layout of data on tapes and synthetic datasets are fabricated in Rucio to simulate different levels of data collocation. The tape recall metrics are measured to quantify the performance corresponding to these data collocation levels.

    <br>

---
