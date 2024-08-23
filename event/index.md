---
title: Event
nav:
  order: 4
  tooltip: Seminar, Retreat, and Activity
---

# {% include icon.html %}Event

{%
  include button.html
  link="event/#seminar"
  text="Seminar"
%}

{%
  include button.html
  link="event/#retreat"
  text="Retreat"
  flip=true
%}

{%
  include button.html
  link="event/#activity"
  text="Activity"
%}

{%
  include section.html
%}

## Seminar

| Topic         | Research group | Description        | Date       |
| ------------- | -------------- | ------------------ | ---------- |
| Topic 1       | Group A        | Description of 1   | 2023-08-23 |
| Topic 2       | Group B        | Description of 2   | 2023-08-24 |

{% include section.html %}

## Retreat

| Topic         | Research group | Description        | Date       |
| ------------- | -------------- | ------------------ | ---------- |
| Topic 1       | Group A        | Description of 1   | 2023-08-23 |
| Topic 2       | Group B        | Description of 2   | 2023-08-24 |



{% include section.html %}

## Activity

Welcome to our vibrant lab community where collaboration extends beyond research. 
Alongside groundbreaking publications and impactful projects, we embrace a shared 
passion for exploration and camaraderie.

{% capture content %}

{% include figure.html image="images/team/team-photo-1.jpg" %}
{% include figure.html image="images/team/group/group-video-1.gif" width="100%" %}
{% include figure.html image="images/team/group/group-photo-2.jpg" %}

{% include figure.html image="images/about/food-2.png" %}
{% include figure.html image="images/activity/gv-1.gif" width="100%" %}
{% include figure.html image="images/activity/gp-6.jpg" %}

{% include figure.html image="images/activity/gv-2.gif" width="100%" %}
{% include figure.html image="images/about/plant-3.png" %}
{% include figure.html image="images/activity/gp-2.jpg" %}


{% endcapture %}

{% include grid.html style="square" content=content %}