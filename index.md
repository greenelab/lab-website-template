---
---

{% include section.html size="full" %}

{%
  include hero.html
  eyebrow="TU Delft &middot; Aerospace Engineering"
  title="Perception and AI for <strong>Manufacturing Automation</strong>, <strong>Robotics</strong> and <strong>Space</strong>"
  text="p4MARS builds the perception and world models that let autonomous systems understand, act in, and adapt to complex, dynamic and unstructured environments, from the factory floor to orbit."
  primary-link="research"
  primary-text="Explore our research"
  secondary-link="vacancy"
  secondary-text="Join the lab"
  banner="images/hero-banner.svg"
  banner-alt="A robot arm and its glowing digital twin, with the p4MARS logo"
%}

{% include section.html %}

<h2 class="section-title">About</h2>

### Robust autonomy through perception

The p4MARS Lab is an interdisciplinary research group focused on Perception and AI for Manufacturing Automation, Robotics, and Space, working at the intersection of robotics, agentic AI, and cognitive systems.
We target two classes of problems: automating high-variation tasks in complex and dynamic environments, such as inspection, repair and maintenance, and advanced manufacturing; and building the intelligence behind adaptive, resilient autonomous systems for extreme and unstructured environments, notably space.

Robust autonomy is achieved through advanced perception coupled with high-fidelity digital models that mirror the physical world, enabling embodied and physically grounded intelligence.

<div class="pillars">
  {% include list.html data="pillars" component="pillar" %}
</div>

{% include section.html %}

<h2 class="section-title">Lab lead</h2>

### Reza Sabzevari

<div class="lead">
  {% include portrait.html lookup="reza-sabzevari" %}
  <div class="lead-text" markdown="1">

Reza is an Associate Professor of Robotics and Perception. He leads the p4MARS Lab: an interdisciplinary research group focused on Perception and AI for Manufacturing Automation, Robotics, and Space.

Before joining TU Delft, Reza was a senior scientist at Bosch Research and the Bosch Centre for Artificial Intelligence (BCAI) in Germany, where he founded the x.Lab, a playground for experimenting robot perception algorithms. His research interests include geometric and semantic scene understanding, active perception, and distributed perception, with the application to advanced robotics automation and space domains.

{%
  include button.html
  link="members/reza-sabzevari.html"
  text="Full profile"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

  </div>
</div>

{% include section.html %}

<div class="cta">
  <div>
    <p class="cta-title">Work with us</p>
    <p class="cta-text">We are looking for PhD candidates, thesis students and teaching assistants who want to build perception for real robots.</p>
  </div>
  <div class="hero-actions">
    <a class="hero-button" href="{{ 'vacancy' | relative_url }}">Open positions <i class="icon fa-solid fa-arrow-right"></i></a>
    <a class="hero-button" data-style="ghost" href="{{ 'team' | relative_url }}">Meet the team</a>
  </div>
</div>

{% include section.html %}

<h2 class="section-title">Highlight</h2>

### Featured publication

{% assign pub = site.data.citations | where_exp: "c", "c.title contains 'T-FunS3D'" | first %}
{%
  include citation.html
  style="rich"
  title=pub.title
  authors=pub.authors
  publisher=pub.publisher
  date=pub.date
  description=pub.description
  image=pub.image
  type=pub.type
  buttons=pub.buttons
  tags=pub.tags
  link="https://t-funs3d.github.io/"
%}

{%
  include button.html
  link="research"
  text="Our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% include section.html %}

<h2 class="section-title">News</h2>

### Latest news

{% include list.html data="events" component="event" limit=5 %}

{%
  include button.html
  link="news"
  text="See all news"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
