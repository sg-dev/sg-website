# SG Website

[![github pages](https://github.com/sg-dev/sg-website/actions/workflows/deploy_with_hugo.yml/badge.svg?branch=main)](https://github.com/sg-dev/sg-website/actions/workflows/deploy_with_hugo.yml)

This repository contains the content of the website served at https://www.sg.ethz.ch.

Here is an overview of how to work with this website.

Things to note:

- The website is static
- The content is generated with Hugo
- Content management is done via `git`
- Only changes pushed to the `main` branch are published
- You should learn the basics of `git` before adding content
- If something goes wrong (e.g., CSS breaks), it is easy to roll back to an earlier website version by reverting the commit and recommit.
- If there is a red cross next to the commit hash, it means that there the deployment did not succeed. Email LV for help.


## Setting Environment


The website consists of two repositories:

1. the [sg-website] repository contains the **content**.
2. the [eth-hugo] repository, which includes the **theme** of the website, i.e., HTML, JS, CSS, Hugo.

If you are not interested in the layout, you do not need to consider `eth-hugo`.

There are two basic ways to change content on the website:

1. Directly on Github, by editing the relative markdown in the `content` directory and
2. Locally on your machine.

Option 1 is ideal for quick fixes and minor changes, but if you want to add a new piece of content (possibly with pictures), it is easier to do so locally.
To set up the local development environment (i.e., copy of the website), clone this repository using the following command (note the `--recursive` flag). This command will download the current website's content and place a copy of the `eth-hugo` theme in the correct place.

```bash
git clone --recursive git@github.com:sg-dev/sg-website.git
```

**Note:** To use the above command, you must have `ssh` access to GitHub (not `http`). Please follow these [instructions] if you still need to set up an ssh key on GitHub.

To get future theme updates locally, you should also run the following command, which will ensure that, upon pull, `eth-hugo` will also be updated.

```bash
git config submodule.recurse true
```


[sg-website]: https://github.com/sg-dev/sg-website
[eth-hugo]: https://github.com/sg-dev/eth-hugo


## Test preview changes before pushing/publishing

To test if the website compiles correctly and see how Hugo will render the post on the web, run the following command:

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
To see the website, then open your browser http://localhost:1313 or http://127.0.0.1:1313.

Note that the `-D` flag means that also Hugo will include content marked with `draft: true` (in the frontmatter).
The deployed website **does not include drafts**.
Drop the `-D` if you want to see the website as shown on the web.


[instructions]: https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account


If you are happy with your addition, add all required files for the new post, commit the changes, and push GitHub (on the `main` branch).

Hugo will recompile the website; if there are no errors, your new content should be visible within a minute or two.


## Adding Content (Basics)

Adding content in Hugo is done by creating a markdown file (ending in `.md`) in the relative `content/*` directory.

Again there are two ways to add such a markdown file:

- Create it manually:
	By creating a `*.md` file in the relative content directory (e.g., `content/news/` or `content/team/`) and adding the front matter (the stuff between `---` at the top of the '.md' files) manually.
	Since the frontmatter varies across content types (i.e., `news`, `team`, `publication`), you can look at the possible values to include in `archetypes/<content-type>.md`.

- Create it with `hugo`:
	You can automatically have `hugo` include the correct frontmatter defined in `archetypes/` by creating a new post with:

```bash
# as a single MD file (i.e., no pics/pdfs or similarly placed with it)
hugo new news/simple-post.md
# will create the file `content/news/simple-post.md`
# with the title: Simple Post and a creation date
# Note: You need to run the commands from root, not the content directory

# For a more complex post with dedicated files
#, i.e., you want to keep all the post files with the post
hugo new news/bundle-post/index.md
mv featured.png news/bundle-post/  # optional
# will create the file `content/news/bundle-post/index.md`
```

Adding a post as `title.md` or as `title/index.md` does not affect the rendering. It is merely a way to organize content.
You are encouraged to place pdfs, images, etc., in with the post because it makes it easier to reuse and find the relative media.


## Featured and Pinned Posts

To add your post to the front page, you can set the `feature: true` in the frontmatter of the markdown file.
The post will be shown as a card on the first page.
Only the last nine posts marked as featured will be shown (this can be changed in `config.toml`).

If you have a post that should be shown regardless of publication, you can **pin** it by setting `pin: true` in the front matter.
This means that it will be shown before the featured content.
Only 3 pinned posts are possible (this can be changed in the `config.toml`).



## Adding Pictures

To include pictures in a post, you use the standard markdown syntax.

```markdown
<!-- linking to pictures with an URL -->
![A description](https://link.to-place.on/the/internet.png)

<!-- or to pictures from our website (relative to post) -->
<!-- .i.e., in the same directory -->
![A description](my_pic.png)

<!-- or a picture in the `static/images/mypic.png` directory -->
![A description](/images/mypic.png)
```

**Remember** to add the picture in the commit. Otherwise, Hugo will not push it to the website.

## Adding News: Guidelines

When you create a new news post, you should adhere to the following guidelines.
These will ensure a) a more readable home page and b) more informative news.

