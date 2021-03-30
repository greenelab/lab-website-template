---
title: Resources
---

# <i class="fas fa-tools"></i>Resources

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!-- section break -->

## Featured

{% capture contents %}
{% include resource-list.html group="featured" size="large" %}
{% endcapture %}

{% include centerer.html contents=contents %}

<!-- section break -->

## More

{% capture contents %}
{% include resource-list.html group="more" size="medium" %}
{% endcapture %}

{% include centerer.html contents=contents %}

<!-- section break -->

## Legacy

{% capture contents %}
{% include resource-list.html group="legacy" size="small" %}
{% endcapture %}

{% include centerer.html contents=contents %}
