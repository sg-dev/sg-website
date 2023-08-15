# SG Website

[![github pages](https://github.com/sg-dev/sg-website/actions/workflows/deploy_with_hugo.yml/badge.svg?branch=main)](https://github.com/sg-dev/sg-website/actions/workflows/deploy_with_hugo.yml)

This repository contains the content of the website served at https://www.sg.ethz.ch

Here is an overview of how to work with this website.

Things to note:

- The website is static
- The content is generated with Hugo
- Content management is done via `git`
- Only changes pushed to the `main` branch are published
- You should learn the basics of `git` before adding content
- If something goes wrong (e.g. CSS breaks), it is easy to roll back to an earlier version of the website by reverting the commit and recommit.
- If there is a red cross next to the commit hash, it means that there the deployment did not succeed. Email LV for help.


## Setting Environment


The website consists of two repositories:

1. the [sg-website] repository, which contains the **content**.
2. the [eth-hugo] repository, which includes the **theme** of the website, i.e., HTML, JS, CSS, Hugo etc

If you are not interested in the layout, you do not need to consider `eth-hugo`.

There are two basic ways to change content on the website:

1. Directly on Github, by editing the relative markdown in the `content` directory and
2. Locally on your machine.

Option 1 is ideal for quick fixes and minor changes, but if you want to add a new piece of content (possibly with pictures), it is easier to do so locally.
To set up the local development environment (i.e., copy of the website), proceed as follows clone this repository using the following command (note the `--recursive` flag). This command will download the current web site's content and place a copy of the `eth-hugo` theme in the correct place.

```bash
git clone --recursive git@github.com:sg-dev/sg-website.git
```

**Note:** To use the above command, you need to have `ssh` access to GitHub (not `http`). Please follow these [instructions] if you do not have an ssh key yet set on Github.

To get future theme updates locally, you should also run the following command, which will make sure that upon pull also `eth-hugo` will be updated.

```bash
git config submodule.recurse true
```


[sg-website]: https://github.com/sg-dev/sg-website
[eth-hugo]: https://github.com/sg-dev/eth-hugo


## Test preview changes before pushing/publishing

To test if the website compiles correctly, and see how Hugo will render the post on the web, run the following command:

```bash
hugo server -D
```

Which will print the following:

```plain
                   | EN
-------------------+------
  Pages            | 327
  Paginator pages  |  25
  Non-page files   | 842
  Static files     |  71
  Processed images | 290
  Aliases          |   4
  Sitemaps         |   1
  Cleaned          |   0

Built in 1153 ms
Watching for changes in /Users/lucaverginer/Research/Other/sg-website/{archetypes,content,static,themes}
Watching for config changes in /Users/lucaverginer/Research/Other/sg-website/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```
To see the website then open in your brower http://localhost:1313 or http://127.0.0.1:1313.

Note the `-D` flag means that also Hugo will include content marked with `draft: true` (in the frontmatter).
The deployed website **does not include drafts**.
Drop the `-D` if you want to see the website as shown on the web.


[instructions]: https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account


If you are happy with your addition, add all required files for the new post, commit the changes, and push GitHub (on the `main` branch).

Hugo will recompile the website, and if there are no errors, your new content should be visible within a minute or two.


## Adding Content (Basics)

Adding content in Hugo is done by creating a markdown file (ending in `.md`) in the relative `content/*` directory.

Again there are two ways to add such a markdown file:

- Create it manually:
	by creating a `*.md` file in the relative content directory (e.g. `content/news/` or `content/team/`) and add manually the front matter (the stuff between `---` at the top of the '.md' files).
	Sice, the frontmatter varies across content types (i.e. `news`, `team`, `publication`) you can look at the possible values to include in `archetypes/<content-type>.md`.

- Create it with `hugo`:
	You can automatically have `hugo` include the correct frontmatter defined in `archetypes/` by creating a new post with:

```bash
# as a single MD file (i.e. no pics/pdfs or similar placed with it)
hugo new news/simple-post.md
# will create the file `content/news/simple-post.md`
# with the title: Simple Post and a creation date
# Note: you need to run the commands from root, not content directory

# For a more comlex post with dedicated files
# i.e. you want to keep all the files of the post with the post
hugo new news/bundle-post/index.md
mv featured.png news/bundle-post/  # optional
# will create the file `content/news/bundle-post/index.md`
```

Note that both adding a post as `title.md` or as `title/index.md` has no effect on the rendering. It is merely a way to organize content.
You are encouraged to place pdfs, images etc., in with the post because it makes it easier to reuse and find the relative media.


## Featured and Pinned Posts

To add your post to the front page you can set the `feature: true` in the frontmatter of the markdown file.
This means that the post will be shown as a card on the first page.
Note that only the last 9 posts marked as featured will be shown (this can be changed in `config.toml`).

If you have post which should be shown regardless of publication you can **pin** it by setting `pin: true` in the frontmatter.
This means that it will be shown before the featured content.
Note also here that only 3 pinned posts are possible (this can be changed in the `config.toml`).



## Adding Pictures

To include pictures in a post, you use the standard markdown syntax.

```markdown
<!-- linking to pictures with an URL -->
![A description](https://link.to-place.on/the/internet.png)

<!-- or to pictures from our website (relative to post) -->
<!-- .i.e. in the same directory -->
![A description](my_pic.png)

<!-- or a picture in the `static/images/mypic.png` directory -->
![A description](/images/mypic.png)
```

**Remember** to add the picture in the commit. Otherwise, Hugo will not push it to the website.

## Adding News: Guidelines

When you create a new news post you should adhere to the following guidelines.
These will ensure a) a more readable home page, and b) more informative news.

