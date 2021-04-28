---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

The Translational and Integrative Science Center (TISC) reimagines data to change the world.
The center supports the translation of insights from data files to implemented solutions.
From the diagnosis of rare diseases and improving food systems and nutrition, to revealing patterns of biodiversity in response to climate change, TISC embodies an interdisciplinary, distributed collaboration model of science.
In TISC, we are committed to the belief that shared, open science is the best way to solve problems and advance society.
Bringing people and their data together across fields brings new discoveries and the ability to solve real world problems.
Not only are we changing the world, we are also changing science itself.

{% include section.html %}

{% include list.html data="members" component="portrait" filters="tier: first" %}
{% include list.html data="members" component="portrait" filters="tier: second" %}
{% include list.html data="members" component="portrait" filters="tier: " %}

{% include section.html dark=true %}

Whether you are a scientist looking to step into an emerging field with your data, an organization interested in investing in this work, or if you are simply curious and would like to stay informed about how translational science will evolve, we welcome your partnership. We work with leading scientists around the world and are funded by large national grants and institutions with new discoveries emerging every day.

{%
  include link.html
  icon="fas fa-hands-helping"
  text="Join the Team"
  link="contact"
  style="button"
%}
{:.center}

{% comment %}
{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.
{:.center}

{%
  include gallery.html
  fit="false"

  image1="images/photo.jpg"
  link1="https://nasa.gov/"
  tooltip1="Cool Foundation"

  image2="images/photo.jpg"
  link2="https://nasa.gov/"
  tooltip2="Cool Institute"

  image3="images/photo.jpg"
  link3="https://nasa.gov/"
  tooltip3="Cool Initiative"

  image4="images/photo.jpg"
  link4="https://nasa.gov/"
  tooltip4="Cool Foundation"

  image5="images/photo.jpg"
  link5="https://nasa.gov/"
  tooltip5="Cool Institute"

  image6="images/photo.jpg"
  link6="https://nasa.gov/"
  tooltip6="Cool Initiative"
%}
{% endcomment %}
