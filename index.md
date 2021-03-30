---
title: Home
---

<!-- section full -->

{% include banner.html image="images/banner.png" %}

<!-- section break -->

{% capture text %}
Translational science breaks down traditional silos between discreet disciplines of science empowering innovation.
On the front lines of this emerging field, TISLab applies these varied disciplines to the study of the data encoded on phenotypes to unlock new understanding and amplify discovery in areas such as rare disease diagnosis in both plants and humans, accelerated cancer research, coping with climate change, and current pressing issues like COVID-19 and other viral threats.
{% endcapture %}

{%
  include feature.html
  image="images/translational-science.png"
  link="team"
  title="What is Translational Science?"
  text=text
%}

{% capture text %}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{% capture contents %}
{% include big-link.html link="research" text="Learn More" button=true %}
{% endcapture %}
{% include centerer.html contents=contents %}
{% endcapture %}

{%
  include feature.html
  image="images/research.png"
  link="research"
  title="Our Research"
  text=text
%}
