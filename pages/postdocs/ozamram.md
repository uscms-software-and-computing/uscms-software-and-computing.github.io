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
  <br>
  <b>2024 Q2 </b>
  <br>

  *   Progress
      *   Completed full data pipeline for training on CMS HGCal simulation.
      *   Trained first models to reproduce single photon HGCalEE showers in a limited energy range at fixed rapidity and angle. Captured basic structure of the shower but modeling of some features can be improved
      *   Developed first version of the model which uses existing fastsim as an input to reduce number of diffusion steps needed for high quality generation by using conditional distillation technique
  *   Next steps
      *   Generate a larger set of CMS HGCal simulations covering a larger phase space. Use these simulations to train the model at a larger scale.
      *   Improve the modeling of some HGCal shower features (energy per layer, radial spread of the shower, occupancy) 
      *   Develop testing suite to quantitatively validate performance of trained model
      *   Further optimize usage of existing fast sim input to improve speedup gains


  <br>
  <b>2024 Q1 </b>
  <br>

  *   Progress
      *   Began development of pipeline for training on CMS HGCal simulation, including handling complicated geometry.
      *   Began development of hybrid model which incorporates existing fast simulation to reduce time needed for generation of high quality showers
  *   Next steps
      *   Complete HGCal simulation pipeline, train first models.
      *   Complete developement of hybrid model. Test speed up gains from its usage


  <b>2023 and prior </b>

  *   Progress
      *   Have successfully developed denoising diffusion model for calorimeter simulation that achieves state of the art results on public datasets.
      *   Paper published in <a href="https://doi.org/10.1103/PhysRevD.108.072014"> Phys.Rev.D 108 (2023) </a>
  *   Next steps
      *   Next steps are to explore different methods of improving the generation speed, including diffusing from existing fast simulation rather than pure noise. 
      *   Following this, we will apply the model to simulate the current CMS calorimeter and eventually the HGCal design. 
---
