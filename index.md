---
title: Home
---

# Your Lab Slogan...

[Lab Website Template](https://github.com/greenelab/lab-website-template) is an easy-to-use, flexible website template for [labs](https://www.greenelab.com/), with automatic citations, GitHub tag imports, pre-built components, and more.
Spend less time reinventing the wheel, and more time running your lab.

{%
  include link.html
  type="github"
  icon=""
  text="See the template on GitHub"
  link="greenelab/lab-website-template"
  style="button"
%}
{%
  include link.html
  type="docs"
  icon=""
  text="See the documentation"
  link="https://github.com/greenelab/lab-website-template/wiki"
  style="button"
%}
{:.center}

{% include section.html full=true %}

{% include banner.html image="images/UMCU_banner_cropped.jpeg" %}

{% include section.html %}

# Highlights

{% capture text %}
The emergence of antibiotic resistant bacterial infections worldwide highlights the importance of monitoring these outbreaks. We analyse and provide tools to characterize these bacteria, their mobile genetic elements and their transmission patterns.

[See what we've published &nbsp;→](research)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/research_picture.jpg"
  link="research"
  headline="Our Research"
  text=text
%}

{% capture text %}
We also release data and software to enable reproducible computational biology analyses following the FAIR (Findable, Accessible, Interoperable and Reusable) principles. Find more about our tools in the link below.

[See our tools &nbsp;→](resources)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/tools_picture.png"
  link="resources"
  headline="Our Tools"
  text=text
%}

{% capture text %}
We are a group of enthusiastic scientists with different interests and backgrounds that work in close collaboration with experimentalists and clinicians.

[Meet our team &nbsp;→](team)
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/BioIT_group_picture.png"
  link="team"
  headline="Our Team"
  text=text
%}


