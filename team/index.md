---
title: Team
nav:
  order: 3git log
---

# {% include icon.html icon="fa-solid fa-users" %} Team

At the AeroSat Vision Lab, our team is comprised of dedicated professionals and talented students who are passionate about advancing the fields of artificial intelligence and aerospace technology. Led by Dr. Trong-An Bui, our diverse team combines expertise in engineering, electronic systems, computer science, and space technology to drive innovative research and development projects.

{% include section.html %}

## Principal Investigator
{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include section.html %}

## Members
<div class="team-container">
  {% include list.html data="members" component="portrait" filters="role: master" %}
</div>

{% include section.html background="images/background.jpg" dark=true %}

The AeroSat Vision Lab is proud to collaborate with leading research institutions and industry partners worldwide. Our strategic partnerships with renowned labs and companies, enable us to combine resources and expertise to drive groundbreaking research and development. Through these collaborations, we enhance our capabilities in AI, aerospace, and satellite technologies, transforming innovative ideas into real-world applications. Together, we are committed to advancing the frontiers of aerospace research and technology.

{% include section.html %}

{% capture content %}
Will be updated soon!
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}