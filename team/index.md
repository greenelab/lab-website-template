---
title: Team
nav:
  order: 3
  tooltip: About our team
---
{% include party.html %}
# <i class="fas fa-users"></i>Team

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi, status: current"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer, status: current"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc, status: current"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd, status: current"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: student, status: current"
%}
{:.center}

{% include section.html background="images/banner.jpg" dark=true%}


{% include section.html %}


# <i class="fas fa-users"></i>Alumni

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi, status: alumni"
  style="small"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer, status: alumni"
  style="small"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc, status: alumni"
  style="small"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd, status: alumni"
  style="small"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: student, status: alumni"
  style="small"
%}
{:.center}

{% include section.html background="images/banner.jpg" dark=true%}


{% include section.html %}

## Join

We have no open positions at the moment.

{% include link.html type="external" link="https://google.com/" text="Apply Now" icon="" style="button" %}
{:.center}

{% include section.html %}

