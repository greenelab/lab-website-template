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

{% include section.html background="images/activity/gp-8.jpg" dark="true" %}

## Story

TIME Lab is a dynamic research team composed of master's and honours students from ANU, engaged in final-year research projects under the expert guidance of Dr. Lei Wang. Established in February 2024, our team is dedicated to advancing the fields of video processing, dynamics, and motion analysis, addressing both academic challenges and industry needs.

Our research spans diverse domains, with a particular focus on enhancing safety, security, future cities, IoT, agribusiness, and defence, including applications in health and innovative industries. We are committed to developing cutting-edge techniques for real-time analysis and efficient video data processing to improve performance and safety across these areas.

Time Lab members have forged strong collaborations with industry leaders like Active Intelligence Corp. in Western Australia, CSIRO's Data61, and have built academic partnerships with institutions such as the University of Central Florida and Curtin University.

We are a team driven by passion, discipline, and a strong work ethic, expertly balancing our commitments to work, study, and life. United by our belief in making meaningful contributions to science, we strive to push the boundaries of knowledge, one step at a time.


{%
  include section.html
%}

## Research Areas

{%
  include feature.html
  image="images/about/action-recognition.gif"
  title="Action Recognition"
  text="This field focuses on identifying human actions from videos using two main methods: skeleton-based, which tracks body joints to detect movements, and video-based, which analyzes full video frames for detailed context. Advancements include video captioning for generating descriptions, highlighted moment segmentation for pinpointing key events, and sequence matching for recognizing patterns. These innovations aim to provide deeper insights and more accurate understanding of video content."
  flip=true
%}

{%
  include feature.html
  image="images/about/vad.gif"
  title="Video Anomaly Detection"
  text="Focuses on identifying unusual events in video streams, but existing methods often struggle with limited datasets, camera viewpoints, and scenario diversity. These methods frequently lack generalizability, requiring retraining for new environments, and are vulnerable to factors like lighting changes and complex backgrounds, leading to false positives and negatives. To improve reliability, there’s a need for comprehensive, multi-scenario datasets that better reflect real-world conditions and enhance detection accuracy across diverse surveillance scenarios."
%}

{%
  include feature.html
  image="images/about/video-representation.gif"
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
