<h1 align="center">Lab Website Template</h1>
<p align="center"><img height="200" src="https://github.com/greenelab/lab-website-template/blob/master/mascot.png?raw=true"></p>

A customizable, flexible website template for [labs](https://www.greenelab.com/). Includes automatic citations, GitHub tag imports, and more.

## Features

- A **Home** page, where you can highlight the most important things that make your lab special
- A **Research** page, with a full, sorted, searchable list of your published works
- Generate citations **automatically** (using [Manubot](https://manubot.org)) from just an identifier (DOI, PubMed ID, and many more)
- A **Resources** page, where you can show off your software, datasets, or other useful tools
- Pull in and display tags from GitHub repositories automatically
- Individual team member pages with bios, assignable roles, and social media links
- A **Team** page, compiled automatically from individual members
- A **Join the team** page, where you can put job listings and outreach
- A **Blog** page, with dated and tagged posts about anything
- A **Contact** page, where you can specify all the routes for communicating with your lab
- Social media links to Twitter, Instagram, and Google Scholar
- Several useful pre-built components for things like figures w/ captions, image galleries, and more
- Fully customizable, so you can include things like your vision statement, your approach to research, and more

_The main goal of this template is to allow you to spend less time learning and fussing with web technologies, and more time running your lab._

## Target audience

## Basic primer

Many tutorials take a lot of background knowledge for granted, which can lead to frustration for new users just trying to accomplish something quickly.
To help you interpret the rest of this readme, here are some (very quick and basic) definitions you should know.

- A **repository** (or repo for short) is a place to store code for a project
- **[Git](https://git-scm.com/)** is a [command line tool](https://en.wikipedia.org/wiki/Command-line_interface) for and way of tracking changes to code.
  If you don't have experience using git or your operating system's command line, this template might not be for you, unless you're [willing to learn](https://try.github.io/)!
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
- **[Jekyll](https://jekyllrb.com/)** is a tool written in [Ruby](https://www.ruby-lang.org/en/) that can automatically generate large HTML sites from much simpler markdown, and with less grunt work and code duplication, allowing you to focus on the content.
  Jekyll has many useful features that you'll see throughout this readme.
  It also integrates very nicely with GitHub Pages, so almost no set up is required.
  One important thing to note is that Jekyll runs as a "pre-process" step.
  The seemingly "dynamic" things you'll see Jekyll do happen before you upload the site, not when the user opens the site.
  You make a change to the site content, Jekyll "compiles" the full site, then you upload the full site.
- **[Liquid](https://shopify.github.io/liquid/)** is a [templating language](https://en.wikipedia.org/wiki/Template_processor) that allows you to insert repetitive chunks of content automatically and define logic for how your site is built by Jekyll.
  For example, you can provide Jekyll with a simple list of items, then use Liquid to sort them and [automatically](https://shopify.github.io/liquid/tags/iteration/) put each one in their own table row.
  This is much better than having to type them all out manually, and re-sort them yourself any time you add or remove one.
  You can almost think of Liquid as (a much more limited) JavaScript for Jekyll, except that Jekyll still outputs a static, complete file at the end.

## How do I start my own copy of this template?

1. [Make a GitHub account](https://github.com/join)
2. [Create a new repo under your account from this template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).
   We recommend naming your repository `yourlabname-website`, or `yourlabname.com` if you're going to buy a custom domain.
   Leave `Include all branches` unchecked.

## How do I edit a file?

1. Edit the file [through the GitHub website](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)

OR

1. Edit the file [with Git](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line) on your computer

## How do I publish my site?

1. [Turn on GitHub Pages](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) in the settings of the repo
2. Go where GitHub shows you that your site is published.
   If you haven't bought a custom domain, it will be at `https://[your-user-name].github.io/the-repo-name/`.

### How do I hook up my site to a custom domain (e.g. theawesomelab.com)?

Follow the instructions [here]([Point the service you chose to GitHub Pages](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain).
Summarized:

1. Purchase a domain name from a reputable service, such as Google Domains, Namecheap, etc.
2. Point your domain name provider to GitHub Pages using an `A` record.
   It's slightly different for each company, so they should have their own instructions on how to do this.
3. Set the custom domain field in the settings of the repo.

## Template contents

Where to look for specific features and files.

## I need help!

There are a lot of different technologies involved in this template, it's okay if you don't have a deep understanding of them all.
If you need help or have a suggestion for how to make this template easier to understand or use for novice users, please let us know by [making a GitHub account](https://github.com/join) and [posting an issue on this repository](https://github.com/greenelab/lab-website-template/issues).
