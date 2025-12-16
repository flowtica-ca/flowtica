# Flowtica landing page structure

This repo has been refactored so `index.html` is built from smaller section files.

## Structure

- `index.html` – generated file used by GitHub Pages
- `src/_head.html` – `<head>` and layout shell up to the Home section
- `src/home.html` – Home section
- `src/about.html` – About section
- `src/services.html` – Services section
- `src/portfolio.html` – Case Studies & Demos section
- `src/offers.html` – Introductory Offers section
- `src/contact.html` – Contact section + form
- `src/_footer.html` – layout closing markup, style switcher, and scripts
- `build.js` – small Node script that concatenates the pieces into `index.html`
- `build_cases.py` – rebuilds the case study HTML files from a shared template in `src/cases`

## Usage

1. Edit the section files under `src/` instead of editing `index.html` directly.
2. Rebuild `index.html` by running:

   ```bash
   node build.js
   ```

3. Rebuild the case study pages (to keep the navigation and shell consistent) by running:

   ```bash
   python build_cases.py
   ```

4. Commit the updated `index.html` and the generated `case-*.html` files for deployment (for example, to GitHub Pages).

