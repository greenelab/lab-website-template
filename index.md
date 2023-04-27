---
subtitle: biomedical informatics
---

# Who we are, what we do

We are a research laboratory at the [University of Colorado Anschutz Medical Campus](https://medschool.cuanschutz.edu/).
Our research is focused on developing novel machine-learning methods to advance key computational aspects of precision medicine.
For this, we design and develop computational algorithms and tools that are applied to human disease with a systems biology approach.

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

Our team is committed to developing robust and user-friendly tools to facilitate reproducible research.
Our software is openly accessible on GitHub and conveniently packaged for easy installation.
These resources are designed to promote transparency and accessibility in academic research, enabling fellow scholars to replicate and build upon our findings.

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/neural_net2.png"
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
