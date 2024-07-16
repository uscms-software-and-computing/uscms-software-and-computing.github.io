---
layout: postdoc
pagetype: postdoc
shortname: ozamram
permalink: /postdocs/ozamram.html
postdoc-name: Oz Amram
title: Post-doctoral researcher
active: True
dates:
  start: 2022-09-12
  end: 2024-09-12
photo: /assets/images/team/Oz-Amram.jpg
institution: Fermilab
e-mail: oz.amram@cern.ch
project_title: AI Denoising to Accelerate Detector Simulation
project_goal: >
    Develop fast and accurate simulation of highly granular calorimeters using
    machine learning models.
    Use a 'denoising' approach to upscale existing physics-based fast
    simulation to achieve better quality at similar speeds.
mentors:
  - Kevin Pedro (Fermilab)

proposal: /assets/pdfs/Oz-Amram.pdf
presentations:
  - title: "Machine Learning Models for Calorimeter Simulation"
    date: 2022-11-08
    url: https://indico.cern.ch/event/1219769/contributions/5131599/attachments/2543904/4380363/LHC_RD_calorimeter_simulation_intro.pdf
    meeting: HL-LHC R&D Initiative Meeting
    meetingurl: https://indico.cern.ch/event/1219769/
    record: 
    focus-area: Simulation
  - title: "Fast and Accurate Calorimeter Simulation with Diffusion Models"
    date: 2023-05-11
    url: https://indico.jlab.org/event/459/contributions/11736/attachments/9599/14176/CHEP23_CaloDiffusion.pdf
    meeting: Computing in High Energy Physics (CHEP) 2023
    meetingurl: https://indico.jlab.org/event/459/
    record: 
    focus-area: Simulation
  - title: "Denoising Diffusion Models for High Fidelity Calorimeter Simulation"
    date: 2023-05-30
    url: https://agenda.infn.it/event/34036/contributions/200894/attachments/105911/149021/CaloChallenge_CaloDiffusion.pdf
    meeting: CaloChallenge Workshop
    meetingurl: https://agenda.infn.it/event/34036/
    record: 
    focus-area: Simulation

current_status: >
  In progress. Have successfully developed denoising diffusion model for calorimeter
  simulation that achieves state of the art results on public datasets.
  
  A paper summarizing these was published in [Phys.Rev.D](https://doi.org/10.1103/PhysRevD.108.072014). 
  
  We have since implemented further improvements to the model, which have led to improved energy response modeling and faster generation times. We also developed an alternate version of our diffusion model that was able to use existing fast simulation as an additional input, which allowed the model to achieve high quality results in fewer diffusion steps.

  We have begun working on simulations of the CMS HGCal. Using initial R&D simulation of the HGCal we are developing a pipeline to convert between the CMS SimHit format and HGCal geometry and to the data format needed by our model and back. We are also preparing a production of significantly larger samples of HGCal simulation which will test the scalability of our model to cover the entire simulation phase space. 
---
