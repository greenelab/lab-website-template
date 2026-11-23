---
title: Vacancy
nav:
  order: 5
  tooltip: Open positions and thesis projects
seo_title: "PhD, Postdoc and MSc Thesis Positions | p4MARS Lab, TU Delft"
seo_description: "Open PhD, postdoc, research assistant and MSc thesis positions in robot perception, SLAM and space robotics at the p4MARS Lab, TU Delft."
---

{% include section.html size="full" %}

{% include page-hero.html title="Vacancy" icon="fa-solid fa-user-plus" %}

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}


{% include section.html %}
## Postdoc Positions

{% include list.html data="posts" component="post-excerpt" filter="Array(tags).include?('postdoc-position')" %}

## PhD Positions

PhD candidates in the lab carry out a four-year research project on Spatial & Agentic Intelligence, Actionable World Models or Evolving Digital Twins, leading to a doctoral thesis at TU Delft. Positions are fully funded employee positions under the Dutch collective labour agreement for universities, and include a limited teaching contribution. Openings are announced here and on the TU Delft vacancy portal.

<details markdown="1">
<summary>Information for interested candidates</summary>

We look for candidates with an MSc in robotics, computer science, mechanical engineering, electrical engineering or a related field, a strong background in perception, machine learning or optimisation, and solid programming skills. A good command of English is required.

Applications normally include your CV, transcripts of your BSc and MSc, a motivation letter explaining why this particular project interests you, and the contact details of two referees. If you have a thesis, publication or code repository that represents your work well, please include a link.

If none of the announced positions matches your interests but you would like to join the group, you are welcome to contact [Prof. Sabzevari](mailto:R.Sabzevari@tudelft.nl) with your CV and a short research statement. We are also glad to support strong candidates applying with their own funding, for example through NWO Mosaic, national scholarship programmes, or the Marie Skłodowska-Curie actions.

</details>

<!-- TODO: please review this draft description -->

{% assign phd_positions = site.posts | where_exp: "p", "p.tags contains 'phd-position'" %}
{% if phd_positions.size == 0 %}
There are no open PhD positions at the moment. New openings are posted here as soon as funding is confirmed.
{% else %}
{% include list.html data="posts" component="post-excerpt" filter="Array(tags).include?('phd-position')" %}
{% endif %}

## RA Positions

Research assistant positions are paid, fixed-term roles for students and recent graduates who want hands-on research experience in the lab. Assistants work alongside our PhD candidates and postdocs on a concrete part of a running project, such as building a demo, preparing datasets or implementing and evaluating methods on real robots. They are usually part-time and run for a few months, and can be combined with your studies.

<details markdown="1">
<summary>Information for interested students</summary>

To apply, send an email to [Prof. Sabzevari](mailto:R.Sabzevari@tudelft.nl) and other contact persons with your CV, your transcript of records, and a short note on why this position interests you and what relevant experience you bring. Please also state how many hours per week you are available and your preferred start date.

</details>

{% include list.html data="posts" component="post-excerpt" filter="Array(tags).include?('ra-position')" %}

## TA Positions

Teaching assistants support the courses taught by members of the lab, mostly in computer vision, machine learning and robotics. The work involves guiding students during lab sessions and tutorials, answering questions on the course forum, and grading assignments together with the teaching team. In Q1 and Q4 of the academic calendar we always look for talented TAs. TA positions are part-time, and are open to BSc and MSc students who have taken the course or an equivalent one.

- **Q1 &middot; [CIEM6306 Advanced Data Science in Engineering Applications](https://studiegids.tudelft.nl/courses/study-guide/educations/37558)** &mdash; supporting student teams across the full data pipeline, from data processing and feature engineering to machine learning and visualization, in a project run with external stakeholders.
- **Q4 &middot; [AE4ASM527 Spatial AI for Industrial Automation](https://studiegids.tudelft.nl/courses/study-guide/educations/21184)** &mdash; supporting the hands-on labs on robot perception and ROS, and the teams building their systems on the MIRTE Master platform.

Both courses are described on the [Education](/education) page. We advise interested students to get in touch in the quarter before the course runs.

<details markdown="1">
<summary>Information for interested students</summary>

To apply, email the contact person listed with the position with your CV, your transcript of records, the grade you obtained for the course (or an equivalent one), and your availability during the quarter in which the course runs. Previous TA experience is welcome but not required.

</details>

<!-- TODO: please review this draft description -->

{% assign ta_positions = site.posts | where_exp: "p", "p.tags contains 'ta-position'" %}
{% if ta_positions.size == 0 %}
No teaching assistant positions are advertised here at the moment. The recurring openings for CIEM6306 (Q1) and AE4ASM527 (Q4) are announced in the quarter before each course starts.
{% else %}
{% include list.html data="posts" component="post-excerpt" filter="Array(tags).include?('ta-position')" %}
{% endif %}

## Master Projects

We offer MSc thesis projects on Spatial & Agentic Intelligence, Actionable World Models and Evolving Digital Twins for automation of highly adaptive tasks in industrial and space robotics. Each project is defined together with your supervisor and combines methodological work with experiments on synthetic data or real robots. Projects can start at any time.

<details markdown="1">
<summary>Information for interested students</summary>

These projects are primarily for students at TU Delft or students from master programs at other European universities. If you are interested please see below the information that we require from you. Students from other European universities are advised to apply for Erasmus+ scholarships. We advise interested students to contact us several months before the intended start date.

All of our MSc Thesis + Literature Survey assignments can be extended with a Research Assignment in the same topic. This is an interesting option for students interested in a longer research experience (e.g. if you would like to publish an article during your MSc thesis or do a PhD afterwards). We do not offer separate Research Assignments - only those linked to an MSc thesis project. You may also choose to do an Internship in a company.

If you do not find an interesting project, but you would like to join our group, or your would like to propose your own project, then, send an email to [Prof. Sabzevari](mailto:R.Sabzevari@tudelft.nl). We can also supervise TUD MSc students in industry or in our partners abroad.
</details>


<details markdown="1">
<summary>How to apply</summary>
Students interested in a MSc project should contact the direct supervisor and provide the following information:
- Why are you interested in this project? What would you like to achieve?
- What is your experience relevant to this project? This could be past projects, past courses; theoretical knowledge or practical experience, related to constrained optimization, planning and/or robotics.
- When would you like to start and which courses will you have left by then?
- Is your motivation to do algorithmic work or applied research?
- Your transcript of record with past courses, including which master & track you are following.
- Available day/times to meet within one/two weeks.
</details>

In the following link you can find a list of available MSc projects. For announced projects, please first contact the daily supervisor to discuss the project.

{% include list.html data="posts" component="post-excerpt" filter="Array(tags).any? { |t| ['master-project'].include?(t) }" %}