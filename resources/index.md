---
title: Resources
---

# <i class="fas fa-tools"></i>Resources

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