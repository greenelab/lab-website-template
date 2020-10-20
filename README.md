<h1 align="center">Lab Website Template</h1>
<p align="center"><img height="200" src="https://raw.githubusercontent.com/greenelab/lab-website-template/master/icons/share-thumbnail.jpg?raw=true" alt="Lab Website Template"></p>

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
  - beautifully formatted tables and code blocks
  - social media links with icons
  - figures with captions
  - image galleries
  - multi-size cards with image and text
  - member portraits with assignable role icons
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
That said, the template tries to make things as simple as possible, and if you're willing to learn, you should still be able to use it.

- A **repository** (or repo for short) is a place to store code for a project
- **[Git](https://try.github.io/)** is a for and way of tracking changes to code through a [command line](https://en.wikipedia.org/wiki/Command-line_interface).
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
- **[Sass](https://sass-lang.com/)** (a superset of [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)) is how you get a web page to look that way you want it.
  You can set [positions, margins, colors, fonts, etc](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#Keyword_index), and apply them to certain elements in the HTML with [selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors).
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)** (or JS for short) is a programming language to make web pages more interactive.
  HTML is static/unchanging, but JavaScript allows the page to change dynamically as the user is viewing it.
  For example, JavaScript can hide/show certain paragraphs in the HTML based on what the user types into a search box.
- **[Jekyll](https://jekyllrb.com/)** is a tool that can automatically generate large HTML sites from much simpler markdown, and with less grunt work and code duplication, allowing you to just focus on the content.
  It does all this fancy work in a "pre-process" step, before you open the site.
  When you make a change, Jekyll compiles everything together into the final product which can then be viewed or uploaded.
  Jekyll also integrates very nicely with GitHub Pages, so almost no set up is required.
- **[Liquid](https://shopify.github.io/liquid/)** is a [templating language](https://en.wikipedia.org/wiki/Template_processor) that allows you to insert repetitive chunks of content automatically and define logic for how your site is built by Jekyll.
  For example, you could provide Jekyll with a simple list of items, then use Liquid to sort them and [automatically](https://shopify.github.io/liquid/tags/iteration/) put each one in their own table row.
  This is much better than having to type them all out manually and re-sort them any time you add or remove one.
  You can almost think of Liquid as (a much more limited) JavaScript for Jekyll, except that it still results in a static file at the end.
- **[Ruby](https://www.ruby-lang.org/en/)** is a general-purpose programming language.
  It isn't necessary to know any Ruby to use this template, but you'll encounter a few [Ruby-related files](https://www.rubyguides.com/2018/09/ruby-gems-gemfiles-bundler/) in the template, because Jekyll is built on Ruby.

## Contents

An overview of the contents of this template and basic notes on how to edit and use them.
If something is still not clear, try looking for comments in the file of interest.

### Your files and folders

Files and folders to be edited by you.

- `/blog`, `/contact`, etc - A sub-folder to make in the resulting site, eg `yoursite.com/blog`.
  You can create any folder you want, put an `index.md` in it, and link to it like any other page.
  To edit the links shown in the site header, see `/_includes/header.html`.
- `/_posts` - Where your blog posts go.
  Name your post files in the format `YYYY-MM-DD-your-post-title.md`.
  Each file will automatically generate its own page and be listed on the blog page.
- `/icons` - Icons for when your site is bookmarked in a browser, added as an app shortcut on a phone, and shared on social media.
  These are important!
  Replace these images with variations of your own logo, taking care to match the size and cropping.
  They can be transparent, but make sure they can be distinguished on any background, dark or light.
  [realfavicongenerator.net](https://realfavicongenerator.net/) can help you generate all the necessary icon variations, but it goes overboard with support for legacy browsers.
  What's included in this template is a simplified subset that works fine on all of the most common modern browsers.
- `/images` - A default folder to hold all your site's images.
  You can organize and place your images however you want though.
  For example, you could put photos of your team in `/team/photos/` and just refer to them like `team/photos/anna-sun.jpg`.
- `_config.yml` - The main Jekyll configuration for your site.
  Contains important site-wide things like the site title, the site url, the default email/twitter/etc, the default background image, etc.
- `404.md` - A fallback page for when a user goes to a page that doesn't exist on your site.
- `index.md` - The landing page for your site.

_Note:_ Naming a file `index` is a web convention for referring to the "main" page of a particular folder.
For example, `yoursite.com/join` actually takes you to `yoursite.com/join/index.md`.
And `yoursite.com` takes you to the root `index.md`.

_Note:_ When manually linking to other pages on your site, use the Jekyll [`relative_url`](https://jekyllrb.com/docs/liquid/filters/) filter to make sure links always work no matter where you're hosting your site from.
For example, instead of `[Join the team](/join)`, do `[Join the team]({{ "/join" | relative_url }})`.
Pre-built components that have links already do this for you though, so you can just do eg `link="/join"`.

### Template files and folders

Files and folders used by the template.
You might want to touch these if you want more customization, but make sure you know what you're doing.

- `/_includes` - Reusable, small snippets of HTML that can take parameters, aka _components_.
  See `index.md` for which ones you are meant to use.
  Notably, see `header.html` to edit the links shown in the site header.
- `/_layouts` - Templates that all pages are built upon.
- `/css` - Sass styles that determine how the site looks.
  Notably, see `variables.scss` to change things like site-wide colors and fonts.
  If you need to add your own custom styles, make a new `.scss` file here and make sure to include it in `/_includes/styles.html`.
- `/js` - JavaScript "plugins" that add interactive features to the site, such as tooltips.
- `start.sh` - A convenient script to start and open the site on your computer.
  Quicker to type and easier to remember than the commands it runs.
  Run like `./start.sh`.

### Under-the-hood files and folders

Files and folders used internally by Jekyll or other tools in the setup.
You should never need to touch these.

- `/_site` - The "compiled" output of the entire Jekyll site.
  Changes to it will get overwritten when the site is rebuilt.
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
3. [Make a pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) to your repo, and a live preview website of the changes will be automatically built and [shown in the pull request](https://docs.netlify.com/site-deploys/notifications/#github-commit-statuses)

### Previewing and testing changes on your computer

1. [Install Ruby](https://www.ruby-lang.org/en/documentation/installation/)
2. [Install RubyGems](https://rubygems.org/pages/download)
3. [Install Jekyll](https://jekyllrb.com/) by running `gem install bundler jekyll`
4. In your command line, go to the folder where you cloned your site
5. Start the site by running `./start.sh`
6. The site should automatically open in a browser.
   Any changes you make will automatically rebuild the site and refresh the page, except for changes to `_config.yml` which require re-running the start script.

### Publishing your site

1. [Turn on GitHub Pages](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) in the settings of the repo
2. Go where GitHub shows you that your site is published.
   If you haven't set up a custom domain, it will be at `https://your-org-name.github.io/the-repo-name/`.

### Using the pre-built components

The `index.md` file aims to provide a complete listing of all of the included components, and how to use them.
See its [raw source code](https://github.com/greenelab/lab-website-template/blob/master/index.md) to see how to write the components into your site, and see the [template demo](https://greenelab.github.io/lab-website-template) to see what the components look like in action.

### Hooking up a custom domain

Follow the instructions [here](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain).

Summarized:

1. Purchase a domain name from a reputable service, such as Google Domains, Namecheap, etc.
2. Point your domain name provider to GitHub Pages using an `A` record.
   It's slightly different for each company, so they should have their own instructions on how to do this.
3. Set the custom domain field in the settings of the repo.

Then:

1. Set `baseurl` in `_config.yml` to `""` to make all the links on your site operate under the assumption that the root of the site is at `yournewdomain.com/` instead of eg `github.io/lab-website-template`.

(This is why it's necessary to use the Jekyll [`relative_url`](https://jekyllrb.com/docs/liquid/filters/) filter, as mentioned in [Contents](#contents).)

### Updating your site when this template gets updated

See [this post](https://stackoverflow.com/questions/56577184/github-pull-changes-from-a-template-repository) about pulling upstream changes from a template repository.

## Acknowledgments

All included photos are licensed under [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/), found using [Creative Commons Search](https://search.creativecommons.org/).

## Support

There are a lot of different technologies involved in this template, it's okay if you don't have a deep understanding of them all.
If you need help or have a suggestion for how to make this template easier to understand or use for novice users, please let us know by [making a GitHub account](https://github.com/join) and [posting an issue on this repository](https://github.com/greenelab/lab-website-template/issues).
