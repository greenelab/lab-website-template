---
title: Team
---

# <i class="fas fa-users"></i>Team

## Team List

A _team list_ component, to sort and group all of the members on your team automatically.
Can be used on any page, but assumes its content from `/_members`.
Uses the _portrait_ component.

All team members, sorted alphabetically by file name:

{% capture html %}
{% include team-list.html %}
{% endcapture %}

{% include centerer.html html=html %}

Team members filtered and sorted by role:

{% capture html %}
{% include team-list.html role="pi" %}
{% include team-list.html role="phd" %}
{% include team-list.html role="programmer" %}
{% endcapture %}

{% include centerer.html html=html %}

Team members filtered and sorted by group:

{% capture html %}
{% include team-list.html group="current" %}
{% include team-list.html group="" %}
{% include team-list.html group="alum" %}
{% endcapture %}

{% include centerer.html html=html %}

Team members in a specific order:

{% capture html %}
{% include team-list.html order="team-order" %}
{% endcapture %}

{% include centerer.html html=html %}
