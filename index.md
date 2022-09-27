---
title: Home
---

{% capture text %}
We are a small group of dedicated software developers with the [Department of Biomedical Informatics](https://medschool.cuanschutz.edu/dbmi) at the [University of Colorado Anschutz](https://www.cuanschutz.edu/).

{%
  include link.html
  link="about"
  title="Who we are"
  text="Learn more about us"
  icon="fas fa-arrow-right"
  flip=true
  style="button"
%}
{:.center}
{% endcapture %}

{% 
  include feature.html
  image="images/ahsb.jpg"
  title="Who we are"
  text=text
  link="about"
%}

{% include section.html %}

{% capture text %}
We support the labs and individuals within the Department by developing high quality web applications, web servers, data visualizations, data pipelines, and much more.

{%
  include link.html
  link="portfolio"
  text="Our portfolio"
  icon="fas fa-arrow-right"
  flip=true
  style="button"
%}
{:.center}
{% endcapture %}

{% 
  include feature.html
  image="images/code.jpg"
  title="What we do"
  text=text
  link="portfolio"
  flip=true
%}
