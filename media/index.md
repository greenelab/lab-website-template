---
title: Media
nav:
  order: 7
  tooltip: Interviews, talks and press
---

{% include section.html size="full" %}

{% include page-hero.html title="Media" icon="fa-solid fa-photo-film" %}

{% include section.html %}

<!-- To add an item, edit _data/media.yaml -->

{% include section.html %}

<div class="media-list">
  {% assign items = site.data.media | sort: "date" | reverse %}
  {% for item in items %}
    {% include media-item.html title=item.title type=item.type outlet=item.outlet date=item.date description=item.description link=item.link image=item.image %}
  {% endfor %}
</div>
