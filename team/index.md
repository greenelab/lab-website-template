---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

Our lab is home to passionate and collaborative researchers.
We believe that diversity is essential for achieving our research goals, and we foster an environment where all team members are treated equally, respected, and valued for their unique perspectives and experiences.

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include section.html dark=true %}

We're currently hiring for several positions, and we encourage all individuals from diverse backgrounds to apply.
**Join us** and become part of our team.

{%
  include button.html
  text="Join the lab"
  link="join"
  style="button"
%}