1) Use a short informative title.
   Try to make it a one-liner when cards are at their maximum width.
   **Do not simply paste the title of your paper**, which can be already accessed through the publication page.
2) Always add a short description. It will be automatically cut if it exceeds 100 characters.
3) Remember that the description will not automatically show on the post webpage.
   You may need to rewrite it in the main content.
4) Always add an image.


## Adding publications

To add publications use the script available in `scripts/create_pub_md.py`

You may need to install these packages before with pip.

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

To add a picture and a pdf of the file, place them in the same directory, and Hugo will create a thumbnail and a link to the pdf.

The folder structures should then look like this:

```plain
content/publications/cite-key/
├── PUBLICATION.pdf
├── index.md
├── PICTURE.png
└── reference.bib
```

To add additional text to the publication, e.g., where to find the code or if it has been mentioned on the news, you can add this in the `index.md` as content. This text will be shown above the abstract.


For the button `Official Link` to appear either of the following two fields must be set: `doi` or `url_pdf`. `doi` will take precedence as it is a permanent identifier and the preferred link type. However, sometimes a DOI is unavailable, so you should use `url_pdf`.
As soon as you have a valid `doi`, add it; this will make the linking more robust.


## Updating a Publication

If you wish to update the details of a publication, for instance, if it has been published, there are two ways to go about it:

### Reuse the Existing Directory

Should only minor details change, such as the DOI and year:

- [ ] Move the directory containing the publication to its new location (if necessary). Replace `<YEAR-OLD>` and `<YEAR-NEW>` with the relevant years.

	```bash
	mv content/publications/<YEAR-OLD>/<cite-key> content/publications/<YEAR-NEW>/<cite-key>
	```

- [ ] Update the `index.md` details. **Ensure that the `date` is updated**.

	```yaml
	publication: Scientific Reports
	date: 2021-05-01
	DOI: <NEW-DOI>
	```

- [ ] Update the `reference.bib`.
- [ ] Replace the PDF if it is new.
- [ ] Update the figure if it is new.

### Completely Replace the Directory (Preferred)

For major changes:

- [ ] Take note of any particular content in the old publication's `index.md`, like `projects` or custom text.
- [ ] Execute the dedicated Python script:

	```bash
	python scripts/create_pub_md.py ref.bib content/publications/
	```

- [ ] Add the new PDF and image as suggested.
- [ ] Restore `projects` and custom text if they were in the original.
- [ ] **Delete** the directory containing the old publication to avoid duplicates.

---

## Adding a New Team Member

To create a page for a new team member, use Hugo:

```bash
hugo new team/FIRSTNAME-LASTNAME/index.md
```

Place an image named `profile_pic` in the same directory. Ensure the image adheres to standard dimensions or any specific guidelines provided. Optionally, include a CV in PDF format named `CV.pdf`.

---

## Projects

Classify a post or publication under a specific project by including the project's name in the frontmatter:

For single-word projects:

```yaml
---
...
projects:
  - Alphorn
---
```

For multi-word projects, such as `Science of Science`, use the exact string:

```yaml
---
...
projects:
  - Science of Science
---
```

Internally, `Science of Science` will automatically transform to `science-of-science`. The corresponding URL will be `sg.ethz.ch/projects/science-of-science/`.

Using the uppercase format with spaces enhances readability in the publication or news item listing.

You can also tag news posts with these keys, appearing under the relevant project categories.

To indicate that a project is funded by a specific agency (for example, "Funded by SNF"), include this in the front matter of a project site, such as `content/projects/130-years-swiss-parliament/_index.md`:

```yaml
---
...
label: Funded by <AGENCY NAME>
---
```

Replace `<AGENCY NAME>` with the relevant funding agency's name.

---

## Creating an Event on Our Hugo-Based Website


### How to Create an Event

#### Step 1: Create a New Event File

Create a new file with a descriptive name, like `sg-symposium-april-2023/_index.md`, in the `content/events` directory. This name becomes the event's identifier, which links talks to this event.

#### Step 2: Add the Necessary Frontmatter

In the event file, add the following front matter:

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

Create a directory in `content/talks/<short-name>` to group all talks about a given event.

#### Step 2: Add Talks to the Program

