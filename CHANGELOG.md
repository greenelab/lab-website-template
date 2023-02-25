# Changelog

Reference: common-changelog.org

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

- Template is no longer limited to GitHub Pages white-listed Jekyll plugins.
- Pull request previews happen right within GitHub instead of needing Netlify.
- Citation-related files in `/_data` must now be named prefixed with the cite plugin they are to be run with, e.g. `sources-2020.yaml` or `orcid-casey.yaml`.
- Folder renames for clarity and for better separation of template and user content: `/auto-cite` → `/_cite`, `/css` → `/_styles`, `/js` → `/_scripts`.
- "Tools" page renamed to "Projects" to be more clear and general purpose.
- `extra-links` renamed to `buttons` in `sources.yaml` files.
- Renamed `theme.scss` to `-theme.scss`.
- Renamed components: link → button, two-col → cols, gallery → grid.
- Use CSS variables instead of Sass variables.
- Redesign components, change parameters and behavior.
- Simplify caching method in automatic citation process.
- Drastically simplify Liquid code by including Ruby plugins.
- Simplify CSS and JS.
- `CITATION.cff` file now source of truth for version.
- Update Font Awesome icon names from v5 to v6.

### Added

- New docs at greene-lab.gitbook.io/lab-website-template-docs.
- Add automations for first time setup and URL change.
- Write PubMed and Google Scholar automatic citation plugins.
- Automatic citations through GitHub Actions should now work from (most) forks.
- Add optional description and type params to citations.
- Add periodic cite process run that opens a pull request.
- List component filter can now accept arbitrary regex.
- Add richer metadata for SEO.
- Add author portrait and updated date for blog posts.
- Add light/dark mode toggle.

### Removed

- Remove options from `_config.yaml` to simplify configuration: `baseurl`, `auto-cite`, `logo`.
- Remove `/favicons` folder, hardcode files for logo, icon, and share in `images`.
- Remove `palettes.scss`.
- Remove banner component (same thing can be achieved with full width section and figure components).
- Remove role component. Combined with portrait component.
