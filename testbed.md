---
title: Testbed
header: https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg
footer: https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg
header-dark: false
footer-dark: false
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

|              Stage | Direct Products | ATP Yields |
| -----------------: | --------------: | ---------: |
|         Glycolysis |           2 ATP |            |
|                 ^^ |          2 NADH |   3--5 ATP |
| Pyruvaye oxidation |          2 NADH |      5 ATP |
|  Citric acid cycle |           2 ATP |            |
|                 ^^ |          6 NADH |     15 ATP |
|                 ^^ |          2 FADH |      3 ATP |
|         30--32 ATP |                 |            |

$ a \* b = c ^ b $

$ 2^{\frac{n-1}{3}} $

$ \int_a^b f(x)\,dx. $

```mermaid!
pie title Pets adopted by volunteers
  "Dogs" : 386
  "Cats" : 85
  "Rats" : 35
```

{% include section.html %}

## Section

{% include section.html dark=false %}

Section, `dark=false`

{% include section.html dark=true %}

Section, `dark=true`

{% include section.html background="images/background.jpg" %}

Section, `background` `dark=`

{% include section.html background="images/background.jpg" dark=true %}

Section, `background` `dark=true`

{% include section.html size="wide" %}

Section, `size=wide`

{% include section.html %}

## Figure

{% include figure.html image="images/icon.png" caption="`px` width" link="team" width="400px" %}
{% include figure.html image="images/icon.png" caption="`%` width" link="team" width="50%" %}
{% include figure.html image="images/icon.png" caption="`px` height" link="team" height="200px" %}
{% include figure.html image="images/fallback.svg" caption="`px` width, svg" link="team" width="400px" %}
{% include figure.html image="images/fallback.svg" caption="`%` width, svg" link="team" width="50%" %}
{% include figure.html image="images/fallback.svg" caption="`px` height, svg" link="team" height="200px" %}

{% include section.html size="full" %}

{% include figure.html image="images/background.jpg" link="team" width="100%" %}

{% include section.html %}

## Button

{% include button.html type="github" %}
{% include button.html type="github" style="bare" %}
{% include button.html type="github" icon="fa-brands fa-youtube" text="Override Text" tooltip="Override tooltip" %}
{% include button.html type="github" text="" style="bare" %}
{% include button.html type="github" text="" link="github-handle" %}

{% include section.html %}

## Icon

{% include icon.html icon="fa-brands fa-github" %}{% include icon.html icon="orcid.svg" %}{% include icon.html icon="manubot.svg" %}

{% include section.html %}

## Feature

