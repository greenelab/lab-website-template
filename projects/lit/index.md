---
title: Luchtvaart in Transitie (LiT)
seo_description: "Luchtvaart in Transitie (LiT): p4MARS develops 3D modeling of manufacturing processes and automated non-destructive testing for climate-neutral aviation."
---

{% assign project = site.data.projects | where_exp: "p", "p.link == 'projects/lit'" | first %}

<p class="eyebrow"><a href="{{ 'projects' | relative_url }}">Projects</a></p>

# {% include icon.html icon="fa-solid fa-plane" %}Luchtvaart in Transitie (LiT)

{{ project.description | markdownify }}

{% include sponsors.html sponsors=project.sponsors %}

{%
  include button.html
  type="website"
  text="Luchtvaart in Transitie"
  link="https://luchtvaartintransitie.nl/en/"
  style="bare"
%}

{% include section.html %}

## Activities

{% for a in project.activities %}
{% assign anchor = a.title | slugify %}
{% include project.html id=anchor title=a.title icon=a.icon image=a.image description=a.description tags=a.tags people=a.people vacancies=a.vacancies %}
{% endfor %}
