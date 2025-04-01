---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

We currently have a few M.Sc. and Integrated M. Tech thesis students working with us. 

#### Openings
We are looking for motivated and aspiring candidates for PhD positions (current vacancy: 2). Candidates interested working in areas such as UAV-IoT networks, Edge computing, Non-terrestrial networks, digital twin, and edge-cloud-continuum may write to me with a copy of their updated CV. For more information about the eligibility criteria, benefits, and fellowship of PhD program, you may visit the following links -- [PhD program](https://admission.iitism.ac.in/index.php/admission/phd).

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}
{% include list.html data="members" component="portrait" filter="role != 'pi'" %}

{% include section.html background="images/background.jpg" dark=true %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
