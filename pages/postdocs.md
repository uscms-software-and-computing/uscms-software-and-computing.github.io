---
permalink: /postdocs.html
layout: default
title: US CMS S&C Research Initiative
---

# U.S. CMS Software and Computing Research Initiative


The Software and Computing Research Initiative provides partial funding for physicists working in areas where R&D are needed to meet the goals of Software and Computing for the HL-LHC. Projects span the different R&D focus areas, including advanced algorithms, analysis systems, and underlying infrastructure.  The overall goal is to make computation of all types feasible and efficient at HL-LHC scale.

{% assign postdocs = site.pages | where: "pagetype", "postdoc"
                               | last_name_sort: "postdoc-name"
                               | reverse
                               | iris_hep_fellow_sort
                               | reverse %}
{% assign active-postdocs = postdocs | select: "active" %}
{% assign inactive-postdocs = postdocs | reject: "active" %}


# Current U.S. CMS Post Doctoral Researchers

<div class="container-fluid">
  <div class="row">
    {% for person in postdocs %}
      <div class="card" style="width: 12rem;">
         <img class="card-img-top" src="{{person.photo}}" alt="Card image cap">
         <div class="card-body d-flex flex-column">
           <div class="card-text">
              <b><a href="{{person.permalink}}">{{person.postdoc-name}}</a></b><br>
              <small>{{person.institution}}</small><br>
              <small>{{person.project_title}}</small><br><br>
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
