---
title: Transferable Spatial Intelligence
outcomes:
  - title: "T-FunS3D: Task-Driven Hierarchical Open-Vocabulary 3D Functionality Segmentation"
    label: Publication · ICRA 2026
    icon: fa-solid fa-file-lines
    image: images/research/T-FunS3D_teaser.webp
    description: >-
      T-FunS3D segments the functional parts of a 3D scene (handles, knobs, buttons, drawers) directly
      from a natural-language task description. It builds an open-vocabulary 3D scene graph from posed
      RGB-D frames and reasons hierarchically from the scene to objects to their functional parts, so a
      robot is told not just *what* is in the room but *where to act* to complete a task. Presented at
      the IEEE International Conference on Robotics and Automation (ICRA) 2026 in Vienna.
    buttons:
      - type: website
        text: Project website
        link: https://t-funs3d.github.io/
      - type: paper
        text: Paper
        link: https://arxiv.org/abs/2606.05975v1
      - type: source
        text: Code
        link: https://github.com/EdwardjkFeng/T-FunS3D
  - title: From Language to Action with Open-Vocabulary 3D Scene Understanding
    label: Demo · Robots in Business 2026 · RoboHouse, Delft · 19 Nov 2026
    icon: fa-solid fa-robot
    image: images/events/robots-in-business-2026.png
    description: >-
      At Robots in Business 2026, the annual RoboHouse event on business applications of robotics and
      embodied AI, we demonstrate open-vocabulary navigation and manipulation built on T-FunS3D: a robot
      receives a task in plain language, finds the relevant object and functional part in the scene, and
      acts on it. The demo shows how transferable spatial intelligence moves from a research result to a
      working robot.
    buttons:
      - type: link
        text: Event page
        link: https://robohouse.tudelftcampus.nl/events/robots-in-business-the-robots-are-here
seo_description: "Transferable Spatial Intelligence: open-vocabulary 3D scene graphs and vision-language models that tell robots where to act. Includes T-FunS3D (ICRA 2026)."
---

<p class="eyebrow"><a href="{{ 'projects' | relative_url }}">Projects</a></p>

# {% include icon.html icon="fa-solid fa-cube" %}Transferable Spatial Intelligence

Robots that understand a 3D scene not only as geometry, but as objects, their functional parts, and what can be done with them, and that carry this understanding across environments, tasks and embodiments.

We combine 3D scene graphs with vision-language foundation models to obtain open-vocabulary, task-driven perception that transfers to new settings without retraining. The goal is actionable perception: given a task in natural language, a robot should know where in the scene to look and where to act.

{% assign project = site.data.projects | where: "title", "Transferable Spatial Intelligence" | first %}
{% include project-links.html vacancies=project.vacancies %}
{% include sponsors.html sponsors=project.sponsors %}

{% include tags.html tags="scene understanding, scene graph, foundation models, robotics" %}

{% include section.html %}

## Outcomes

{% for o in page.outcomes %}
<div class="outcome">
{% include project.html label=o.label title=o.title icon=o.icon image=o.image description=o.description buttons=o.buttons %}
</div>
{% endfor %}
