---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# <i class="fas fa-envelope"></i>Contact

Our lab is part of the [Department of Metaphor](), at the school of [Whimsy and Caprice]().
We are located on the 13th floor of the [Center for Wit and Sagacity]().

{%
  include link.html
  type="email"
  icon=""
  text="scrooge@mcduck.com"
  tooltip=""
  link="scrooge@mcduck.com"
  style="button"
%}
{%
  include link.html
  type="phone"
  icon=""
  text="(555) 867-5309"
  tooltip=""
  link="+1-555-867-5309"
  style="button"
%}
{%
  include link.html
  type="address"
  icon=""
  text="Google Maps"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps/place/That+St+%26+The+Other+St,+Porters+Lake,+NS+B3E+1H3,+Canada/@44.7389237,-63.3033296,20.78z/data=!4m5!3m4!1s0x4b5a31023bb02565:0xb9505694e83a53d7!8m2!3d44.7389353!4d-63.3030828"
  style="button"
%}
{:.center}

{% include section.html %}

### <i class="fas fa-mail-bulk"></i>Mailing Address

That St & The Other St  
Porters Lake, NS B3E 1H3  
Canada
{:.center}

{% capture col1 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="The Center for Wit and Sagacity"
%}
{% endcapture %}
{% capture col2 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="Department of Metaphor"
%}
{% endcapture %}
{% include two-col.html col1=col1 col2=col2 %}
