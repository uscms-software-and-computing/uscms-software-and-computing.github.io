---
permalink: /about/team_alphabetical.html
layout: people
title: Institute Team
---

{% include image_caption.html url="../assets/images/220105-Org_Chart.png" alt="US CMS S&C Org Chart" description="" %}


{% include institution_list.html %}
{% assign members = site.data.people | values
                                     | where_exp:"item", "item.active and item.hidden != true"
                                     | last_name_sort: "name" %}
{% assign former_members = site.data.people | values
                                    | where_exp:"item", "item.active == false and item.hidden != true"
                                    | last_name_sort: "name" %}


<h1>Full Team</h1><br>

<div class="container-fluid">
<div class="row">
{% for person in members %}
    {% include standard_person_card.md person=person %}
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
