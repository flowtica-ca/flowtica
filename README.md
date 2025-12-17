# Flowtica Marketing Site

Flowtica is a static marketing site built from reusable HTML partials. The repo includes simple build scripts that stitch together the landing page and case study pages so navigation stays consistent across the site.

## Project layout

- `src/` – HTML partials for the main landing page and shared fragments such as the head, nav, and footer
- `src/cases/` – Content snippets for case studies and the shared case page template
- `index.html` – Generated landing page published to GitHub Pages
- `case-*.html` – Generated case study pages that reuse the shared navigation shell
- `build.js` – Node.js script that concatenates `src/*.html` into `index.html`
- `build_cases.py` – Python script that rebuilds the individual case pages from the shared template and content snippets

## Prerequisites

- Node.js 18+ (for `build.js`)
- Python 3.10+ (for `build_cases.py`)

## Workflow

1. Edit the HTML partials under `src/` or the case content files under `src/cases/`.
2. Rebuild the landing page:
   ```bash
   node build.js
   ```
3. Rebuild the case study pages:
   ```bash
   python build_cases.py
   ```
4. Commit the updated `index.html` and `case-*.html` outputs so they remain in sync with the source partials.

## Local preview

The generated files are static HTML, so you can open `index.html` directly in a browser or serve the repository root with any static file server (for example, `python -m http.server 8000`).
