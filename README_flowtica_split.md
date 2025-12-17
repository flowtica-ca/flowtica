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
- `src/career.html` – Careers section
- `src/contact.html` – Contact section + form
- `src/_footer.html` – layout closing markup, style switcher, and scripts
- `build.js` – small Node script that concatenates the pieces into `index.html`

## Usage

1. Edit the section files under `src/` instead of editing `index.html` directly.
2. Rebuild `index.html` by running:

   ```bash
   node build.js
   ```

3. Commit the updated `index.html` for deployment (for example, to GitHub Pages).

