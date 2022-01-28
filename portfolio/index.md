---
title: Portfolio
nav:
  order: 1
  tooltip: Our past, present, and future projects
---

# Portfolio

Our past, present, and future projects with our various clients.
{:.center}

{% include link.html link="https://greenelab.com/" text="Greene Lab" icon="fas fa-flask" %}
{% include link.html link="https://tislab.org/" text="TIS Lab" icon="fas fa-flask" %}
{% include link.html link="https://medschool.cuanschutz.edu/ai" text="The Center itself" icon="fas fa-flask" %}
{:.center}

**Filter by type:**
{:.center}
{%
  include tags.html
  tags="website, frontend, backend, devops, UI"
%}
{% include search-info.html %}

{% include section.html %}

## Current Projects

{%
  include list.html
  data="portfolio"
  component="card"
  filters="group: "
%}

{% include section.html %}

## Past Projects

{%
  include list.html
  data="portfolio"
  component="card"
  filters="group: past"
%}
