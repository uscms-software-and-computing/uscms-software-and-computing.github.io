---
permalink: /interns.html
layout: default
title: US CMS S&C Research Interns
---

# U.S. CMS Software & Computing Interns


The Software and Computing Research Initiative provides funding for undergraduate students in various research areas.

{% assign interns = site.pages | where: "pagetype", "intern"
                               | last_name_sort: "intern-name"
                               | reverse
                               | iris_hep_fellow_sort
                               | reverse %}
{% assign active-interns = interns | select: "active" %}
{% assign inactive-interns = interns | reject: "active" %}


# Current Interns

<div class="container-fluid">
  <div class="row">
    {% for person in active-interns %}
      <div class="card" style="width: 14rem;">
         <img class="card-img-top" src="{{person.photo}}" alt="Card image cap">
         <div class="card-body d-flex flex-column">
           <div class="card-text">
              <b><a href="{{person.permalink}}">{{person.intern-name}}</a></b><br>
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

# Former Interns

<div class="container-fluid">
  <div class="row">
    {% for person in inactive-intern %}
      <div class="card" style="width: 14rem;">
         <img class="card-img-top" src="{{person.photo}}" alt="Card image cap">
         <div class="card-body d-flex flex-column">
           <div class="card-text">
              <b><a href="{{person.permalink}}">{{person.intern-name}}</a></b><br>
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
