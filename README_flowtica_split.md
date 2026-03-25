# Flowtica landing page structure

This repo builds the homepage from section partials and generates additional root pages for solutions, supporting
examples, and jobs.

## Structure

- `index.html` - generated homepage used by GitHub Pages
- `src/_head.html` - shared `<head>` and layout shell up to the main content area
- `src/_nav.html` - shared navigation sidebar used by the homepage, generated root pages, and job pages
- `src/home.html` - Home section
- `src/about.html` - About section
- `src/services.html` - Services section
- `src/portfolio.html` - Solutions section on the homepage
- `src/offers.html` - Offers section
- `src/careers.html` - Careers section
- `src/contact.html` - Contact section and form
- `src/_footer.html` - layout closing markup and scripts
- `src/cases/` - source content for generated solution and example pages
- `src/jobs/` - source content for generated job pages
- `build.py` - canonical rebuild command for homepage, generated root pages, and jobs
- `build_cases.py` - helper that generates solution and example pages from `src/cases/`
- `build_jobs.py` - helper that generates job pages from `src/jobs/`
- `build.js` - legacy homepage-only helper; not the canonical rebuild path

## Usage

1. Edit source files under `src/`, `src/cases/`, or `src/jobs/`.
2. Rebuild the published outputs with:

   ```bash
   python build.py
   ```

3. Commit the updated generated files in the repo root and `jobs/`. GitHub Pages uploads the repository root directly,
   so deploys will drift if generated outputs are not committed.
