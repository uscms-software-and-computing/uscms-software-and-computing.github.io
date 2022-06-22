---
permalink: /postdocs.html
layout: default
title: US CMS S&C Research Initiative
---

# U.S. CMS Software and Computing Research Initiative


The Software and Computing Research Initiative provides partial funding for physicists working in areas where R&D are needed to meet the goals of Software and Computing for the HL-LHC. Projects span the different R&D focus areas, including advanced algorithms, analysis systems, and underlying infrastructure.  The overall goal is to make computation of all types feasible and efficient at HL-LHC scale.

{% assign fellows = site.pages | where: "pagetype", "fellow"
                               | last_name_sort: "fellow-name"
                               | reverse
                               | iris_hep_fellow_sort
                               | reverse %}
{% assign active-postdocs = fellows | select: "active" %}
{% assign inactive-postdocs = fellows | reject: "active" %}


# Current U.S. CMS Post Doctoral Researchers

<div class="container-fluid">
  <div class="row">
    {% for person in fellows %}
      <div class="card" style="width: 14rem;">
         <img class="card-img-top" src="{{person.photo}}" alt="Card image cap">
         <div class="card-body d-flex flex-column">
           <div class="card-text">
              <b><a href="{{person.permalink}}">{{person.fellow-name}}</a></b><br>
              <small>{{person.institution}}</small><br><br>
              <small><b>{{person.project_title}}</b></small><br><br>
           </div>
           <div class="card-text mt-auto"><i>
             {% include postdoc_dates.html dates=person.dates %}
           </i><br></div>
         </div>
      </div>
    {% endfor %}
  </div>
  <br>
</div>
