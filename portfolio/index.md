---
title: Portfolio
nav:
  order: 1
  tooltip: Our past, present, and future projects
---

# Portfolio

{% include section.html %}

## Collaborators

Some of the individual groups we work with:
{:.center}

{% 
  include gallery.html
  link1="https://greenelab.com/"
  image1="images/greene-lab.png"
  tooltip1="Greene Lab"
  link2="https://tislab.org/"
  image2="images/tis-lab.png"
  tooltip2="TIS Lab"
  link3="https://www.waysciencelab.com/"
  image3="images/way-lab.png"
  tooltip3="Way Lab"
%}

{% include section.html %}

Filter:
{:.center}
{%
  include tags.html
  tags="website,frontend,backend,devops,UI,API"
%}
{% include search-info.html %}

## Projects

{%
  include list.html
  data="portfolio"
  component="card"
%}
