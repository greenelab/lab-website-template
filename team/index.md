---
title: Team
nav:
  order: 4
  tooltip: Members of our lab
seo_title: "Team | p4MARS Lab, TU Delft Aerospace Engineering"
seo_description: "Meet the p4MARS Lab at TU Delft: faculty, postdocs, PhD candidates, research assistants, visiting researchers and alumni working on robot perception."
---

{% include section.html size="full" %}

{% include page-hero.html title="Team" icon="fa-solid fa-users" %}

{% include section.html %}

<style>
  /* compact section headings on the Team page */
  main h2 { font-size: 1.25rem; margin: 30px 0 6px; }
</style>

{% include section.html %}

## Faculty

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

## Postdoctoral researchers

{% include list.html data="members" component="portrait" filter="role == 'postdoc' and group != 'alum' and group != 'incoming'" %}

## PhD candidates

{% include list.html data="members" component="portrait" filter="role == 'phd' and group != 'alum' and group != 'incoming'" %}

## Research assistants

{% include list.html data="members" component="portrait" filter="role == 'research-assistant' and group != 'alum' and group != 'incoming'" %}

## Visiting researchers

{% include list.html data="members" component="portrait" filter="role == 'visiting' and group != 'alum' and group != 'incoming'" %}

<!-- Uncomment once there are current MSc students (set `role: master` in _members/*.md)
## Master students

{% include list.html data="members" component="portrait" filter="role == 'master' and group != 'alum' and group != 'incoming'" %}
-->

{% include section.html %}

## Alumni

{% include list.html data="members" component="portrait" filter="group == 'alum'" style="small" %}