1) Use a short informative title.
   Try to make it a one liner when cards are at their maximum width.
   **Do not simply paste the title of your paper**, that can be already accessed through the publication page.
2) Always add a short description. It will be automatically cut if it exceeds 100 characters.
3) Remember that the description will not automatically show on the post webpage.
   You may need to rewrite it in the main content.
4) Always add an image.


## Adding publications

To add publications use the script available in `scripts/create_pub_md.py`

you may need install these packages before with pip

```bash
pip install ruamel.yaml
pip install bibtexparser
```

then run

```bash
python scripts/create_pub_md.py my-bibfile.bib content/publications/
# Remember to add to content/publications/cite-key/:
#  1. a figure
#  2. a PDF of the paper
```

This will create the directory `content/publications/cite-key/` containing:

```plain
content/publications/cite-key/
├── index.md
└── reference.bib
```

To add a picture and a pdf of the file, place them in the same directory and Hugo will create a thumbnail and create a link to the pdf.

The folder structures should then look like this:

```plain
content/publications/cite-key/
├── PUBLICATION.pdf
├── index.md
├── PICTURE.png
└── reference.bib
```

To add additional text to the publication, e.g., where to find the code or if it has been mentioned on the news, you can add this in the `index.md` as content. This text will be shown above the abstract.


For the button `Official Link` to appear either of the following two fields must be set: `doi` or `url_pdf`. `doi` will take precedence as it is a permanent identifier and the preferred link type. However, sometimes a DOI is not available, in which case you should use `url_pdf`.
As soon as you do have a valid `doi` add it, this will make the linking more robust.


## Updating a publication

If you want to update the details of a publication, e.g., it has been published. There are two ways to do this.

### Reuse the existing directoty

If nothing major has changed except, DOI and year may simply

- [ ] move the directoy with the publication to its new location (if necessary)

	```bash
	mv content/publications/<YEAR-OLD/<cite-key> content/publications/<YEAR-NEW/<cite-key>
	```

- [ ] change the details in the `index.md` file, **note that the `date` must be updated**

	```yaml
	publication: Scientific Reports
	date: 2021-05-01
	DOI: <NEW-DOI>
	```

