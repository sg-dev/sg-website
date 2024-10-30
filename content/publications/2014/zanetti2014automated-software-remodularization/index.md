---
title: Automated Software Remodularization Based on Move Refactoring
date: '2014-01-01'
pages: '73-84 '
publishDate: '2021-02-08T11:56:32.678865Z'
authors:
- Marcelo Serrano Zanetti
- Claudio Juan Tessone
- Ingo Scholtes
- Frank Schweitzer
abstract: Modular design is a desirable characteristic of complex software systems
  that can significantly improve their comprehensibility, maintainability and thus
  quality. While many software systems are initially created in a modular way, over
  time modularity typically degrades as components are reused outside the context
  where they were created. In this paper, we propose an automated strategy to remodularize
  software based on move refactoring, i.e. moving classes between packages without
  changing any other aspect of the source code. Taking a complex systems perspective,
  our approach is based on complex networks theory applied to the dynamics of software
  modular structures and its relation to an n-state spin model known as the Potts
  Model. In our approach, nodes are probabilistically moved between modules with a
  probability that nonlinearly depends on the number and module membership of their
  adjacent neighbors. The latter are defined by the underlying network of software
  dependencies. To validate our method, we apply it to a dataset of 39 Java open source
  projects in order to optimize their modularity. Comparing the source code generated
  by the developers with the optimized code resulting from our approach, we find that
  modularity (i.e. quantified in terms of a standard measure from the study of complex
  networks) improves on average by 166+-77 percent. In order to facilitate the application
  of our method in practical studies, we provide a freely available Eclipse plug-in.
publication: 13th International Conference on Modularity
url_pdf: http://dl.acm.org/citation.cfm?id=2584469.2577097
doi: '10.1145/2577080.2577097 '
featured: false
sg-areas:
research: 
- Software Engineering

---
