---
title: Contact
nav:
  order: 8
  tooltip: Email, address, and location
seo_title: "Contact | p4MARS Lab, TU Delft Aerospace Engineering"
seo_description: "Contact the p4MARS Lab at the TU Delft Faculty of Aerospace Engineering, Kluyverweg 1, Delft: email Reza Sabzevari or book a meeting."
---

{% include section.html size="full" %}

{% include page-hero.html title="Contact" icon="fa-regular fa-envelope" %}

{% include section.html %}

{%
  include button.html
  type="email"
  link="r.sabzevari@tudelft.nl"
%}
{%
  include button.html
  icon="fa-regular fa-calendar-check"
  text="Schedule a meeting"
  tooltip="Schedule a meeting via Microsoft Bookings"
  link="https://bookings.cloud.microsoft/bookwithme/user/7fcaff9dda37434d9343d10fc312cc4c@tudelft.nl/meetingtype/vhXb3wMD0kSkKbGIHRgMJg2?anonymous&ismsaljsauthenabled&ep=mLinkFromTile"
%}
{% if site.links.linkedin %}
{%
  include button.html
  type="linkedin"
  link=site.links.linkedin
%}
{% endif %}
<!-- {%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/aGo3qTV3fbQ7GBRGA"
%} -->

{% capture map_embed %}
<iframe
  src="https://www.google.com/maps?q=TU+Delft+Faculty+of+Aerospace+Engineering,+Kluyverweg+1,+2629+HS+Delft&output=embed"
  width="100%"
  height="100%"
  style="border: 0;"
  allowfullscreen=""
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade"
></iframe>
{% endcapture %}

{% capture contact_text %}

<div class="center">

<b>TU Delft Faculty of Aerospace Engineering</b>
<br>Kluyverweg 1, 2629 HS Delft, The Netherlands

</div>

{% endcapture %}

<style>
.feature-compact {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  gap: 20px;
}
</style>

{%
  include feature.html
  embed=map_embed
  title="Address"
  text=contact_text
  flip=true
  class="feature-compact"
%}