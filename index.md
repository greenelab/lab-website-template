---
title: Home
background: images/test-tube.jpg
---

# <i class="fas fa-flask"></i>Lab Website Template

An easy-to-use, flexible website template for [labs](https://www.greenelab.com/), with automatic citations, GitHub tag imports, pre-built components, and more.
Spend less time reinventing the wheel, and more time running your lab.

{% include big-link.html icon="fab fa-github" text="See the template and readme on GitHub" link="https://github.com/greenelab/lab-website-template" %}{:.center}

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

## Big Link

A _big link_ component, useful for emphasizing important links, such as other key pages on your site that aren't in the top nav bar.

{% include big-link.html icon="fas fa-hands-helping" text="Join the team" link="/join" -%}
{%- include big-link.html icon="fas fa-hands-helping" text="Join the team" link="/join" -%}
{:.center}

## Font Awesome Icons

[Font Awesome](https://fontawesome.com/) is a large professionally-designed library of clean, consistent icons.
[Find the icon you want](https://fontawesome.com/icons?d=gallery&q=flask), and paste its HTML code right into your markdown:

<i class="fas fa-flask"></i>
<i class="fas fa-microscope"></i>
<i class="fas fa-glasses"></i>
<i class="fas fa-vial"></i>
<i class="fas fa-bacteria"></i>
<i class="fas fa-virus"></i>

Use the same [style](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use) of icon across your site to maintain a consistent look.
See the [styling section](https://fontawesome.com/how-to-use/on-the-web/styling/sizing-icons) of their docs to see some of the easy ways you can modify the look of the icons.

## Basic Formatting

_italic text_

**bold text**

A centered paragraph.
Other elements can also be centered with the same method.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{:.center}

- list item 1
- list item 2
- list item 3

| TABLE  | Game 1 | Game 2 | Game 3 | Total |
| ------ | :----: | :----: | :----: | :---: |
| Anna   |  144   |  123   |  218   |  485  |
| Bill   |   90   |  175   |  120   |  385  |
| Cara   |  102   |  214   |  233   |  549  |

```javascript
// a code block with syntax highlighting
const popup = document.querySelector("#popup");
popup.style.width = "100%";
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
```

This sentence has `inline code`, useful for making references to variables, packages, versions, etc within a sentence.

# Heading 1

## Heading 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Tortor id aliquet lectus proin nibh nisl.
Pretium lectus quam id leo in.
Arcu felis bibendum ut tristique et.
Et magnis dis parturient montes nascetur.
Tincidunt lobortis feugiat vivamus at augue eget arcu dictum.
Auctor urna nunc id cursus metus aliquam eleifend mi.
Pretium viverra suspendisse potenti nullam.
Gravida cum sociis natoque penatibus et.

Ut aliquam purus sit amet luctus venenatis lectus magna fringilla.
Mi bibendum neque egestas congue quisque egestas diam in.
Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque.
Sapien nec sagittis aliquam malesuada.
Non odio euismod lacinia at quis risus sed vulputate.
Laoreet id donec ultrices tincidunt arcu non sodales neque.

### Heading 3

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur.
Id volutpat lacus laoreet non curabitur gravida arcu ac.
Purus in mollis nunc sed id semper risus in.
Enim ut sem viverra aliquet eget sit amet tellus.
Commodo ullamcorper a lacus vestibulum sed arcu non.
Vitae auctor eu augue ut lectus arcu bibendum.
Sapien pellentesque habitant morbi tristique senectus et netus.
Pulvinar proin gravida hendrerit lectus.
Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla.

#### Heading 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
In aliquam sem fringilla ut.
Blandit cursus risus at ultrices mi tempus imperdiet.
Luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor purus.
Vestibulum morbi blandit cursus risus at ultrices mi.
A arcu cursus vitae congue mauris rhoncus aenean.

Tristique nulla aliquet enim tortor at auctor.
Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget.
Vulputate sapien nec sagittis aliquam malesuada bibendum.
Volutpat blandit aliquam etiam erat.
Varius quam quisque id diam.
Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat.
Pharetra et ultrices neque ornare aenean euismod elementum nisi.
