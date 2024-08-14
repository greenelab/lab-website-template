---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include section.html background="images/background.jpg" dark=true %}

Welcome to our vibrant lab community where collaboration extends beyond research. 
Alongside groundbreaking publications and impactful projects, we embrace a shared 
passion for exploration and camaraderie.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/team/team-photo-1.jpg" %}
{% include figure.html image="images/team/group/group-video-1.gif" width="100%" %}
{% include figure.html image="images/team/group/group-photo-2.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
