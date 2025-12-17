# Flowtica landing page

This repository builds `index.html` from the section files in `src/` using either `node build.js` or `python build.py`. Edits should go into the source fragments, then re-run the build to refresh the compiled page.

## Syncing with main

This workspace does not have a remote configured, so `git pull origin main` will fail until a remote is added (for example: `git remote add origin <repo-url>`). Once a remote exists, pull the latest main branch and rebuild to resolve any merge conflicts in the generated `index.html`.

```bash
git pull --rebase origin main
node build.js
```
