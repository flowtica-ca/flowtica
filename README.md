# Flowtica Marketing Site

Flowtica is a static marketing site built from reusable HTML partials and generated root pages. The production deploy
model is intentionally simple: GitHub Pages publishes the repository root as-is, so generated outputs must be rebuilt
locally and committed with source changes.

## Project layout

- `src/` - HTML partials for the homepage and shared fragments such as the head, nav, and footer
- `src/cases/` - Source content for generated solution pages and supporting example pages, plus their shared body template
- `src/jobs/` - Source content and template for job pages
- `index.html` - Generated homepage published from the repo root
- `property-management-maintenance-intake-automation.html`, `accounts-payable-back-office-automation.html`, `casl-first-outreach-automation.html` - Generated solution landing pages
- `case-*.html` - Generated supporting example pages published from the repo root
- `jobs/*.html` - Generated job pages
- `build.py` - Canonical full-site build entrypoint; rebuilds `index.html`, generated root pages, and jobs
- `build_cases.py` - Python helper used by `build.py` to generate solution and example pages
- `build_jobs.py` - Python helper used by `build.py` to generate job pages
- `build.js` - Legacy index-only helper; not the canonical production rebuild path

## Prerequisites

- Python 3.10+ for `build.py`
- Node.js is only needed if you intentionally use the legacy `build.js` helper

## Workflow

1. Edit the source files under `src/`, `src/cases/`, or `src/jobs/`.
2. Rebuild the site with:

   ```bash
   python build.py
   ```

3. Review the generated root HTML files and `jobs/*.html`.
4. Commit both the source changes and regenerated outputs. GitHub Pages uploads the repo root directly and does not run a build on deploy.

## Local preview

Open `index.html` directly in a browser or serve the repository root with any static file server, for example:

```bash
python -m http.server 8000
```
