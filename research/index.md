---
title: Research
nav:
  order: 1
  tooltip: Published works
---

{% include section.html size="full" %}

{% include page-hero.html title="Research" icon="fa-solid fa-microscope" %}

{% include section.html %}

{% include tags.html tags="Scene Understanding, SLAM, Scene Graph, Robotics" %}

{% include section.html %}

## Research pillars

<div class="pillars research-areas">
{% for pillar in site.data.pillars %}
  {% include research-area.html title=pillar.title icon=pillar.icon description=pillar.description items=pillar.items %}
{% endfor %}
</div>

{% include section.html %}

## Highlighted

{% include citation.html lookup="T-FunS3D" style="rich" %}
