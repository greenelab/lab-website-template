---
name: Reza Sabzevari
image: images/member/r_sabzevari.jpg
role: principal-investigator
description: Associate Professor
affiliation: TU Delft | AE
aliases:
  - R. Sabzevari
  - Reza
links:
  email: R.Sabzevari@tudelft.nl
  home-page: https://www.tudelft.nl/en/staff/r.sabzevari/
  github: p4mars
  youtube: "@p4mars"
  google-scholar: FLvPYqwAAAAJ
  semantic-scholar: "2979011"
  orcid: 0000-0002-6309-5890
  pure: bba71e74-720a-4b4c-b116-3cf3678f8693
  research-gate: Reza-Sabzevari-2
  scopus: "16032197600"
  web-of-science: H-8127-2014
  linkedin: rezasabzevari
  twitter: rezasabzevari
hide_research_link: true
---

Reza is an Associate Professor of Robotics and Perception. He leads the p4MARS Lab: an interdisciplinary research group focused on Perception and AI for Manufacturing Automation, Robotics, and Space.

Before joining TU Delft, Reza was a senior scientist at Bosch Research and the Bosch Centre for Artificial Intelligence (BCAI) in Germany. He founded the x.Lab, a playground for experimenting robot perception algorithms. He contributed to the field through innovative projects and the publication of several patents.
 
He received his Ph.D. in 3D Computer Vision from the Italian Institute of Technology (IIT) and the University of Genoa in Italy in 2013. Following his doctoral studies, he spent several years as a postdoctoral researcher, affiliating himself with the Robotics and Perception Group (RPG) at the University and ETH Zurich, as well as the Technologies for Vision (TeV) group at the Fondazione Bruno Kessler in Trento, Italy.
 
Reza's research interests include geometric and semantic scene understanding, active perception, and distributed perception, with the application to advanced robotics automation and space domains.

{% include section.html %}

## Community contributions

{% for section in site.data.service %}
<div class="service-section">
  <div class="service-section-head">
    <span class="service-section-icon"><i class="icon {{ section.icon }}"></i></span>
    <h3 class="service-section-title">{{ section.title }}</h3>
  </div>
  {% if section.description %}
    <p class="service-section-text">{{ section.description }}</p>
  {% endif %}
  <div class="service-list">
    {% for item in section.items %}
      {% include service-item.html role=item.role organization=item.organization detail=item.detail period=item.period link=item.link %}
    {% endfor %}
  </div>
</div>
{% endfor %}
