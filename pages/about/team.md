---
permalink: /about/team.html
layout: people
title: US CMS S&C Team
---

{% include org_chart.html %}

{% include wbs_list.html %}
{% assign areas = wbs_list | hash_fetch: site.data.orgs | sort_natural: "wbs_no" %}
{% assign former_members = site.data.people | values
                                    | where_exp:"item", "item.active == false and item.hidden != true"
                                    | last_name_sort: "name" %}

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

<br>
<h1>Former Members</h1><br>
<div class="container-fluid">
<div class="row">
{% for former_person in former_members %}
    {% include standard_person_card.md person=former_person %}
{% endfor %}
</div>
</div>
 
