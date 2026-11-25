---
title: Education
nav:
  order: 3
  tooltip: Courses and supervised theses
seo_title: "Robotics Courses and MSc Theses | p4MARS Lab, TU Delft"
seo_description: "Courses taught by the p4MARS Lab at TU Delft, from robot perception with ROS to deep learning for vision, plus the MSc theses we supervise."
---

{% include section.html size="full" %}

{% include page-hero.html title="Education" icon="fa-solid fa-book" %}

{% include section.html %}

{% include section.html %}

## Courses

{% capture text %}

This project-based course introduces students to robotics systems, sensing and perception, and the Robot Operating System (ROS) through a combination of lectures, self-study materials, and hands-on labs. Working in teams, students tackle simplified real-world challenges proposed by TU Delft researchers, companies, and governmental organizations. Using the MIRTE Master robotic platform and a toolbox of sensors and software modules, students design, integrate, and evaluate perception systems that enable robots to operate autonomously in unknown environments. It concludes with a symposium where teams present their system design on a poster and demonstrate their robotic solution to academic and industry audiences.

{%
  include button.html
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/21184"
  text="Study guide"
  icon="fa-solid fa-arrow-up-right-from-square"
  flip=true
  style="bare"
%}
{%
  include button.html
  link="https://youtu.be/IWHBAUt_tHI?si=uD2Bq4A_ML17c6zx"
  text="Course content"
  icon="fa-brands fa-youtube"
  flip=true
  style="bare"
%}
{%
  include button.html
  link="https://youtu.be/bxEkVHfG4ek?si=JVCWKX9t7y-C6wFP"
  text="Course structure"
  icon="fa-brands fa-youtube"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/spatial-ai-2526Q4.jpg"
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/21184"
  title="AE4ASM527 &middot; Spatial AI for Industrial Automation"
  text=text
%}

{% capture text %}

A bachelor course in the TU Delft Robotics minor on everything it takes to build an intelligent robot, from both a computer-science and an electrical-engineering perspective. Following the sense–think–act loop, students work through microcontrollers and data handling, perception and localization, navigation and planning, ROS and Gazebo, decision trees, behavior trees and state machines, and inverse kinematics with coordinate transforms and TF trees. Weekly lectures are combined with hands-on practical sessions, and students learn to make and justify design choices under real constraints of time and cost.

{%
  include button.html
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/37221"
  text="Study guide"
  icon="fa-solid fa-arrow-up-right-from-square"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/teaching/robotics-stack.svg"
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/37221"
  title="WB3708 &middot; Robot Intelligence Stack<span class='feature-subtitle'>(Sensing, Actuation and Primitive Decision Making)</span>"
  text=text
  flip=true
%}

{% capture text %}

A project-based master course run in close collaboration with companies and governmental organizations. Over eight weeks, student teams tackle a real engineering challenge proposed by an external stakeholder, working across the full data pipeline: data processing, analytics and feature engineering, machine learning, and visualization. Supported by self-study materials, thematic sessions, lab exercises and teaching assistants, teams apply agile project management, engage directly with industry experts, and deliver a data story, a code base and concrete recommendations for how their prototype can be taken into practice.

{%
  include button.html
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/37558"
  text="Study guide"
  icon="fa-solid fa-arrow-up-right-from-square"
  flip=true
  style="bare"
%}
{%
  include button.html
  link="https://youtu.be/07NJn7Hbc40"
  text="Course content"
  icon="fa-brands fa-youtube"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/teaching/data-science.svg"
  link="https://studiegids.tudelft.nl/courses/study-guide/educations/37558"
  title="CIEM6306 &middot; Advanced Data Science in Engineering Applications"
  text=text
%}

{% include section.html %}

## Projects

{% include list.html data="projects" component="project" filter="title.include?('Open-Source Interactive Education')" %}

{% include section.html %}

## On-going and Completed Theses

### Completed

{% include list.html data="theses" component="thesis" %}

<!-- Add theses to _data/theses.yaml -->
