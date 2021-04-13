---
featured_image: 110000511_page9_gesetze_regular.jpg
title: "Summary Documents and the Secrets they Hold -- Part 1"
description: "Find out what information can be extracted from summary documents provided by the Swiss Parliament."
date: 2021-04-13
featured: true
projects: 
  - 130-years-Swiss-Parliament
---

One of our main data sources for our Project *130 Years of Swiss Parliament* ([click here for the project overview](https://www.sg.ethz.ch/projects/130-years-swiss-parliament/)) are so-called summary of proceedings documents. The Amtliches Bulltin publishes summary documents (dt. *Übersicht der Verhandlungen* or summary of proceedings) for each parliamentary session. These documents contain a list of proposed bills by the members of parliament along with additional information (date of submission, bill text, committee assignments, co-sponsorship, and dates of important decisions).

One of the main tasks of our project is extracting all relevant information in these summary documents and structuring them in a relational database. 

The following entities are extracted for each bill listed in the summary documents: 

* bill number, identifier
* bill title
* date of submission
* bill text
* committee assignments (for NR and SR)

The following entities are recorded in the summary documents, but are not (yet) extracted:

* dates of important decisions (no need yet)
* whether or not the bill is recorded in the AB (no need yet)

The following page extract highlights (red) how a certain bill is generally represented in the summary documents.
The text boxes in blue show the different entities that can be separated and extracted. 

![Summary document 110000511, page 9](110000511_page9_gesetze_regular.jpg)

For certain interventions (Motion, Postulat, Interpellation, Anfragen, etc), members of parliament can sign onto bills, i.e., co-sponsor bills. These `Mitunterzeichner` are recorded in the summary documents:

![Summary document 110000507, page 15](110000507_page15_motion_postulate_regular.jpg)

Over the years, the layout of the summary document changed slightly. However, the information recorded has remained relatively stable: 

![Summary document 110001683, page 21](110001683_page21_normal.jpg)


