---
title: Team
nav:
  order: 5
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Our Team


{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)(?!alum$)(?!ment$)" %}

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Mentoring Students

{% include list.html data="members" component="portrait" filters="role: ment" %}

{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Alumni

{% include list.html data="members" component="portrait" filters="role: alum" %}
