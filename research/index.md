---
title: Publication
nav:
  order: 2
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}Publications

Explore our latest contributions to the forefront of video motion analysis field through our publications.

{%
  include button.html
  link="research/#published"
  text="Published Papers"
  tooltip="Published works"
%}

{%
  include button.html
  link="research/#preprints"
  text="Preprint Papers"
  tooltip="Preprint Papers"
  flip=true
%}

{% include section.html %}


## Published

{% include list.html data="citations" component="citation" style="rich" filters="status: published"%}

{% include section.html %}

## Preprints

{% include list.html data="citations" component="citation" style="rich" filters="status: preprint"%}