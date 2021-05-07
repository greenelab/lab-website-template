---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

Our lab is made up of a highly engaged and collaborative team of researchers. We recognize that diverse teams do better research. We foster an environment where team members are treated equally, and where we respect and admire our differences. The team includes postdocs, students at all levels, staff, and our lab mascots.


{% capture contents %} {% include team-list.html role="pi" group="" %} {% include team-list.html role="postdoc" group="" %} {% include team-list.html role="phd" group="" %} {% include team-list.html role="undergrad" group="" %} {% include team-list.html role="programmer" group="" %} {% include team-list.html role="mascot" group="" %} {% endcapture %}

{% include centerer.html contents=contents %}

We work with a wide range of outstanding groups from around the world, and we're always on the lookout for new and unique perspectives. We want to push the frontier of data science and train the next generation of data scientists.

{% include big-link.html icon="fas fa-hands-helping" text="Join the Team" link="join" button=true %}{:.center}

<!-- section break -->


{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer"
%}
{:.center}

{% include section.html background="images/banner.jpg" dark=true%}


Text about alumni...
{% capture contents %} {% include team-list.html role="pi" group="alum" mini="true" %} {% include team-list.html role="postdoc" group="alum" mini="true" %} {% include team-list.html role="phd" group="alum" mini="true" %} {% include team-list.html role="undergrad" group="alum" mini="true" %} {% include team-list.html role="programmer" group="alum" mini="true" %} {% include team-list.html role="mascot" group="alum" mini="true" %} {% endcapture %}

{% include centerer.html contents=contents %}




{%
  include link.html
  icon="fas fa-hands-helping"
  text="Join the Team"
  link="join"
  style="button"
%}
{:.center}

{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.
{:.center}

{%
  include gallery.html
  style="square"

  image1="images/photo.jpg"
  link1="https://nasa.gov/"
  tooltip1="Cool Foundation"

  image2="images/photo.jpg"
  link2="https://nasa.gov/"
  tooltip2="Cool Institute"

  image3="images/photo.jpg"
  link3="https://nasa.gov/"
  tooltip3="Cool Initiative"

  image4="images/photo.jpg"
  link4="https://nasa.gov/"
  tooltip4="Cool Foundation"

  image5="images/photo.jpg"
  link5="https://nasa.gov/"
  tooltip5="Cool Institute"

  image6="images/photo.jpg"
  link6="https://nasa.gov/"
  tooltip6="Cool Initiative"
%}
