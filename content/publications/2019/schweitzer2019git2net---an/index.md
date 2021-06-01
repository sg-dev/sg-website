---
title: git2net - An Open Source Package to Mine Time-Stamped Collaboration Networks
  from Large git Repositories
date: '2019-05-01'
pages: 433-444
publishDate: '2021-02-08T11:56:32.330074Z'
authors:
- Frank Schweitzer
- Christoph Gote
- Ingo Scholtes
abstract: Data from software repositories have become an important foundation for
  the empirical study of software engineering processes. A recurring theme in the
  repository mining literature is the inference of developer networks capturing e.g.
  collaboration, coordination, or communication from the commit history of projects.
  Most of the studied networks are based on the co-authorship of software artefacts
  defined at the level of files, modules, or packages. While this approach has led
  to insights into the social aspects of software development, it neglects detailed
  information on code changes and code ownership, e.g. which exact lines of code have
  been authored by which developers, that is contained in the commit log of software
  projects.  Addressing this issue, we introduce git2net, a scalable python software
  that facilitates the extraction of fine-grained co-editing networks in large git
  repositories. It uses text mining techniques to analyse the detailed history of
  textual modifications within files. This information allows us to construct directed,
  weighted, and time-stamped networks, where a link signifies that one developer has
  edited a block of source code originally written by another developer. Our tool
  is applied in case studies of an Open Source and a commercial software project.
  We argue that it opens up a massive new source of high-resolution data on human
  collaboration patterns.
publication: Proceedings of the 16th International Conference on Mining Software Repositories
url_pdf: https://dl.acm.org/citation.cfm?id=3341954
doi: 10.1109/MSR.2019.00070
featured: false
projects:
- Data Science
---
