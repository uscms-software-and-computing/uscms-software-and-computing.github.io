---
permalink: /about/team.html
layout: people
title: US CMS S&C Team
---

{% include image_caption.html url="../assets/images/210113 - Org Chart.png" alt="US CMS S&C Org Chart" description="" %}

{% include wbs_list.html %}
{% assign areas = wbs_list | hash_fetch: site.data.orgs | sort_natural: "wbs_no" %}

<h1>Full Team</h1><br>

<div class="container-fluid">
  <div class="row">
    {% for area in areas %}
      {% assign members = area.personnel | hash_fetch: site.data.people
                                         | where_exp:"item", "item.active and item.hidden != true" %}

      {% for person in members %}
        {% include standard_person_card.md person=person %}
      {% endfor %}
    {% endfor %}
  </div>
</div>
