---
title: About
nav:
  order: 1
  tooltip: Learn about our lab.
---

# About

{%
  include button.html
  link="about/#story"
  text="Story"
  tooltip="Read about us!"
%}

{%
  include button.html
  link="about/#research-areas"
  text="Research Areas"
  tooltip="Interested in what we do?"
  flip=true
%}

{%
  include section.html
%}

## Story


{%
  include section.html
%}

## Research Areas

{%
  include feature.html
  image="images/group-photo.jpg"
  title="Action Recognition"
  text="This field focuses on identifying human actions from videos using two main methods: skeleton-based, which tracks body joints to detect movements, and video-based, which analyzes full video frames for detailed context. Advancements include video captioning for generating descriptions, highlighted moment segmentation for pinpointing key events, and sequence matching for recognizing patterns. These innovations aim to provide deeper insights and more accurate understanding of video content."
  flip=true
%}

{%
  include feature.html
  image="images/group-photo.jpg"
  title="Video Anomaly Detection"
  text="Focuses on identifying unusual events in video streams, but existing methods often struggle with limited datasets, camera viewpoints, and scenario diversity. These methods frequently lack generalizability, requiring retraining for new environments, and are vulnerable to factors like lighting changes and complex backgrounds, leading to false positives and negatives. To improve reliability, there’s a need for comprehensive, multi-scenario datasets that better reflect real-world conditions and enhance detection accuracy across diverse surveillance scenarios."
%}

{%
  include feature.html
  image="images/about/taylor-video.gif"
  title="Video Representation"
  text="Focuses on exploring new modalities for videos beyond traditional methods like RGB, optical flow, and depth video. A key innovation is Taylor video, which captures dominant motions, leading to more efficient and privacy-conscious representations. This approach reduces redundancy and enhances data efficiency, paving the way for advanced video analysis, storage, and transmission while addressing concerns related to privacy and ethical use of video content."
  flip=true
%}

{%
  include feature.html
  image="images/about/motion-video.gif"
  title="Motion-centric video processing"
  text="Focuses on using motion patterns and dynamics in videos to enhance understanding while protecting privacy. By concentrating on motion rather than full visual details, it addresses ethical concerns in surveillance. This approach also enables the use of motion data as signals or sequences in large language models, advancing tasks like action recognition and privacy-preserving video analytics."
%}
