---
title: Research
nav:
  order: 1
---

# Artificial and Biological Intelligence Laboratory at Boston University

The DePasquale lab is located in the [Department of Biomedical Engineering](https://www.bu.edu/eng/academics/departments-and-divisions/biomedical-engineering/) at Boston University. We develop mathematical models to understand how populations of neurons perform computations to produce behavior. Broadly we take two approaches. One is data-driven: we collaborate with experimental neuroscientists to develop tailored machine learning models of neural activity to identify the algorithms that drive behaviors such as decision-making or movement. Our second approach is theoretical: we construct and analyze artificial neural network models to understand how their structure gives rise to analogous computations and other functional features observed in biological neural circuits.

{% include section.html %}

# Research

{% capture text %}
Recent advances in machine learning methods for computational chemistry have opened exciting new avenues for understanding olfaction. We are utilizing graph neural networks and self-supervised learning to identify patterns in unlabeled molecular data, generating representations of odors that are useful for predicting olfactory sensory neuron activation. These learned representations more accurately predict how individual odor molecules interact with olfactory receptors compared to existing methods.

Relevant poster: [_Improved odor-receptor interaction predictions via self supervised learning_](https://depasquale-lab.github.io/images/Poster_draft_2.pdf) \\
McConachie, G, Duniec, E, Younger, M, DePasquale (2024) \\
NAIsys CSHL 2024
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/GNN-image.jpg"
  caption="GNNs"
  headline="Machine learning models of the early olfactory system"
  text=text
%}


{% capture text %}
Biological neural networks compute differently than most artificial neural networks used in machine learning. For example, although real neurons communicate with spikes, reproducing this feature in artificial models has been a challenge. We develop methods for training biophysically detailed neural networks and use thse models to understand how real biologial circuits compute. Through mathematical modeling, we focus on building tighter links between biologial neural networks and more abstract artifical neural network models used in machine learning. 

Relevant paper: [_The centrality of population-level factors to network computation is demonstrated by a versatile approach for training spiking networks_](https://doi.org/10.1016/j.neuron.2022.12.007) \\
DePasquale, B, Sussillo, D., Abbott, L.F., Churchland, M.M. (2023) \\
in press at Neuron
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/NNs.jpg"
  caption="Low-rank synaptic connections in a spiking neural network"
  headline="Biophysically detailed artificial neural networks"
  text=text
%}

{% capture text %}
Neural recordings from behaving animals are often much too complex to link directly to an animal's ongoing behavior. We develop machine learning models to analyze complex neural datasets to understand the algorithms that underlie different behaviors. We principally focus on the neural underpinnings of movement and decision making. 
 
Relevant paper: [_Neural population dynamics underlying evidence accumulation in multiple rat brain regions_](https://www.biorxiv.org/content/10.1101/2021.10.28.465122v1) \\
DePasquale, B., Brody, C.D., Pillow, J. (2022) \\
in revision at eLife
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/Fig2.jpg"
  caption="Ramping neural activity during decision-making"
  headline="Machine learning for neural data analysis"
  text=text
%}

{% include section.html %}

# Other Recent Publications & Preprints

* [Recurrent dynamics of prefrontal cortex during context-dependent decision-making](https://doi.org/10.1101/2020.11.27.401539) \\
Cohen Z, DePasquale, B., Aoi, M., Pillow, J. (2020) \\
bioRxiv
* [Task-dependent changes in the large-scale dynamics and necessity of cortical regions](https://linkinghub.elsevier.com/retrieve/pii/S0896627319307317) \\
Pinto, L., Rajan, K., DePasquale, B., Thiberge, S.Y., Tank, D.W., Brody, C.D. (2019) \\
 Neuron, 104(4), 810-824. e9
* [full-FORCE: A target-based method for training recurrent networks]("https://doi.org/10.1371/journal.pone.0191527")
<a href="https://github.com/briandepasquale/full-FORCE-demos" style="text-decoration: none"><i class="fab fa-github"></i> code</a> \\
DePasquale, B., Cueva, C.J., Rajan, K., Escola, G.S. & Abbott, L.F. (2018) \\
PLoS One 13(2): e0191527
* [Error-correcting dynamics in visual working memory](https://www.nature.com/articles/s41467-019-11298-3) \\
Panichello, M.F., DePasquale, B., Pillow, J.W. & Buschman, T.J. (2018) \\
Nature Communications 10, Article number: 3366
* [Building functional networks of spiking model neurons](https://www.nature.com/articles/nn.4241) \\
Abbott, L.F., DePasquale, B., Memmesheimer, R.-M. (2016) \\
Nature Neuroscience 19:350-355

For a full list of publications, see [Brian's Google Scholar](https://scholar.google.com/citations?user=dkRSv1AAAAAJ&hl=en).
{:.center}

{% include section.html %}

<div style="text-align: center;">
    <img src="images/BU.jpeg" >
</div>
