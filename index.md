---
subtitle: biomedical informatics
---

# Who we are, what we do

We are a research laboratory at the [University of Colorado Anschutz Medical Campus](https://medschool.cuanschutz.edu/).
We design advanced machine learning methods applied to human disease with a systems biology approach.
Strongly committed to open source and open science, we use [GitHub](https://github.com/pivlab) for the development of reproducible workflows and [Manubot](https://manubot.org/) for transparent authoring of modern and collaborative scholarly manuscripts.

{% include section.html %}

## Highlights

{% capture text %}

Our ultimate goal is to advance precision medicine by developing a comprehensive, multi-omics approach to understanding the complex interplay between genetics and disease.
Our research uses the latest developments in machine learning for knowledge discovery to increasingly incorporate the emergent complexity present in biological systems.
By leveraging the power of computational analysis and cutting-edge technology, we aim to unlock the secrets of disease and pave the way for new diagnostic and therapeutic approaches.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/ml_and_disease.png"
  image_title="'A realistic painting of machine learning disentangling the molecular mechanisms of disease' by Milton × DALL·E"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="tools"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  text=text
%}
