---
title: Testbed
---

# Heading 1

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Heading 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### Heading 3

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Heading 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

_italic text_

**bold text**

~~strike-through text~~

<br>
<br>
Text with extra blank lines above and below
<br>
<br>
 
- list item a
- list item b
- list item c
 
1. ordered list item 1
2. ordered list item 2
3. ordered list item 3
 
[External link](https://some-website.org/)
 
[Internal link](team)
 
Centered free text
{:.center}
 
Horizontal rule:
 
---
 
| TABLE | Game 1 | Game 2 | Game 3 | Total |
| :---- | :----: | :----: | :----: | ----: |
| Anna  |  144   |  123   |  218   |   485 |
| Bill  |   90   |  175   |  120   |   385 |
| Cara  |  102   |  214   |  233   |   549 |
 
> It was the best of times it was the worst of times.
> It was the age of wisdom, it was the age of foolishness.
> It was the spring of hope, it was the winter of despair.
 
```javascript
// some code with syntax highlighting
const popup = document.querySelector("#popup");
popup.style.width = "100%";
popup.innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
```
 
This sentence has `inline code`, useful for making references to variables, packages, versions, etc. within a sentence.
 
Font Awesome icons:
{% include icon.html icon="fa-solid fa-flask" %}
{% include icon.html icon="fa-solid fa-microscope" %}
{% include icon.html icon="fa-solid fa-bacteria" %}
{% include icon.html icon="fa-solid fa-virus" %}

{% include section.html %}

## Section

{% include section.html dark=false full=false %}

Section, `dark=false`

{% include section.html dark=true full=false %}

Section, `dark=true`

{% include section.html background="images/background.jpg" %}

Section, `background` `dark=false`

{% include section.html background="images/background.jpg" dark=true %}

Section, `background` `dark=true`

{% include section.html %}

## Figure

{% include figure.html image="images/photo.jpg" caption="`px` width" link="team" width="400px" %}
{% include figure.html image="images/photo.jpg" caption="`%` width" link="team" width="50%" %}
{% include figure.html image="images/photo.jpg" caption="`px` height" link="team" height="200px" %}
{% include figure.html image="images/fallback.svg" caption="`px` width, svg" link="team" width="400px" %}
{% include figure.html image="images/fallback.svg" caption="`%` width, svg" link="team" width="50%" %}
{% include figure.html image="images/fallback.svg" caption="`px` height, svg" link="team" height="200px" %}

{% include section.html size="full" %}

{% include figure.html image="images/background.jpg" link="team" width="100%" %}

{% include section.html %}

## Grid

{% capture content %}
{% include figure.html image="https://journals.plos.org/ploscompbiol/article/figure/image?size=inline&id=info:doi/10.1371/journal.pcbi.1007128.g001&rev=2" %}
{% include figure.html image="https://ars.els-cdn.com/content/image/1-s2.0-S2001037020302804-gr1.jpg" %}
{% include figure.html image="https://iiif.elifesciences.org/lax:32822%2Felife-32822-fig8-v3.tif/full/863,/0/default.webp" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% endcapture %}
{% include grid.html style="square" content=content %}

{% include section.html %}

## Feature

{% include feature.html image="images/photo.jpg" link="team" title="Title" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." %}
{% capture text %}
_lorem_ **ipsum**.
{:.center}
{% endcapture %}
{% include feature.html image="images/photo.jpg" link="team" title="Title" text=text flip=true %}

{% include section.html %}

## Button

{% include button.html type="github" %}
{% include button.html type="github" style="bare" %}

{% include section.html %}

## List

{% include list.html data="members" component="portrait" filters="group: " %}
{% include list.html data="members" component="portrait" filters="group: alum" style="small" %}
{% include list.html data="citations" component="citation" filters="date: ^2020" %}

{% include section.html %}

## Card

{% include card.html image="images/photo.jpg" link="https://nasa.gov/" title="A Large Card" subtitle="A cool card" description="A cool description" tooltip="A cool tooltip" tags="manual tag" repo="greenelab/lab-website-template" %}
{% include card.html image="images/photo.jpg" link="https://nasa.gov/" title="A Small Card" subtitle="A cool card" description="A cool description" tooltip="A cool tooltip" tags="manual tag" repo="greenelab/lab-website-template" style="small" %}

{% include section.html %}

## Citation

{% include citation.html lookup="doi:10.1016/j.csbj.2020.05.017" %}
{% include citation.html lookup="Constructing knowledge graphs" style="rich" %}

{% include section.html %}

## Tags

{% include tags.html tags="ovarian cancer, dataset, gene expression" repo="greenelab/lab-website-template" link="blog" %}

{% include section.html %}

## Portrait

{% include portrait.html id="felix-cited" %}

{% include section.html %}

## Cols

{% capture col1 %}
{% include figure.html image="images/photo.jpg" caption="Fig. 1a" %}
Lorem _ipsum_ dolor **sit** amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% capture col2 %}
{% include figure.html image="images/photo.jpg" caption="Fig. 1b" %}
Lorem _ipsum_ dolor **sit** amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% include cols.html col1=col1 col2=col2 %}

{% include section.html %}

## Post Excerpt

{% include post-excerpt.html lookup="example-post-1" %}

{% include section.html %}

## Search

{% include search-box.html %}
{% include search-info.html %}

{% include section.html %}

## Site Search

{% include site-search.html %}

{% include section.html %}
