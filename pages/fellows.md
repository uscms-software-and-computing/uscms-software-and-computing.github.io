---
permalink: /fellows.html
layout: default
title: US CMS S&C Research Fellows
---

# U.S. CMS Software & Computing Fellows


The Software and Computing Research Initiative provides funding for undergraduate students in various research areas.

{% assign fellows = site.pages | where: "pagetype", "fellow"
                               | last_name_sort: "fellow-name"
                               | reverse
                               | iris_hep_fellow_sort
                               | reverse %}
{% assign active-postdocs = fellows | select: "active" %}
{% assign inactive-postdocs = fellows | reject: "active" %}


# Current Fellows

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
