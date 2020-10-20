---
title: Team
---

# <i class="fas fa-users"></i>Team

All team members, sorted alphabetically by file name:

{% capture html %}
{% include member-list.html %}
{% endcapture %}

{% include centerer.html html=html %}

Team members filtered and sorted by role:

{% capture html %}
{% include member-list.html role="pi" %}
{% include member-list.html role="phd" %}
{% include member-list.html role="programmer" %}
{% endcapture %}

{% include centerer.html html=html %}

Team members filtered and sorted by group:

{% capture html %}
{% include member-list.html group="current" %}
{% include member-list.html group="" %}
{% include member-list.html group="alum" %}
{% endcapture %}

{% include centerer.html html=html %}

Team members in a specific order:

{% capture html %}
{% include member-list.html order="team-order" %}
{% endcapture %}

{% include centerer.html html=html %}