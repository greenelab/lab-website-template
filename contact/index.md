---
title: Contact
nav:
  order: 4
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

A small text for contacts

{%
  include button.html
  type="email"
  text="emad.askarinejad@gmail.com"
  link="emad.askarinejad@gmail.com"
%}
{%
  include button.html
  type="phone"
  text="(438) 465-2705"
  link="+1-438-465-2705"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/brainImage.jpg"
  caption="1st image of contacts"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/brainImage.jpg"
  caption="2nd image of contacts"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
1st col end of the page
{% endcapture %}

{% capture col2 %}
2nd col end of the page
{% endcapture %}

{% capture col3 %}
3rd col end of the page
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
