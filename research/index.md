---
title: Research
nav:
  order: 1
  tooltip: Published works
seo_title: "Research: 3D Scene Understanding, SLAM, Digital Twins | p4MARS"
seo_description: "Spatial and agentic intelligence, actionable world models and evolving digital twins: research and publications of the p4MARS Lab at TU Delft."
---

{% include section.html size="full" %}

{% include page-hero.html title="Research" icon="fa-solid fa-microscope" %}

{% include section.html %}

{% include tags.html tags="Scene Understanding, SLAM, Scene Graph, Robotics" %}

{%
  include button.html
  link="research#selected-publications-and-patents"
  text="Publications"
  icon="fa-solid fa-scroll"
  tooltip="Jump to the publications and patents list"
  style="prominent"
%}

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

{% include section.html %}

## Selected publications and patents

For the full list of publications, visit the [Google Scholar profile](https://scholar.google.com/citations?user=FLvPYqwAAAAJ).

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" %}
