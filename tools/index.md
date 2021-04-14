---
title: Tools
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# <i class="fas fa-tools"></i>Tools

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!-- section break -->

## Featured

{% capture contents %}
{% include list.html component="card" data="tools" filters="group: featured" %}
{% endcapture %}

{% include centerer.html contents=contents %}

<!-- section break -->

## More

{% capture contents %}
{% include list.html component="card" data="tools" filters="group: more" %}
{% endcapture %}

{% include centerer.html contents=contents %}

<!-- section break -->

## Legacy

{% capture contents %}
{% include list.html component="card" data="tools" filters="group: legacy" style="small" %}
{% endcapture %}

{% include centerer.html contents=contents %}
