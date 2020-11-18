---
title: Research
---

# <i class="fas fa-microscope"></i>Research

<!-- section break -->

## Card Search

A _card search_ component, a search box to find all _card_ components on the page that contain certain words/names.

You can type in "terms" (single words) or "phrases" (quoted multiple words), like `term1 term2 "full phrase 1" "full phrase 2"`.
Cards that contain all of the terms and at least one of the phrases will be considered a match.
Search words will be highlighted in the results (if they're longer than 2 characters).
Searching is case insensitive.

{% include card-search.html subject="papers" %}

<!-- section break -->

## Research List

A _research list_ component, to sort and group all of your research publications.
Can be used on any page, but assumes its content from `/_data/research-output.yml`.
Uses the _card_ component (small).

{% include research-list.html %}
