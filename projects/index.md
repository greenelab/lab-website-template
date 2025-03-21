---
title: Projects
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %} Projects

{% include search-box.html %}

{% for project in site.projects %}
  <div class="post-excerpt-container">
    <div class="post-excerpt">
      {% assign url = project.url %}
      {% assign title = project.title %}
      {% assign image = project.image %}

      {% if image %}
        <a href="{{ url }}" class="post-excerpt-image">
          <img src="{{ image | relative_url }}" alt="{{ title }}">
        </a>
      {% endif %}

      <div class="post-excerpt-text">
        <a href="{{ url }}">{{ title }}</a>
        <p>{{ project.description }}</p>
      </div>
    </div>
  </div>
{% endfor %}
