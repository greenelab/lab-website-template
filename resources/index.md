---
title: Resources
---

# <i class="fas fa-tools"></i>Resources

## Resource List

A _resource list_ component, to sort and group all of your tools, datasets, etc.
Can be used on any page, but assumes its content from `/_data/resources.yml`.
Uses the _card_ component (large, medium, or small).

{% capture html %}
{% include resource-list.html type="featured" size="large" %}
{% endcapture %}

{% include centerer.html html=html %}

{% capture html %}
{% include resource-list.html type="other" size="medium" %}
{% endcapture %}

{% include centerer.html html=html %}

{% capture html %}
{% include resource-list.html type="legacy" size="small" %}
{% endcapture %}

{% include centerer.html html=html %}
