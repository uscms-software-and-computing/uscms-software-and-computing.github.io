---
permalink: /about/team.html
layout: people
title: US CMS S&C Team
---

{% include image_caption.html url="../assets/images/210113 - Org Chart.png" alt="US CMS S&C Org Chart" description="" %}

{% include institution_list.html %}
{% assign univs = institution_list | hash_fetch: site.data.institutions %}

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




