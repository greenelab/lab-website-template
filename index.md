---
title: Home
---

# MMB-BioIT

The MMB-BioIT Lab is a team of researchers with different backgrounds, part of the Medical Microbiology department at the UMCU (Utrecht, the Netherlands). Our efforts are dedicated to develop tools and analyze data to track local and global transmission of bacterial pathogens and to provide information on the acquisition of determinants that contribute to virulence, resistance to antibiotics or other fitness traits.

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

{% include banner.html image="images/UMCU.jpeg" %}

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
  image="images/group.png"
  link="team"
  headline="Our Team"
  text=text
%}


