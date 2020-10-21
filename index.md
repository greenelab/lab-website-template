---
title: Home
---

# <i class="fas fa-flask"></i>Home

[Lab Website Template](https://github.com/greenelab/lab-website-template) is an easy-to-use, flexible website template for [labs](https://www.greenelab.com/), with automatic citations, GitHub tag imports, pre-built components, and more.
Spend less time reinventing the wheel, and more time running your lab.

{% include big-link.html icon="fab fa-github" text="See the template and readme on GitHub" link="https://github.com/greenelab/lab-website-template" %}{:.center}

## Basic Formatting

_italic text_

**bold text**

A centered paragraph with `{:.center}`.
Other elements can also be centered with the same method.
{:.center}

- list item 1
- list item 2
- list item 3

Horizontal rule:

---

| TABLE | Game 1 | Game 2 | Game 3 | Total |
| ----- | :----: | :----: | :----: | :---: |
| Anna  |  144   |  123   |  218   |  485  |
| Bill  |   90   |  175   |  120   |  385  |
| Cara  |  102   |  214   |  233   |  549  |

```javascript
// a code block with syntax highlighting
const popup = document.querySelector("#popup");
popup.style.width = "100%";
popup.innerText =
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
```

This sentence has `inline code`, useful for making references to variables, packages, versions, etc within a sentence.

# Heading 1

## Heading 2

Ut aliquam purus sit amet luctus venenatis lectus magna fringilla.
Mi bibendum neque egestas congue quisque egestas diam in.
Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque.
Sapien nec sagittis aliquam malesuada.
Non odio euismod lacinia at quis risus sed vulputate.
Laoreet id donec ultrices tincidunt arcu non sodales neque.

### Heading 3

Enim ut sem viverra aliquet eget sit amet tellus.
Commodo ullamcorper a lacus vestibulum sed arcu non.
Vitae auctor eu augue ut lectus arcu bibendum.
Sapien pellentesque habitant morbi tristique senectus et netus.
Pulvinar proin gravida hendrerit lectus.
Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla.

#### Heading 4

Tristique nulla aliquet enim tortor at auctor.
Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget.
Vulputate sapien nec sagittis aliquam malesuada bibendum.
Volutpat blandit aliquam etiam erat.
Varius quam quisque id diam.
Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat.
Pharetra et ultrices neque ornare aenean euismod elementum nisi.

## Centerer

A _centerer_ component, an alternative method for centering arbitrary items that can't be centered with `{:.center}`, such as groups of pre-built components or manually-written HTML elements:

{% capture html %}

<div>item 1</div>
<div>item 2</div>
<div>item 3</div>
{% endcapture %}

{% include centerer.html html=html spaced=true %}

## Feature

A _feature_ component, with an image, a heading, markdown text, and an optional image link.
Useful for your home page, where you want to highlight key points about your lab.

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Nec sagittis aliquam malesuada bibendum arcu.
{% endcapture %}
{%
  include feature.html
  image="images/laboratory.jpg"
  link="resources"
  heading="Extra, extra, read all about it!"
  text=text
%}

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Nec sagittis aliquam malesuada bibendum arcu.
{% endcapture %}
{%
  include feature.html
  image="images/laboratory.jpg"
  link="resources"
  heading="Extra, extra, read all about it!"
  text=text
%}

## Figure

A _figure_ component with optional caption and image link.

{%
  include figure.html
  image="images/bacteria.jpg"
  caption="A set-height figure"
  height="300px"
  link="team"
%}

{%
  include figure.html
  image="images/bacteria.jpg"
  caption="A full-width figure"
  width="100%"
%}

## Gallery

A _gallery_ component with optional tooltips and image links.

{%
  include gallery.html
  image1="images/cell.jpg"
  tooltip1="Cell"
  link1="https://cell.com/"
  image2="images/virus.jpg"
  tooltip2="Virus"
  image3="images/cell.jpg"
  tooltip3="Cell"
  link3="https://cell.com/"
  image4="images/virus.jpg"
  image5="images/bacteria.jpg"
%}

A _gallery_ component, without fitting the images to squares, and without the image effects.
Useful for transparent images, and images that should not be cropped, like logos.

{%
  include gallery.html
  flat="true"
  fit="false"
  image1="images/cell.jpg"
  tooltip1="Cell"
  link1="https://cell.com/"
  image2="images/virus.jpg"
  tooltip2="Virus"
  image3="images/cell.jpg"
  tooltip3="Cell"
  link3="https://cell.com/"
  image4="images/virus.jpg"
  image5="images/bacteria.jpg"
%}

## Card

A multi-size, flexible _card_ component, with an image, a title link, markdown text, and extra rows for special items such as tags.

{% capture tags %}
{% include tags.html tags="red hammer elephant supercalifragilisticexpialidocious" %}
{% endcapture %}

{% capture largecards %}
{%
  include card.html
  size="large"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Large card"
  truncate=2
  row1="A clickable truncated row of really long text that is too wide to fit in the card but can still be expanded by focusing it"
  row2="Another truncated row of really long text"
  row3="A really long row of text that wraps instead of truncating"
%}
{% capture html %}
An example of putting other components in a row:
{% endcapture %}
{%
  include card.html
  size="large"
  image="images/typo-in-filename-whoops.jpg"
  row1="A card with a placeholder image in case the specified image can't be loaded"
  row2=tags
%}
{% endcapture %}

{% include centerer.html html=largecards %}

{% capture mediumcards %}
{%
  include card.html
  size="medium"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Medium card"
  row1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In aliquam sem fringilla ut."
%}
{%
  include card.html
  size="medium"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Medium card"
  row1="Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  row2=tags
%}
{%
  include card.html
  size="medium"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Medium card"
  row1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In aliquam sem fringilla ut."
%}
{% endcapture %}

{% include centerer.html html=mediumcards %}

{%
  include card.html
  size="small"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Small card"
  row1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In aliquam sem fringilla ut."
  row2=tags
%}
{%
  include card.html
  size="small"
  image="images/space.jpg"
  link="https://nasa.gov/"
  heading="Small card"
  truncate=1
  row1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In aliquam sem fringilla ut."
%}

## Big Link

A _big link_ component, useful for emphasizing important links, such as other key pages on your site that aren't in the top nav bar.

{% include big-link.html icon="fas fa-hands-helping" text="Join the team" link="/join" -%}
{%- include big-link.html icon="fas fa-user-friends" text="Collaborators" link="/collaborators" -%}
{:.center}

## Tags

A _tags_ component.
Provide your own list of tags separated by spaces, and/or provide a GitHub repo and its "tags" (GitHub calls them [topics](https://github.com/topics)) will be fetched automatically!
You can include this as part of other components, such as the _card_ component.

{%
  include tags.html
  tags="ovarian-cancer dataset gene-expression"
  repo="greenelab/lab-website-template"
%}

## Social Link

A customizable _social link_ component, with icon and tooltip.
Specify custom links, or leave blank to use site defaults in `_config.yml`.
To see the built-in links and add your own, see `/_includes/social-link.html`.

{% capture html %}
{% include social-link.html type="website" link=page.website %}
{% include social-link.html type="contact" %}
{% include social-link.html type="email" %}
{% include social-link.html type="google" %}
{% include social-link.html type="github" %}
{% include social-link.html type="twitter" %}
{% include social-link.html type="instagram" %}
{% include social-link.html type="youtube" %}
{% endcapture %}

{% include centerer.html html=html %}

## Paper Link

A customizable _paper link_ component, with icon and text.
Useful for showing supplementary links for a paper.
To see the built-in links and add your own, see `/_includes/paper-link.html`.

{% capture html %}
{% include paper-link.html type="website" link="https://greenelab.com/" %}
{% include paper-link.html type="journal" link="https://greenelab.com/" %}
{% include paper-link.html type="preprint" link="https://greenelab.com/" %}
{% include paper-link.html type="app" %}
{% include paper-link.html type="data" text="Server" %}
{% endcapture %}

{% include centerer.html html=html %}

## Role

A customizable _role_ component, with an icon and optional text, useful for quickly indicating what different team members do.
To see the built-in roles and add your own, see `/_includes/role.html`.

{% capture html %}
{%
  include role.html
  type="pi"
  text=true
%}
{%
  include role.html
  type="phd"
  text=true
%}
{%
  include role.html
  type="programmer"
  text=true
%}
{%
  include role.html
  type="pi"
%}
{%
  include role.html
  type="phd"
%}
{%
  include role.html
  type="programmer"
%}
{% endcapture %}

{% include centerer.html html=html spaced=true %}

## Portrait

A multi-size _portrait_ component with an image, link, name, and role icon, useful for team member links.

{% capture html %}
{%
  include portrait.html
  link="/members/anne-chovie"
  image="images/corgi.jpg"
  name="Anne Chovie"
  role="programmer"
%}
{%
  include portrait.html
  image="images/labrador.jpg"
  name="Felix Cited"
  role="pi"
  mini=true
%}
{%
  include portrait.html
  mini=true
%}
{% endcapture %}

{% include centerer.html html=html %}

## Font Awesome Icons

[Font Awesome](https://fontawesome.com/) is a large library of beautiful, clean, consistent, professionally-designed icons.
[Find the icon you want](https://fontawesome.com/icons?d=gallery&q=icon&m=free), and paste its HTML code right into your markdown:

<i class="fas fa-flask"></i>
<i class="fas fa-microscope"></i>
<i class="fas fa-glasses"></i>
<i class="fas fa-vial"></i>
<i class="fas fa-bacteria"></i>
<i class="fas fa-virus"></i>

Use the same [style](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use) of icon across your site to maintain a consistent look.
See the [styling section](https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons) of their docs to see some of the easy ways you can modify the look of the icons.
