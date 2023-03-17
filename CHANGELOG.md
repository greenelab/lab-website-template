# Changelog

Reference: common-changelog.org

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
