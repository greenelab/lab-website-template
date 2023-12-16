---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

maybe or maybenot quick words about the members

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include section.html background="images/background.jpg" dark=true %}

I donno why but some other text might be needed here! maybe picture of alumni!!!

{% include section.html %}

{% capture content %}

{% include figure.html image="images/TeamE1.jpg" %}
{% include figure.html image="images/TeamE2.jpg" %}
{% include figure.html image="images/TeamE3.jpg" %}
{% include figure.html image="images/TeamE2.jpg" %}
{% include figure.html image="images/TeamE1.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