- [ ] update the `reference.bib`
- [ ] (if new) replace the PDF
- [ ] (if new) update the figure


### Completely replace the directory (preferred)

If on the other hand there are some major changes the following:

- [ ] note down if the old pubolicatio `index.md` had any special content, i.e., `projects` or custom text
- [ ] run the dedicated python script

	```bash
	python scripts/create_pub_md.py ref.bib content/publications/
	```
- [ ] Add as suggested the new PDF and picture
- [ ] (if any) add `projects` and custom text back
- [ ] *Delete* the old directory with the old publication (so there are no duplicates).



## Adding a new Team member

To create a page for a new team member, use Hugo as follows:

```bash
Hugo new team/FIRSTNAME-LASTNAME/index.MD
```

Add a picture with the name `profile_pic` in the same directory and optionally a file CV in pdf format. This file must be named `CV.pdf`.




## Projects

You can classify a post/publication as belonging to a specific project by adding their name in the frontmatter.

For example, a publication related to the "Alphorn" project should have the following keys in the front matter of the markdown.

```yaml
---
...
projects:
  - Alphorn
---
```


For projects which are composed of multipe words for example `Science of Science` you can use exactly this string in the frontmatter like so

```yaml
---
...
projects:
  - Science of Science
---
```

internally this `Science of Science` will be reduced to `science-of-science` and the url containing the project defition will be `sg.ethz.ch/projects/science-of-science/`.

The reason to write it in upper case and with spaces is that it more readable when it is listed on the publication or news item.




Note that you can add these keys also to posts of type news, and they will be listed under the respective areas and projects.

To highlight that a project is funded by an agency you can do so by adding in the front matter of a project site (e.g., `content/projects/130-years-swiss-parliament/_index.md`) the following yaml tags

```yaml
---
...
label: Funded by SNF
---
```


## Creating an Event on Our Hugo-Based Website

### Introduction

This guide provides step-by-step instructions for creating and managing events on our Hugo-based website. Each event can be composed of multiple talks, including breaks.

**Prerequisites:** Basic understanding of YAML syntax and a working Hugo environment.

### How to Create an Event

#### Step 1: Create a New Event File

Create a new file with a descriptive name, like `sg-symposium-april-2023.md`, in the `content/events` directory. This filename becomes the identifier of the event, used to link talks to this event.

#### Step 2: Add the Necessary Frontmatter

In the event file, add the following frontmatter:

```yaml
featured_image: bg.png
title: "Exploring the Hidden Knowledge Space: Ideas, Patents, People"
description: SG Symposium
date: 2023-03-15
from: "2023-04-04T08:45:00"
to: "2023-04-04T12:00:00"
where: "ETH Zurich, WEV, Room F111"
label: SG Symposium
aliases:
    - /SG-Symposium2023/
    - /sg-symposium-knowledge/
```

**Note on Featured Image:**
Name the `featured_image` file for the event's background as `bg.*` (e.g., `bg.png`). This naming ensures that the image is used as the background for associated talks, creating a visual theme across all talks belonging to an event.

**Fields Explanation:**

| Field           | Required/Optional | Description                                           | Example                                          |
|-----------------|-------------------|-------------------------------------------------------|--------------------------------------------------|
| `featured_image`| Required          | Image file for the event's background                 | `bg.png`                                         |
| `title`         | Required          | Full title of the event                               | "Exploring the Hidden Knowledge Space: Ideas, Patents, People" |
| `description`   | Required          | Short description of the event                        | "SG Symposium"                                   |
| `date`          | Required          | Publishing date of the event in `YYYY-MM-DD` format   | `2023-03-15`                                     |
| `from`          | Required          | Starting time of the event in ISO format `YYYY-MM-DDTHH:MM:SS` | `2023-04-04T08:45:00`                     |
| `to`            | Required          | Ending time of the event in ISO format `YYYY-MM-DDTHH:MM:SS` | `2023-04-04T12:00:00`                     |
| `where`         | Required          | Location of the event                                 | "ETH Zurich, WEV, Room F111"                    |
| `label`         | Optional          | A label added at the top of the event page            | "SG Symposium"                                   |
| `aliases`       | Optional          | Alternate URLs redirecting to the event page          | `/SG-Symposium2023/`                             |