To associate a talk with your event, add the event identifier to the `events` key in the talk's front matter. Follow the "How to Add a Talk" instructions below.


#### Step 3: Creating a Session

To introduce a thematic session comprised of multiple talks under a unified topic, create a "session" file within the directory where the event-specific talks are housed. These "session" entries should have a `session: true` field in the frontmatter, distinguishing them from individual talks.

Example of a session frontmatter:

```yaml
title: "Polarization as a Threat to Democracy?"
session: true
draft: false
speaker: Philip Leifeld
affiliation: University of Essex, UK
where:
from: 2023-09-13T11:00:00
to: 2023-09-13T12:30:00
events:
- MMM Workshop September 2023
weight: 1
```

**Note:** The `weight=1` ensures the Session title comes before any talk (Lower numbers are displayed first).



#### Step 4: Schedule Coffee and Lunch Breaks

To schedule coffee and lunch breaks, produce a "talk" file within the directory where talks for the event reside. These "break" talks should have a distinct `break: true` field in their frontmatter, distinguishing them from standard talks.

Here is an example frontmatter for a coffee break:
```yaml
title: "Coffee Break"
from: 2023-04-04T10:45:00
to: 2023-04-04T11:15:00
events:
- sg-symposium-april-2023
break: true
```

#### Step 5: Add Talks to the Program

Link a talk to your event by including the event identifier in the `events` key of the talk's front matter. Consult the "How to Add a Talk" section for instructions.


**Note on Event Naming:**
The `<event-name>` identifier can be spelled with or without dashes (`-`) and in upper or lower case. Hugo will correctly match talks and events regardless. Removing the dashes makes the event name more legible in the talks view, as this name is taken directly from this key. For example, both `sg-symposium-april-2023` and `SG Symposium April 2023` are valid and will work.


### How to Add a Talk

#### Step 1: Create a Directory for the talk

Create a subdirectory to organize the talks in `content/talks/<event-name>` or `content/talks/<year>`.

#### Step 2: Create a Talk File

In the created directory, create a new file named after the talk, e.g., `data-science-knowledge-graphs.md`.

#### Step 3: Add the Necessary Frontmatter


In the talk file, add the following front matter:

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

After saving the file, verify that the talk appears in the correct event and in the website's `/talks` list view. Build and preview the site locally to ensure everything is set up correctly.

### Linking to the event from the Front Page

#### Step 1: Create a New News Item

In the `content/news` directory, create a new file with a similar frontmatter as below:

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

---


## How to Edit the Hugo Theme for the `www.sg.ethz.ch` Website

In order to maintain a clear separation of content and design and also to ensure the privacy of the theme, we have designed the `www.sg.ethz.ch` website using two repositories:

- **www.sg.ethz.ch** (Holds the content of the website)
- **eth-hugo** (The theme of the website)

The `eth-hugo` theme is integrated into the main website using a git submodule. This guide will guide you through editing and updating the theme on the main website.

### Editing the `eth-hugo` Theme

1. **Navigate to the `eth-hugo` Repository**:
   Begin by navigating to the `eth-hugo` repository. Ensure that you are on the `main` branch since this is the branch that the deployed website uses. If you wish to experiment with changes, you can create a new branch and build the website locally. Remember, the deployed website will remain unaffected unless you push changes to the `main` branch.

2. **Make Your Changes**:
   Modify the theme as needed once you have confirmed that the website compiles without errors, you are ready to commit your changes.

3. **Commit Your Changes Locally**:
   Add your edited files to the staging area using `git add <file>` followed by `git commit -m 'Your descriptive message'`. Alternatively, commit all changes using `git commit -a -m 'Your message'`.

4. **Push Changes to GitHub**:
   With your changes committed locally, you can now push them to the online repository with `git push`.

## Updating the Main Website to Use the Edited Theme

1. **Commit Theme Changes to the Main Website**:
   Now, you must let the `www.sg.ethz.ch` website know there is a new theme version to use. While in the `www.sg.ethz.ch` repository, commit the change with `git commit -m 'Updated theme'`. You should see the changed `theme/eth-hugo` being committed.

2. **Push Website Changes**:
   Push the changes of the `www.sg.ethz.ch` repository to GitHub with `git push`.

3. **Verify Deployment**:
   Once you have pushed the changes, check the deployment. Wait about 8 minutes, and ensure no build errors and the website displays correctly.

### Potential Error and Its Solution:
If you encounter a build error relating to a commit or submodule not being available, it is likely you have pushed changes to the `www.sg.ethz.ch` repository that reference the updated theme but forgot to push the `eth-hugo` changes to GitHub. Always push changes to `eth-hugo` before updating the main website repository.
