# Changelog

Reference: common-changelog.org

## 1.3.8 - 2025-11-17

### Changed

- Inherit secrets in GitHub Actions workflows where appropriate
- Add commented out ORCID plugin code to discard source if no ID

## 1.3.7 - 2025-07-31

### Changed

- Improve cleanup of PR preview folders in gh-pages branch.
- Only run debug dump in debug mode to speed up workflow runs.

## 1.3.6 - 2025-07-30

### Changed

- Improve behavior and flexibility of ORCID cite plugin.

## 1.3.5 - 2025-05-12

### Changed

- Fix workflow bug where PR previews on GitHub Actions have broken styles/links/etc.
- Fix tags component relative link bug.
- Make Actions workflows a bit more robust.

## 1.3.4 - 2025-02-03

### Changed

- Fix section component parsing bug.

## 1.3.3 - 2025-01-25

### Changed

- Citation process logging enhancements.

### Added

- Add support for multiple authors in blog posts.
- Add GitHub Actions workflow status badges to readme.

## 1.3.2 - 2025-01-06

### Changed

- Misc enhancements and bug fixes.

## 1.3.1 - 2024-11-11

### Changed

- Update and improve workflows for building site and citations.
- Escape user inputs better in rare edge cases.

## 1.3.0 - 2024-08-16

### Changed

- List component `filters` parameter changed to `filter` and now takes any Ruby expression instead of the existing custom syntax.
  Example: `filters="publisher: bioRxiv, date: ^2020"` becomes `filter="publisher == 'bioRxiv' and date =~ /^2020/"`.
  See docs for more info.
- Fix rare bug where data (e.g. a paper title) containing certain characters (e.g. a double quote) can mess up HTML rendering.
- Fix "first time setup" workflow bug.
- Tweak GitHub Actions debugging/logging.

### Added

- Styling for `<details>` HTML element.

## 1.2.2 - 2024-06-05

### Added

- Add `affiliation` member portrait field.

### Changed

- Change order and type of preferred ids from ORCID API.
- Expand list of supported Manubot identifiers and thus keep ORCID API details less often.
- Simplify portrait component under-the-hood.
- Make tag component de-duplication consistent with search plugin de-duplication.

## 1.2.1 - 2024-04-01

### Changed

- Minor bug fixes in cite process and sitemap generation.

## 1.2.0 - 2024-03-08

### Changed

- Update all GitHub Actions to fix "Node v16 deprecated" warnings.
- Sources that Manubot doesn't know how to cite (e.g. wosuid:12345) are now ignored by default if they're from metasources.
- Fix bug where passing tags to tags component manually doesn't work.
- Fix bug in citation (and other) components when `lookup` is blank.
- Fix nested tables bug.
- Dark mode tweaks.
- Various CSS tweaks and fixes.

### Added

- Add `image` param to support blog post thumbnails.
- Add `html-proofer` plugin that checks for broken images/links/etc.
- Add `remove` flag to remove a source from a metasource.

## 1.1.6 - 2023-10-06

### Changed

- Use latest minor versions of Python packages in auto-cite script.

## 1.1.5 - 2023-05-19

### Changed

- Fix ORCID plugin bug and other cite process tweaks.

## 1.1.4 - 2023-04-28

### Changed

- Fix ORCID plugin and other cite process bugs.

## 1.1.3 - 2023-04-20

### Changed

- Fix first-time-setup mv bug.
- Fix citation, float, and portrait component CSS.
- Filter and trim citation info fields.

## 1.1.2 - 2023-04-11

### Changed

- Fix first-time-setup rm bug.

## 1.1.1 - 2023-04-06

### Changed

- Change member profile page from col layout to float.
- Fix first time setup. Preserve config formatting and comments.
- Improve Docker cite process behavior.
- Fix post excerpt component start/end markers and special search attr chars.
- Fix misc CSS.

### Added

- Add show-title and show-subtitle site config options.
- Include site subtitle in description meta tag.
- Add user pull request template.
- Add title and link fallbacks to citation component.

## 1.1.0 - 2023-03-17

Add alert component, Docker support, accessibility fixes.

### Changed

- Fix Lighthouse accessibility issues.
- De-href components when link isn't provided (no hand cursor icon on hover or nav on click).
- In search script, limit highlights by total count instead of char length.
- Grid and link style tweaks.
- Take ORCID icon from Font Awesome.
- Misc bug fixes in tags script, float component.

### Added

- Add Docker configuration and scripts for local previewing.
- Add alert component and types.
- Role icon in portrait component hoisted to top left.

## 1.0.0 - 2023-02-28

First official release.

High-level comparison with pre-releases:

- Simpler configuration.
- More automation, less setup.
- More customization and flexibility.
- Redesigned components.
- New docs.
- Complete rewrite.
- Culmination of years of feedback.

### Changed

- Template is no longer limited to GitHub Pages white-listed Jekyll plugins. Any plugins possible.
- Pull request previews happen right within GitHub instead of needing Netlify.
- Better versioning. `CITATION.cff` file now source of truth for version, and tags/releases enforced.
- Citation-related files in `/_data` must now be named prefixed with the cite plugin they are to be run with, e.g. `sources-2020.yaml` or `orcid-students.yaml`.
- Folder renames for clarity and for better separation of template and user content: `/auto-cite` → `/_cite`, `/css` → `/_styles`, `/js` → `/_scripts`.
- Rename "Tools" page to "Projects" to be more clear and general purpose.
- Rename `extra-links` to `buttons` in `sources.yaml` files.
- Rename `theme.scss` to `-theme.scss`.
- Rename/repurpose components: link → button, two-col → cols, gallery → grid.
- Combine "link" and "role" data lists into single `types.yaml` map.
- Redesign components, change parameters and behavior.
- Update Font Awesome icon names from v5 to v6.
- Change placeholder text, images, and other images.
- Use CSS variables instead of Sass variables.
- Simplify caching method in cite process.
- Simplify Liquid code by including custom Ruby plugins.
- Simplify styles and scripts.

### Added

- New docs at greene-lab.gitbook.io/lab-website-template-docs.
- Add automations for first time setup and URL change.
- Write PubMed and Google Scholar automatic citation plugins.
- Automatic citations through GitHub Actions should now work from (most) forks.
- Add optional description and type params for citations.
- Add periodic cite process run that opens a pull request.
- List component filters can now accept arbitrary regex.
- Add light/dark mode toggle.
- Pre-install selection of useful Jekyll plugins, namely Jekyll Spaceship.
- Add author portrait and updated date for blog posts.
- Add richer metadata for SEO.
- Google Fonts link determined automatically from theme file.

### Removed

- Remove options from `_config.yaml` to simplify configuration: `baseurl`, `auto-cite`, `logo`.
- Remove `/favicons` folder, hardcode files for logo, icon, and share in `/images`.
- Remove `palettes.scss` and `mixins.scss`.
- Remove banner component (same thing can be achieved with full width section and figure components).
- Remove role component. Combine with portrait component.
