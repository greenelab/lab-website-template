---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research

A small discription of general research theme of the lab

{% include section.html %}

## Highlights

{% capture text %}

1st subject that we're working on

{% endcapture %}

{%
  include feature.html
  image="images/Research1.jpg"
  <!-- link="research" -->
  title="1st Research"
  text="this a text for 1st research"
%}


{% capture text %}

2nd subject that we're working on

{% endcapture %}

{%
  include feature.html
  image="images/Research2.jpg"
  <!-- link="research" -->
  title="2nd Research"
  text="this a text for 2nd research"
%}

<!-- {% include citation.html lookup="One of the published works" style="rich" %}

{% include section.html %}

## All

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %} -->
