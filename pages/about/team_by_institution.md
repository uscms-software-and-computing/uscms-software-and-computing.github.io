---
permalink: /about/team_by_institution.html
layout: people
title: US CMS S&C Team
---

{% include org_chart.html %}

{% include institution_list.html %}
{% assign univs = institution_list | hash_fetch: site.data.institutions | sort_natural: "name" %}
{% assign former_members = site.data.people | values
                                    | where_exp:"item", "item.active == false and item.hidden != true"
                                    | last_name_sort: "name" %}

<h1>Full Team</h1><br>

<div class="container-fluid">
  <div class="row">
    {% for univ in univs %}
      {% assign members = univ.personnel | hash_fetch: site.data.people
                                         | where_exp:"item", "item.active and item.hidden != true"
                                         | last_name_sort: "name" %}


      {% for person in members %}
        {% include standard_person_card.md person=person %}
      {% endfor %}
    {% endfor %}
  </div>
</div>

<br>
<h1>Former Members</h1><br>
<div class="container-fluid">
<div class="row">
{% for former_person in former_members %}
    {% include standard_person_card.md person=former_person %}
{% endfor %}
</div>
</div> 
