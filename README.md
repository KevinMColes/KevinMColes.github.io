# Kevin M. Coles — personal website

A responsive, buildless website for GitHub Pages. No npm installation, framework, server, database, or JavaScript is required.

## Pages

- `/` — Home
- `/about/` — biography, fatherhood, Raising Tactical Daughters and technology leadership
- `/speaking/` — three talks and the existing Calendly inquiry link
- `/book/` — The One Who Would Be Okay (publication details pending)
- `/media/` — coverage, biography and newsletter

Shared styles: `assets/site.css`. Photos: `images/`. The approved photograph with the beard trim is `images/kevin-m-coles-podcast.webp`. The supplied book cover appears on Home and Book, with forthcoming status and a cover-subject-to-change note. Original files and existing downloads are retained.

## Deployment

Keep `CNAME` as `kevinmcoles.com`. Retain the repository's current GitHub Pages source settings; for branch-based Pages this site is served from the root of the published branch. Merge the reviewed redesign branch into that branch to publish. Do not change DNS.

## Content updates

Edit the relevant page's `index.html`. Use **Kevin M. Coles** consistently in visible copy and metadata. Keep light-section copy black. Before publication changes, update both current book-cover treatments and update the book's availability copy, metadata and structured data together. No ISBN, release date, publisher, endorsements or speaking credentials are invented.

## Search setup

Each page includes a unique title, description, canonical URL, social metadata and JSON-LD using the same Person ID. `sameAs` contains personal identity profiles; organizations are represented separately with founder relationships. Submit `/sitemap.xml` to verified Google Search Console and inspect the five URLs after release.

Google's Search profiles are a separate eligibility/claiming process: https://creators.google/profile . Structured data and this redesign do not guarantee rankings or a Knowledge Panel. No meta-keyword tags or hidden keyword lists are used.

## Validation

Run `python3 scripts/check_site.py` to check page structure, local links and assets, canonical URLs, schema consistency, image dimensions and required domain settings. For a local preview, use your editor's static server or `python3 -m http.server` at the repository root. Verify desktop and mobile layouts and test Calendly before merging.
