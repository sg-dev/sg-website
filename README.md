# SG Website

This repository contains the sg-website's content


## Creating local Copy

The website consists of two repositories:

1. the sg-website repository, which contains the **content**
2. the eth-hugo repository, which contains the **theme** of the website, i.e., HTML, JS, CSS, Hugo etc

If you want add content to the website it is best to clone this repository and add content with your favourite editor and push the changes.

To get a working copy of the website you my run the following command:

```bash
git clone --recursive git@github.com:sg-dev/sg-website.git
```
This command will download the current website's content and place a copy of the `eth-hugo` theme in the correct place.

**Note:** To use the above command you need to have `ssh` access to github (not `http`). Please follow these [instructions] if you have not yet done so.

### Ad a news post
To add a news article, for example, you would then invoke hugo as follows.

```bash
hugo new news/cfp-social-science-2021.md
# edit the content add missing info etc.
# save
```

To test if the website combiles and to see how the post will be rendered run the test server as follows:

```bash
hugo server -D 
```

 Note the -D flag means that also content marked with `draft: true` will be included.
 The deployed website **does not include drafts**.
 Drop the `-D` if you want to see the website rendered with drafts.
 
 
[instructions]: https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account
