<h1 align="center">Lab Website Template</h1>
<p align="center"><img height="200" src="https://raw.githubusercontent.com/greenelab/lab-website-template/main/icons/share-thumbnail.jpg?raw=true" alt="Lab Website Template"></p>

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
- A suite of pre-built components:
  - formatted tables and code blocks
  - social media links with icons
  - figures with captions
  - image galleries
  - multi-size cards with image and text
  - ...and more!
- A **home page**, where you can highlight the most important things that make your lab special
- A **research page**, with a sorted, searchable list of all your published works
- A **blog page**, with a sorted, grouped, tagged list of all your posts
- A **resources page**, where you can show off your software, datasets, or other useful things
- Individual **team member pages** with bios, assignable roles, and social media links
- A **team** page, compiled automatically from individual members

## Background knowledge

Here are some (very basic) definitions to help you interpret the rest of the readme.
If you aren't already somewhat familiar with these, this template might not be for you.
That said, the template tries to make things as simple as possible, and if you're willing to learn, you should still be able to use it fairly easily.

- A **repository** (or _repo_ for short) is a place to store code for a project
- **[Git](https://try.github.io/)** is a way of tracking changes to code in repos through a [command line](https://en.wikipedia.org/wiki/Command-line_interface).
- **[GitHub](https://github.com/)** is an online place to store, view, track, share, and collaborate on code in repos.
  You can make simple changes to your code on the GitHub website itself, but for most changes you'll need to use [Git](https://git-scm.com/).
- **[GitHub Pages](https://pages.github.com/)** (or _gh-pages_ for short) is a service built-in to GitHub that can host a website for you, for free.
  No need to buy monthly hosting from GoDaddy!
  Put the source code for your website in a repo, turn on GitHub Pages, and the site will go live.
  Any changes you make to the code will update on the site automatically.
- **[GitHub Actions](https://github.com/features/actions)** (or _gh-actions_ for short) is a feature of GitHub that can (among other things) automatically run scripts and other actions when changes are made to a repo.
  Setting up GitHub Actions is only needed for certain specific tasks that aren't handled automatically by Jekyll or other parts of the template.
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)** is how you write the main content of a web page.
  It tells the browser what to show, like paragraphs of text, tables of numbers, images with captions, etc.
- **[Markdown](https://en.wikipedia.org/wiki/Markdown)** is a easier way to write certain [basic things from HTML](https://commonmark.org/help/).
  But browsers can't display markdown directly; it has to be converted to HTML first.
- **[Sass](https://sass-lang.com/)** (a superset of [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)) is how you get a web page to look that way you want.
  You can set [positions, margins, colors, fonts, etc](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#Keyword_index), and apply them to certain elements (tables, images, etc) in the HTML with [selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors).
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)** (or _js_ for short) is a programming language to make web pages more interactive.
  HTML is static/unchanging, but JavaScript allows the page to change dynamically as the user is viewing it.
  For example, JavaScript can be used to hide/show certain paragraphs in the HTML based on what the user types into a search box.
- **[Jekyll](https://jekyllrb.com/)** is a tool that can automatically generate large HTML sites from much simpler markdown, and with less grunt work and code duplication, allowing you to just focus on the content.
  It does all this fancy work in a "pre-process" step, before you view the site.
  When you make a change, Jekyll compiles everything together into the final product which can then be viewed or uploaded.
  Jekyll also integrates very nicely with GitHub Pages, so almost no set up is required.
- **[Liquid](https://shopify.github.io/liquid/)** is a [templating language](https://en.wikipedia.org/wiki/Template_processor) built-in to Jekyll that allows you to insert repetitive chunks of content automatically and define logic for how your site is built by Jekyll.
  For example, you could provide Jekyll with a simple list of items, then use Liquid to sort them and [automatically](https://shopify.github.io/liquid/tags/iteration/) put each one in their own formatted table row.
  You can almost think of Liquid as (a much more limited) JavaScript for Jekyll, except that it still results in a static file at the end.
- **[Ruby](https://www.ruby-lang.org/en/)** is a general-purpose programming language.
  You don't need to know Ruby to use this template, but you'll encounter a few [Ruby-related files](https://www.rubyguides.com/2018/09/ruby-gems-gemfiles-bundler/) in the template, because Jekyll is written in Ruby.
- **[Python](https://www.python.org/)** is a general-purpose programming language.
  You don't need to know Python to use this template, unless you want to understand or modify the behavior of [the automatic citations](#automatic-citations).

## Contents

An overview of the contents of this template and basic notes on how to edit and use them.

### Your files and folders

Files and folders to be edited by you.

- `/blog`, `/contact`, etc - A sub-folder to create in the resulting site, eg `yoursite.com/blog`.
  You can name a folder anything you want, put an `index.md` in it, and link to it like any other page.
- `/_data` - A place to put large, ordered lists of data that don't need individual generated pages.
  Your `research` and `resources` content live here.
- `/_members` - Where your team member bios go.
  Member bios can include a photo, role (researcher/programmer/etc), group (current/alumni/etc), and social media links.
  Each file will automatically generate its own page.
- `/_posts` - Where your blog posts go.
  Name your post files in the format `YYYY-MM-DD-your-post-title.md`.
  Each file will automatically generate its own page.
- `/icons` - Icons for when your site is bookmarked in a browser, added as an app shortcut on a phone, and shared on social media.
  These are important!
  Replace these images with variations of your own logo, taking care to match the size and cropping.
  They can be transparent, but make sure they can be distinguished on any background, dark or light.
  [realfavicongenerator.net](https://realfavicongenerator.net/) can help you generate all the necessary icon variations, but it goes overboard with its support for unused legacy browsers like Internet Explorer.
  What's included in this template is a simplified subset that works fine on all of the most common modern browsers.
- `/images` - A default folder to hold all your site's images.
  You can organize and place your images however you want though.
  For example, you could put photos of your team in `/team/photos/` and just refer to them like `team/photos/anna-sun.jpg`.
- `_config.yml` - The main Jekyll configuration for your site.
  Contains important site-wide things like the site title, the site url, the default email/twitter/etc, the default background image, etc.
- `404.md` - A fallback page for when a user goes to a page that doesn't exist on your site.
- `index.md` - The landing/"home" page for your site.
- `start.sh` - A convenient script to start and open the site on your computer.
  Run like `./start.sh`.

#### General editing notes

- Naming a file `index` is a web convention for referring to the "main" page of a particular folder.
  For example, `yoursite.com/join` actually takes you to `/join/index.html` (generated from `/join/index.md`), and `yoursite.com` takes you to the root `index.html` (generated from `index.md`).

- Liquid has [special syntax to trim whitespace](https://shopify.github.io/liquid/basics/whitespace/) on either side of Liquid tags.
  Sometimes this matters, like when you have expressions on separate lines that might evaluate to blank, leading markdown to insert blank paragraphs, messing up layout.
  We recommend only adding the trim syntax when you observe unwanted whitespace/paragraphs in your resulting site.

### Template files and folders

Files and folders used by the template.
You might want to touch these if you want more customization, but make sure you know what you're doing.

- `.github` - Files related to GitHub Actions.
  This template uses GitHub Actions to help [build the research page](#automatic-citations).
- `/_includes` - Reusable, small snippets of HTML that can take parameters, aka _components_.
  See `index.md` for which ones you are meant to use.
  Notably, see `header.html` to change the links that appear in the header on every page.
- `/_layouts` - Templates that all pages are built upon.
  See `member.html` and `post.html` to change how the individual team member and blog post pages look.
- `/css` - Sass styles that determine how the site looks.
  Notably, see `variables.scss` to change things like site-wide colors and fonts.
  If you need to add your own custom styles, make a new `.scss` file here and make sure to list it in `/_includes/styles.html`.
- `/js` - JavaScript "plugins" that add interactive features to the site, such as tooltips.

### Under-the-hood files and folders

Files and folders used internally by Jekyll or other tools in the setup.
You should never need to touch these.

- `/_site` - The "compiled" output of the entire Jekyll site.
  Changes to it will get overwritten every time the site is rebuilt.
  This folder is also what GitHub reads to make the GitHub Pages site.
- `/.jekyll-cache` - Cache so that Jekyll can build and re-build the site quickly.
- `.gitignore` - Files to not be tracked/included in your site's repo.
- `debug.log` - Jekyll outputs this log when something goes wrong compiling the site.
- `Gemfile` and `Gemfile.lock` - Files that specify the package dependencies of the project.
  Similar to `package.json` and `package-lock.json` in `npm`.

## FAQ's

### Starting a copy of this template

1. [Make a GitHub account](https://github.com/join)
2. [Create a new repo under your account from this template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).
   We recommend naming your repository `yourlabname-website`.
   Leave `Include all branches` unchecked.

### Editing your site

[Find the item you want to edit](#contents), then:

1. Edit the file [through the GitHub website](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)

OR

1. Edit the file [with Git](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line) on your computer

### Previewing and testing changes on the GitHub website

1. [Make a Netlify account](https://app.netlify.com/signup) for your organization
2. [Hook up Netlify to your repo](https://docs.netlify.com/configure-builds/get-started/#basic-build-settings)
3. [Set the deploy notifications you want](https://docs.netlify.com/site-deploys/notifications/).
A bunch are enabled by default.
We recommend deleting them all, then adding just `GitHub commit status → Deploy Preview succeeded`, `GitHub commit status → Deploy Preview failed`, `GitHub pull request comment → Deploy Preview succeeded`, and `GitHub pull request comment → Deploy Preview failed`.
With these, when you open or update a PR, Netlify will post a comment with a link to the preview and its status, and also add a [check](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-required-status-checks)/[status](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-status-checks) for the preview.
4. [Make a pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) to your repo, and a live preview website of the changes will be automatically built and shown in the pull request according to your notifications.

### Previewing and testing changes on your computer

1. [Install Ruby](https://www.ruby-lang.org/en/documentation/installation/)
2. [Install RubyGems](https://rubygems.org/pages/download)
3. Open your command line
4. [Install Jekyll](https://jekyllrb.com/) by running `gem install bundler jekyll`
5. Go to the folder where you cloned your site, eg `cd lab-website-template`
6. Start the site by running `./start.sh`
7. The site should automatically open in a browser.
   Any changes you make should automatically rebuild the site and refresh the page, except for changes to `_config.yml` which require re-running the start script.

### Publishing your site

1. [Turn on GitHub Pages](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) in the settings of your repo
2. Your site should be live within a minute or two
3. Go where GitHub shows you that your site is published.
   If you haven't set up a custom domain, it should be at `https://your-lab.github.io/lab-website/` by default.

### Using the pre-built components

The various `index.md` files in this repo aim to list and document all of the included components.
See their source code to see how to write the components into your site, and see the [template demo](https://greenelab.github.io/lab-website-template) to see what the components look like in action.

### Automatic Citations

Automatic citations work a little bit different than the rest of the template.
Instead of Jekyll automatically building them, we need to run a special Python script in `/_data/build-research.py`.

**Having GitHub run the script for you (previewing and testing on the GitHub website):**

When possible, make pull requests from branches on your main website repo rather than from forks of it.
GitHub Actions still has certain [quirks](https://github.com/stefanzweifel/git-auto-commit-action/issues/117) and [limitations](https://github.com/stefanzweifel/git-auto-commit-action#using-the-action-in-forks-from-public-repositories) with forks, so the following process will be more reliable with branches.

1. Make sure that [GitHub Actions is enabled](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/disabling-or-limiting-github-actions-for-a-repository) on your main website repo
2. If making changes from a fork of your main website repo, make sure GitHub Actions is also enabled on the fork
3. Add or change the desired papers in `/_data/research-input.yml`
4. [Make a pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) with the changes 
5. GitHub should automatically run the Python script
6. Citations will be automatically generated and output to `/_data/research-output.yml`
7. GitHub should automatically commit the output file onto your pull request
8. The _research list_ component will now (in [pull request previews](#previewing-and-testing-changes-on-the-github-website) and when you merge the pull request) show the updated list of papers

**Running the script manually (previewing and testing on your computer):**

1. [Install Python](https://www.python.org/downloads/)
2. [Install pip](https://pip.pypa.io/en/stable/installing/)
3. [Install Manubot](https://github.com/manubot/manubot#installation)
4. Add or change the desired papers in `/_data/research-input.yml`
5. Run `./build.sh`, which will run the Python script
6. Citations will be automatically generated and output to `/_data/research-output.yml`
7. The _research list_ component will now show the updated list of papers

### Configuring blog post comments

Having comments on blog posts (or elsewhere) isn't a trivial feature to implement.
There needs to be 1) a plugin on the page that lets users log in, read comments, and post new ones, and 2) a server running to receive, permanently store, and retrieve comments.

It's beyond the purview of this template to build in solution for this, but luckily there are many third party ones that can be easily integrated:

- [Disqus](https://disqus.com/)
- [Facebook Comments](https://developers.facebook.com/docs/plugins/comments/)
- [Hyvor Talk](https://talk.hyvor.com/)
- [Staticman](https://staticman.net/docs/)
- [Schnack](https://github.com/schn4ck/schnack)
- [Remark42](https://github.com/umputun/remark42)
- [Isso](https://github.com/posativ/isso)

...[to name a few](https://www.google.com/search?q=jekyll+comments).
Research the options [carefully](https://replyable.com/2017/03/disqus-is-your-data-worth-trading-for-convenience).

Some are full services that take care of the plugin and server for you.
Usually for these, you just create an account the paste the code snippet they give you anywhere you want a comment section to appear, eg at the bottom of `/_layouts/post.html`.

Others just give you a plugin and the tools you need to run your own server, giving you greater privacy and security, but requiring more work to set up.

### Hooking up a custom domain

Follow the instructions [here](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain).

Summarized:

1. Purchase a domain name from a reputable service, such as Google Domains, Namecheap, etc.
2. Point your domain name provider to GitHub Pages using an `A` record.
   It's slightly different for each company, so they should have their own instructions on how to do this.
3. Set the custom domain field in the settings of the repo.

Then:

1. Set `baseurl` in `_config.yml` to `""` to make all the links on your site operate under the assumption that the root of the site is at `your-new-domain.com/` instead of eg `your-lab.github.io/lab-website`.

### Updating your site when this template gets updated

See [this post](https://stackoverflow.com/questions/56577184/github-pull-changes-from-a-template-repository) about pulling upstream changes from a template repository.

## Acknowledgments

All included photos are licensed under [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/), found using [Creative Commons Search](https://search.creativecommons.org/).

## Support

There are a lot of different technologies involved in this template; it's okay if you don't have a deep understanding of them all.

If you need help, first make sure you search this readme and look through the various `index.md` files in the repo.
Also, we've tried to include comments in all files where we think they're needed, especially where users are likely to want to customize things.
Look for file names relevant to your question, and you may find that you can achieve what you want just by opening them up and editing them.

If you still need help, or if you have a suggestion for how to make this template easier to use for novices, please [post a new issue on this repository](https://github.com/greenelab/lab-website-template/issues).

<p align="center"><img height="200" src="https://user-images.githubusercontent.com/8326331/96628877-d1658e00-12e0-11eb-894c-7bb0d7f07632.png" alt="Lab Website Template"></p>
