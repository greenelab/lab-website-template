<h1 align="center">Lab Website Template</h1>
<p align="center"><img height="200" src="https://github.com/greenelab/lab-website-template/blob/master/mascot.png?raw=true"></p>

An easy-to-use, flexible website template for [labs](https://www.greenelab.com/), with automatic citations, GitHub tag imports, pre-built components, and more.
Spend less time reinventing the wheel, and more time running your lab.

[**⭐ See the demo ⭐**](https://greenelab.github.io/lab-website-template/)

## Target audience

People who run labs and have some familiarity with GitHub and web technologies.
In other words, people who need [these features](#features) and have [this background knowledge](#background-knowledge).

## Features

- **Automatically generated citations** (using [Manubot](https://manubot.org)) from **just an identifier** (DOI, PubMed ID, and many more)
- Automatically pull in and display tags from GitHub repositories
- Works and looks good on all major desktop and mobile browsers
- A suite pre-built components: social media links, figures w/ captions, image galleries, tags, member portraits, and much more
- Fully and easily customizable
- A **Home** page, where you can highlight the most important things that make your lab special
- A **Research** page, with a full, sorted, searchable list of your published works
- A **Resources** page, where you can show off your software, datasets, or other useful tools
- Individual team member pages with bios, assignable roles, and social media links
- A **Team** page, compiled automatically from individual members
- A **Blog** page, with dated and tagged posts about anything
- A **Contact** page, where you can specify all the routes for communicating with your lab

## Background knowledge

Here are some (very basic) definitions to help you interpret the rest of the readme.
If you aren't already somewhat familiar with these, this template might not be for you.
That said, the template tries to make things as simple as possible, and if you're willing to learn, you should still be able to use it.

- A **repository** (or repo for short) is a place to store code for a project
- **[Git](https://try.github.io/)** is a [command line tool](https://en.wikipedia.org/wiki/Command-line_interface) for and way of tracking changes to code.
- **[GitHub](https://github.com/)** is an online place to store, view, track, share, and collaborate on code.
  You can make simple changes to your code on the GitHub website itself, but for most changes you'll need to use [Git](https://git-scm.com/).
- **[GitHub Pages](https://pages.github.com/)** (or gh-pages for short) is a service built-in to GitHub that can host a website for you, for free.
  No need to buy monthly hosting from GoDaddy or the like!
  Put the source code for your website in a repo, turn on GitHub Pages, and the site will go live.
  Any changes you make to the code will update on the site automatically.
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)** is how you write the main content of a web page.
  It tells the browser what to show, like paragraphs of text, tables of numbers, images with captions, etc.
- **[Markdown](https://en.wikipedia.org/wiki/Markdown)** is a easier way to write certain [basic things from HTML](https://commonmark.org/help/).
  But browsers can't display markdown directly; it has to be converted to HTML first.
- **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)** is how you get a web page to look that way you want it.
  You can set [positions, margins, colors, fonts, etc.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#Keyword_index), and apply them to certain elements in the HTML with [selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors).
  CSS can be confusing and painful, so this template tries to avoid exposing you to it as much as possible.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)** (or JS for short) is a programming language to make web pages more interactive.
  HTML is static, what-you-see-is-what-you-get, but JavaScript allows the page to change dynamically as the user is viewing it.
  For example, JavaScript can hide/show certain paragraphs in the HTML based on what the user types into a search box.
- **[Jekyll](https://jekyllrb.com/)** is a tool that can automatically generate large HTML sites from much simpler markdown, and with less grunt work and code duplication, allowing you to focus on the content.
  Jekyll has many useful features that you'll see throughout this readme.
  It also integrates very nicely with GitHub Pages, so almost no set up is required.
  One important thing to note is that Jekyll runs as a "pre-process" step.
  The seemingly "dynamic" things you'll see Jekyll do happen before you upload the site, not when the user opens the site.
  You make a change to the site content, Jekyll "compiles" the full site, then you upload the full site.
- **[Liquid](https://shopify.github.io/liquid/)** is a [templating language](https://en.wikipedia.org/wiki/Template_processor) that allows you to insert repetitive chunks of content automatically and define logic for how your site is built by Jekyll.
  For example, you can provide Jekyll with a simple list of items, then use Liquid to sort them and [automatically](https://shopify.github.io/liquid/tags/iteration/) put each one in their own table row.
  This is much better than having to type them all out manually, and re-sort them yourself any time you add or remove one.
  You can almost think of Liquid as (a much more limited) JavaScript for Jekyll, except that Jekyll still outputs a static, complete file at the end.
- **[Ruby](https://www.ruby-lang.org/en/)** is a general-purpose programming language.
  It isn't necessary to know any Ruby to use this template, but you'll encounter a few [Ruby-related files](https://www.rubyguides.com/2018/09/ruby-gems-gemfiles-bundler/) because Jekyll is built on Ruby.

## Contents

Where to look for specific features and files.

## FAQ's

### How do I start my own copy of this template?

1. [Make a GitHub account](https://github.com/join)
2. [Create a new repo under your account from this template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).
   We recommend naming your repository `yourlabname-website`.
   Leave `Include all branches` unchecked.

### How do I edit my site?

[Find the item you want to edit](#contents), then:

1. Edit the file [through the GitHub website](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)

OR

1. Edit the file [with Git](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line) on your computer

### How do I see and test changes on the GitHub website?

1. [Make a Netlify account](https://app.netlify.com/signup) for your organization
2. [Hook up Netlify to your repo](https://docs.netlify.com/configure-builds/get-started/#basic-build-settings)
3. [Make a pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) to your repo, and a live preview website of the changes will be automatically built and [shown in the pull request](https://docs.netlify.com/site-deploys/notifications/#github-commit-statuses)

### How do I see and test changes on my computer?

1. [Install Ruby](https://www.ruby-lang.org/en/documentation/installation/)
2. [Install RubyGems](https://rubygems.org/pages/download)
3. [Install Jekyll](https://jekyllrb.com/) by running `gem install bundler jekyll`
4. In your command line, go to the folder where you cloned your site
5. Start the site by running `bundle exec jekyll serve --livereload`
6. Open the "server address" it gives you (eg. `http://127.0.0.1:4000/lab-website-template/`) in a browser
7. Any changes you make will automatically rebuild the site and refresh the page, except for changes to `_config.yml` which require r-erunning the serve command

### How do I publish my site?

1. [Turn on GitHub Pages](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) in the settings of the repo
2. Go where GitHub shows you that your site is published.
   If you haven't set up a custom domain, it will be at `https://your-org-name.github.io/the-repo-name/`.

### How do I hook up a custom domain (e.g. www.theawesomelab.com)?

Follow the instructions [here](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain).

Summarized:

1. Purchase a domain name from a reputable service, such as Google Domains, Namecheap, etc.
2. Point your domain name provider to GitHub Pages using an `A` record.
   It's slightly different for each company, so they should have their own instructions on how to do this.
3. Set the custom domain field in the settings of the repo.

## Acknowledgments

All included photos are licensed under [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/), found using [Creative Commons Search](https://search.creativecommons.org/).

## Support

There are a lot of different technologies involved in this template, it's okay if you don't have a deep understanding of them all.
If you need help or have a suggestion for how to make this template easier to understand or use for novice users, please let us know by [making a GitHub account](https://github.com/join) and [posting an issue on this repository](https://github.com/greenelab/lab-website-template/issues).