### How to Create the Program

#### Step 1: Organize Talks

Create a directory in `content/talks/<short-name>` to group all talks belonging to a given event.

#### Step 2: Add Talks to the Program

To associate a talk with your event, add the event identifier to the `events` key in the talk's frontmatter. Follow the instructions in the "How to Add a Talk" section below.

#### Step 3: Schedule Coffee and Lunch Breaks

To add coffee and lunch breaks, create a "talk" file in the same directory where all the talks belonging to a specific event are listed. These "break" talks have a special `cbreak: true` field in the frontmatter, differentiating them from regular talks.

Example of a coffee break frontmatter:
```yaml
title: "Coffee Break"
from: 2023-04-04T10:45:00
to: 2023-04-04T11:15:00
events:
- sg-symposium-april-2023
cbreak: true
```

**Note on Event Naming:**
The `<event-name>` identifier can be spelled with or without dashes (`-`), and in upper or lower case. Hugo will correctly match talks and events regardless. Removing the dashes makes the event name more legible in the talks view, as this name is taken directly from this key. For example, both `sg-symposium-april-2023` and `SG Symposium April 2023` are valid and will work.

### How to Add a Talk

#### Step 1: Create a Directory for the Talk

In `content/talks/<event-name>` or `content/talks/<year>`, create a subdirectory to organize the talks.

#### Step 2: Create a Talk File

In the created directory, create a new file named after the talk, e.g., `data-science-knowledge-graphs.md`.

#### Step 3: Add the Necessary Frontmatter



In the talk file, add the following frontmatter:

```yaml
title: "Data Science on Knowledge Graphs: From Complex Data to Network Models"
date: 2023-04-02
draft: false
featured: false
featured_image: giona.png
description: "An in-depth look at knowledge graphs."
speaker: Giona Casiraghi
affiliation: Chair of Systems Design, ETH Zürich
where: LEE E 101
from: 2023-04-04T10:00:00
to: 2023-04-04T10:45:00
events:
- sg-symposium-april-2023
```

#### Step 4: Write the Talk Content

Below the frontmatter, write the content of the talk, starting with an abstract, like this:

```
---
title: ...
...: ...
---

### Abstract

This is the abstract text for this talk.

```

#### Step 5: Verify the Talk

After saving the file, verify that the talk appears in the correct event and in the `/talks` list view on the website. Build the site locally and preview it to ensure everything is set up correctly.

### Linking to the Event from the Front Page

#### Step 1: Create a New News Item

In the `content/news` directory, create a new file with similar frontmatter as below:

```markdown
---
title: "Nov 24 — SG Symposium: The Complex Network Approach to Data Science"
date: 2022-11-14T13:36:19+01:00
draft: false
featured: true
featured_image: bg.png
description: On November 24, join us in LEE E 101. Click to check out the program.
---

<meta http-equiv="refresh" content="0;URL='/events/sg-symposium-november-2022/'">
```

**Important Fields:**
- `featured: true`: Flag to list the item on the front page.
- `featured_image`: Add this image to the same directory as this news item.
- `<meta>` redirect tag: Replace the URL with the target root page of the event.

### Common Errors

1. **Wrong Name of Event:** Ensure the `events` key in the talk's frontmatter matches the event identifier exactly.
2. **Missing Image:** If the `featured_image` in the frontmatter is missing or the filename is incorrect, you will get an `$image.Fill` error. Double-check the image filename and its location.
