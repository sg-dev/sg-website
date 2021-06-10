# SG Website

This repository contains the content of the website served at https://www.sg.ethz.ch

Here is an overview of how to work with this website.

Things to note:

- The website is a static
- The content is generated with the Hugo framework
- Content management is done through `git`
- Only changes pushed to the `main` branch are published
- You should learn the basics of `git` before adding content
- If something goes wrong (e.g. CSS breaks), it is easy to roll back to an earlier version of the website by reverting the commit and recommit.



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
Hugo new news/simple-post.MD
# will create the file `content/news/simple-post.md` 
# with the title: Simple Post and a creation date

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
pip install ruaml.yaml
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



