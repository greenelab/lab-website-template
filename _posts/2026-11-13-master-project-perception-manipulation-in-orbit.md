---
title: Perception-Guided High-Precision Manipulation for In-Orbit Assembly
image: images/vacancy/perception-manipulation.svg
unavailable: true
author: reza-sabzevari
tags:
  - master-project
---

In-orbit assembly comes down to a classic problem under unforgiving conditions: peg-in-hole. A robot has to insert a peg, a strut, a connector or a docking pin into its receptacle with sub-millimetre clearance, while illumination is harsh and changing, surfaces are specular and textureless, nothing settles under gravity, and no operator can correct a mistake in real time. This project asks whether **vision-language-action (VLA) models** can solve that insertion task end to end, instead of a hand-built pipeline of pose estimation, planning and control.

**What you will work on**

- Applying and fine-tuning a vision-language-action model on peg-in-hole insertion: from images and a task description straight to robot actions.
- Comparing the VLA policy against a classical baseline of pose estimation plus visual servoing, on precision, success rate and recovery from failed insertions.
- Studying what the model needs in order to generalise across peg and hole geometries, tolerances, lighting and viewpoints, and how much of that can come from simulation.
- Dealing with contact: the last millimetres are a contact-rich problem, so the policy has to use force or compliance, not vision alone.
- Validating on a robot arm in the lab with representative mock-ups and space-like lighting.

**What we look for**

- An MSc student in robotics, computer science, aerospace or a related field.
- Experience with deep learning and PyTorch; familiarity with VLA models, imitation learning or reinforcement learning is a plus.
- Comfort with Python and ROS, and willingness to work on real hardware.

This project is currently taken. See the [Vacancy](/vacancy) page for projects that are open.

<!-- TODO: please review this draft description -->