{% include feature.html image="images/icon.png" link="team" title="Title" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." %}
{% capture text %}
_lorem_ **ipsum**.
{:.center}
{% endcapture %}
{% include feature.html image="images/icon.png" link="team" title="Title" text=text flip=true %}
{% include feature.html link="team" title="Title" text=text %}

{% include section.html %}

## List

{% include list.html data="citations" component="citation" %}

---

{% include list.html data="projects" component="card" %}

---

{% include list.html data="members" component="portrait" %}

---

{% include list.html data="posts" component="post-excerpt" %}

{% include section.html %}

## Citation

{% include citation.html lookup="doi:10.1016/j.csbj.2020.05.017" %}
{% include citation.html lookup="Constructing knowledge graphs" style="rich" %}
{% include citation.html title="Manual title" %}
{% include citation.html %}

{% include section.html %}

## Card

{% include card.html image="images/icon.png" link="https://nasa.gov/" title="A Large Card" subtitle="A cool card" description="A cool description" tooltip="A cool tooltip" tags="manual tag" repo="greenelab/lab-website-template" %}
{% include card.html image="images/icon.png" link="https://nasa.gov/" title="A Small Card" subtitle="A cool card" description="A cool description" tooltip="A cool tooltip" tags="manual tag" repo="greenelab/lab-website-template" style="small" %}

{% include section.html %}

## Portrait

{% include portrait.html lookup="jane-smith" %}
{% include portrait.html lookup="john-doe" style="small" %}
{% include portrait.html name="Manual name" %}

{% include section.html %}

## Post Excerpt

{% include post-excerpt.html lookup="example-post-1" %}
{% include post-excerpt.html title="Example post 1" author="No Name Man" date="2020-02-20" last_modified_at="" %}

{% include section.html %}

## Tags

{% include tags.html tags="ovarian cancer, dataset, gene expression" repo="greenelab/lab-website-template" link="blog" %}

{% include section.html %}

## Float

Figures:

{% capture content %}
{% include figure.html image="images/icon.png" caption="Caption" height="100px" %}
{% endcapture %}
{% include float.html content=content %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi etiam dignissim diam quis. Id aliquet lectus proin nibh nisl condimentum id venenatis a. Tristique magna sit amet purus gravida quis blandit turpis cursus. Ultrices eros in cursus turpis massa tincidunt dui ut ornare. A cras semper auctor neque vitae tempus quam pellentesque nec. At tellus at urna condimentum mattis pellentesque. Ipsum consequat nisl vel pretium. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Integer vitae justo eget magna fermentum iaculis eu non diam. Mus mauris vitae ultricies leo integer malesuada nunc vel. Leo integer malesuada nunc vel risus. Ornare arcu odio ut sem nulla pharetra. Purus semper eget duis at tellus at urna condimentum. Enim neque volutpat ac tincidunt vitae semper quis lectus.
{% include float.html clear=true %}
{% include float.html content=content flip=true %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi etiam dignissim diam quis. Id aliquet lectus proin nibh nisl condimentum id venenatis a. Tristique magna sit amet purus gravida quis blandit turpis cursus. Ultrices eros in cursus turpis massa tincidunt dui ut ornare. A cras semper auctor neque vitae tempus quam pellentesque nec. At tellus at urna condimentum mattis pellentesque. Ipsum consequat nisl vel pretium. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Integer vitae justo eget magna fermentum iaculis eu non diam. Mus mauris vitae ultricies leo integer malesuada nunc vel. Leo integer malesuada nunc vel risus. Ornare arcu odio ut sem nulla pharetra. Purus semper eget duis at tellus at urna condimentum. Enim neque volutpat ac tincidunt vitae semper quis lectus.

Code:

{% capture content %}
```javascript
const test = "Lorem ipsum dolor sit amet"
```
{% endcapture %}
{% include float.html content=content %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi etiam dignissim diam quis. Id aliquet lectus proin nibh nisl condimentum id venenatis a. Tristique magna sit amet purus gravida quis blandit turpis cursus. Ultrices eros in cursus turpis massa tincidunt dui ut ornare. A cras semper auctor neque vitae tempus quam pellentesque nec. At tellus at urna condimentum mattis pellentesque. Ipsum consequat nisl vel pretium. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Integer vitae justo eget magna fermentum iaculis eu non diam. Mus mauris vitae ultricies leo integer malesuada nunc vel. Leo integer malesuada nunc vel risus. Ornare arcu odio ut sem nulla pharetra. Purus semper eget duis at tellus at urna condimentum. Enim neque volutpat ac tincidunt vitae semper quis lectus.

{% include section.html %}

## Grid

Regular:

{% capture content %}
{% include figure.html image="https://journals.plos.org/ploscompbiol/article/figure/image?size=inline&id=info:doi/10.1371/journal.pcbi.1007128.g001&rev=2" %}
{% include figure.html image="https://ars.els-cdn.com/content/image/1-s2.0-S2001037020302804-gr1.jpg" %}
{% include figure.html image="https://iiif.elifesciences.org/lax:32822%2Felife-32822-fig8-v3.tif/full/863,/0/default.webp" %}
{% include figure.html image="images/icon.png" %}
{% include figure.html image="images/icon.png" %}
{% include figure.html image="images/icon.png" %}
{% endcapture %}
{% include grid.html content=content %}

Square:

{% capture content %}
{% include figure.html image="https://journals.plos.org/ploscompbiol/article/figure/image?size=inline&id=info:doi/10.1371/journal.pcbi.1007128.g001&rev=2" %}
{% include figure.html image="https://ars.els-cdn.com/content/image/1-s2.0-S2001037020302804-gr1.jpg" %}
{% include figure.html image="https://iiif.elifesciences.org/lax:32822%2Felife-32822-fig8-v3.tif/full/863,/0/default.webp" %}
{% include figure.html image="images/icon.png" %}
{% include figure.html image="images/icon.png" %}
{% include figure.html image="images/icon.png" %}
{% endcapture %}
{% include grid.html style="square" content=content %}

List of citations:

{% capture content %}
{% include list.html data="citations" component="citation" %}
{% endcapture %}
{% include grid.html content=content %}

List of blog posts:

{% capture content %}
{% include list.html data="posts" component="post-excerpt" %}
{% endcapture %}
{% include grid.html content=content %}


{% include section.html %}

## Cols

Text:

{% capture col1 %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% capture col2 %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi etiam dignissim diam quis. Id aliquet lectus proin nibh nisl condimentum id venenatis a.
{% endcapture %}
{% capture col3 %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi etiam dignissim diam quis. Id aliquet lectus proin nibh nisl condimentum id venenatis a. Tristique magna sit amet purus gravida quis blandit turpis cursus. Ultrices eros in cursus turpis massa tincidunt dui ut ornare. A cras semper auctor neque vitae tempus quam pellentesque nec. At tellus at urna condimentum mattis pellentesque. Ipsum consequat nisl vel pretium. Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Integer vitae justo eget magna fermentum iaculis eu non diam. Mus mauris vitae ultricies leo integer malesuada nunc vel. Leo integer malesuada nunc vel risus. Ornare arcu odio ut sem nulla pharetra. Purus semper eget duis at tellus at urna condimentum. Enim neque volutpat ac tincidunt vitae semper quis lectus.
{% endcapture %}
{% include cols.html col1=col1 col2=col2 col3=col3 %}

Images:

{% capture col1 %}
{% include figure.html image="images/icon.png" caption="Fig. 1a" %}
Lorem _ipsum_ dolor **sit** amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% capture col2 %}
{% include figure.html image="images/icon.png" caption="Fig. 1b" %}
Lorem _ipsum_ dolor **sit** amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% capture col3 %}
{% include figure.html image="images/icon.png" caption="Fig. 1c" %}
Lorem _ipsum_ dolor **sit** amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}
{% include cols.html col1=col1 col2=col2 col3=col3 %}


Code:

{% capture col1 %}
```javascript
const test = "Lorem ipsum dolor sit amet"
```
{% endcapture %}
{% capture col2 %}
```javascript
const test = "Lorem ipsum dolor sit amet"
```
{% endcapture %}
{% capture col3 %}
```javascript
const test = "Lorem ipsum dolor sit amet"
```
{% endcapture %}
{% include cols.html col1=col1 col2=col2 col3=col3 %}


{% include section.html %}

## Search

{% include search-box.html %}
{% include search-info.html %}

{% include section.html %}

## Site Search

{% include site-search.html %}

{% include section.html %}
