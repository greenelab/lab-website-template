---
title: Event
nav:
  order: 4
  tooltip: Seminar, Retreat, and Activity
---

# {% include icon.html %}Event

{%
  include button.html
  link="event/#seminar"
  text="Seminar"
%}

{%
  include button.html
  link="event/#retreat"
  text="Retreat"
  flip=true
%}

{%
  include button.html
  link="event/#activity"
  text="Activity"
%}

{%
  include section.html
%}

## Seminar

| Topic         | Presenter       | Host | :Description:        | Date       | Resources       |
| ------------- | -------------- | ------------------ | :---------- | ---------- | ------------- |
| Smarter Computing: NCI GADI GPU Research Tips | Qixiang Chen | Prof. Liang's group | This seminar specifically emphasizes NCI basics, highlighting not only how to use but also how to efficiently utilize NCI Gadi computing resources. It has been updated with the latest NCI official Gadi User Guide as of March 2024. | 15 Mar 2024 | [Slides](https://q1xiangchen.github.io/files/gadi_user_guide.pdf), [Codes](https://q1xiangchen.github.io/files/supp.zip) |
| Accelerating Research: NCI GADI GPU Insights | Qixiang Chen | Lei's group | This seminar specifically emphasizes NCI basics, highlighting not only how to use but also how to efficiently utilize NCI Gadi computing resources. Topics covered include environment setup, resource requests, data management, and more. | 8 Dec 2023 | [Slides](https://q1xiangchen.github.io/files/gadi_instructions.pdf), [Codes](https://q1xiangchen.github.io/files/supp.zip) |
| Action Recognition: Past, Present and Future | Dr. Lei Wang | Department of Computer Science, Harbin Institute of Technology, Shenzhen, China | "The next generation of international Chinese young students face to face" Issue 21 International Cooperation and Exchange Program Series Activities of Harbin Institute of Technology (Shenzhen) | 12 Aug 2023 | [Slides](https://leiwangr.github.io/files/AR_PPF_Lei.pdf) |
| Robust Human Action Modelling | Dr. Lei Wang | ANU College of Engineering, Computing and Cybernetics | PhD completion seminar: This seminar covers the following topics (i) an introduction to action recognition (AR) and a comparative review of AR methods, (ii) video-based action recognition, (iii) skeleton-based action recognition, and (iv) one- and few-shot action recognition. | 2 Feb 2023 | [Slides](https://leiwangr.github.io/files/GENG5512ResearchSeminarv4.pdf) |
| Analysis and Evaluation of Kinect-based Action Recognition Algorithms | Dr. Lei Wang | UWA's Department of Computer Science and Software Engineering | MPE Engineering Research Project: In this seminar, I discussed (i) applications, issues, and techniques in action recognition (AR) and (ii) an analysis and evaluation of four handcrafted AR algorithms. | Oct 2017 | [Slides](https://leiwangr.github.io/files/GENG5512ResearchSeminarv4.pdf) |




{% include section.html %}

## Retreat

| **Event**             | **Organizer**       | :**Description**:                                                              | **Date**       | **More Info** |
|-----------------------|---------------------| :------------------------------------------------------------------------------|----------------|---------------|
| TIME Lab Retreat       | TIME Lab       | A full-day retreat featuring presentations, discussions, and collaborative sessions on advanced computing, video modeling, and motion analysis.  | 10 Aug 2024    | [Schedule](retreat/10_08_2024) |





{% include section.html %}

## Activity

Welcome to our vibrant lab community where collaboration extends beyond research. 
Alongside groundbreaking publications and impactful projects, we embrace a shared 
passion for exploration and camaraderie.

{% capture content %}

{% include figure.html image="images/team/team-photo-1.jpg" %}
{% include figure.html image="images/team/group/group-video-1.gif" width="100%" %}
{% include figure.html image="images/team/group/group-photo-2.jpg" %}

{% include figure.html image="images/about/food-2.png" %}
{% include figure.html image="images/activity/gv-1.gif" width="100%" %}
{% include figure.html image="images/activity/gp-6.jpg" %}

{% include figure.html image="images/activity/gv-2.gif" width="100%" %}
{% include figure.html image="images/about/plant-3.png" %}
{% include figure.html image="images/activity/gp-2.jpg" %}


{% endcapture %}

{% include grid.html style="square" content=content %}

More...

<div class="gallery-container">
    <div class="gallery" id="gallery">
        <!-- JavaScript will populate this -->
    </div>
</div>

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }

    .gallery-container {
        max-width: 60%;
        width: 100%;
        max-height: 50vh; /* Set a fixed max height in viewport units to maintain aspect ratio */
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        margin: 0 auto;
    }

    .gallery {
        display: flex;
        flex-wrap: nowrap;
        transition: transform 0.5s ease;
    }

    .gallery-item {
        flex: 0 0 auto;
        width: 100%;
        height: auto;
        box-sizing: border-box;
    }

    .gallery img, .gallery video {
        width: 100%; /* Maintain aspect ratio */
        height: auto; /* Maintain aspect ratio */
        display: block;
        object-fit: cover; /* Ensures the image covers the container */
        object-position: center; /* Centers the image in the container */
    }
</style>

<script>
const mediaFiles = [
    { type: 'image', src: '/images/activity/gp-1.jpg', alt: 'Image 1' },
    { type: 'image', src: '/images/activity/gp-2.jpg', alt: 'Image 2' },
    { type: 'image', src: '/images/activity/gp-3.jpg', alt: 'Image 3' },
    { type: 'image', src: '/images/activity/gp-4.jpg', alt: 'Image 4' },
    { type: 'image', src: '/images/activity/gp-5.jpg', alt: 'Image 5' },
    { type: 'image', src: '/images/activity/gp-6.jpg', alt: 'Image 6' },
    { type: 'image', src: '/images/activity/gp-7.jpg', alt: 'Image 7' },
    { type: 'image', src: '/images/activity/gp-8.jpg', alt: 'Image 8' },
    { type: 'image', src: '/images/activity/gp-9.jpg', alt: 'Image 9' },
    { type: 'image', src: '/images/activity/gp-10.jpg', alt: 'Image 10' },
    { type: 'image', src: '/images/activity/gp-11.jpg', alt: 'Image 11' },
    { type: 'image', src: '/images/activity/gp-12.jpg', alt: 'Image 12' },
    { type: 'image', src: '/images/activity/gp-13.jpg', alt: 'Image 13' },
    { type: 'image', src: '/images/activity/gp-14.jpg', alt: 'Image 14' },
    { type: 'image', src: '/images/activity/gp-15.jpg', alt: 'Image 15' },
    { type: 'image', src: '/images/activity/gp-16.jpg', alt: 'Image 16' },
    { type: 'image', src: '/images/activity/gp-17.jpg', alt: 'Image 17' },
    { type: 'image', src: '/images/activity/gp-18.jpg', alt: 'Image 18' },
    { type: 'image', src: '/images/activity/gp-19.jpg', alt: 'Image 19' },
    { type: 'image', src: '/images/activity/gp-20.jpg', alt: 'Image 20' },
    { type: 'image', src: '/images/activity/gp-21.jpg', alt: 'Image 21' },
    { type: 'image', src: '/images/activity/gp-22.jpg', alt: 'Image 22' },
    { type: 'image', src: '/images/activity/gp-23.jpg', alt: 'Image 23' },
    { type: 'image', src: '/images/activity/gp-24.jpg', alt: 'Image 24' },
    { type: 'image', src: '/images/activity/gp-25.jpg', alt: 'Image 25' },
    { type: 'image', src: '/images/activity/gp-26.jpg', alt: 'Image 26' },
    { type: 'image', src: '/images/activity/gp-27.jpg', alt: 'Image 27' },
    { type: 'image', src: '/images/activity/gp-28.jpg', alt: 'Image 28' },
    { type: 'image', src: '/images/activity/gp-29.jpg', alt: 'Image 29' },
    { type: 'video', src: '/images/activity/gv-1.gif' },
    { type: 'video', src: '/images/activity/gv-2.gif' },
    { type: 'video', src: '/images/activity/gv-3.mp4' },
    { type: 'video', src: '/images/activity/gv-4.mp4' },
    { type: 'video', src: '/images/activity/gv-5.mp4' },
    { type: 'video', src: '/images/activity/gv-6.mp4' },
    { type: 'video', src: '/images/activity/gv-7.mp4' },
    { type: 'video', src: '/images/activity/gv-8.mp4' },
    { type: 'video', src: '/images/activity/gv-9.mp4' },
    { type: 'video', src: '/images/activity/gv-10.mp4' },
    { type: 'video', src: '/images/activity/gv-11.mp4' },
    { type: 'video', src: '/images/activity/gv-12.mp4' }
];

  const gallery = document.getElementById('gallery');

  function shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
  }

  // Shuffle the mediaFiles array
  const shuffledMediaFiles = shuffle(mediaFiles);

  // Populate the gallery
  shuffledMediaFiles.forEach(file => {
      const item = document.createElement('div');
      item.className = 'gallery-item';

      if (file.type === 'image') {
          const img = document.createElement('img');
          img.src = file.src;
          img.alt = file.alt;
          item.appendChild(img);
      } else if (file.type === 'video') {
          const video = document.createElement('video');
          video.src = file.src;
          video.autoplay = true;
          video.loop = true;
          video.muted = true;
          video.playsInline = true;
          item.appendChild(video);
      }

      gallery.appendChild(item);
  });

  let currentIndex = 0;
  const totalItems = mediaFiles.length;

  function scrollToNextItem() {
      currentIndex = (currentIndex + 1) % totalItems; // Loop back to start
      const itemWidth = gallery.clientWidth;
      gallery.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
  }

  setInterval(scrollToNextItem, 5000); // Change item every 5 seconds
</script>