# Maverix Medical — Website Rebuild

A self-contained recreation of www.maverixmedical.com. Every page is a single HTML
file with inline CSS/JS. **All images, video and fonts are self-hosted** in `assets/`
— nothing loads from the old Webflow CDN.

## Pages

| File | Page |
|---|---|
| index.html | Home (hero video, mission, challenge, goal, patient journey) |
| products.html | Products overview (Risk Assessment / Diagnosis / Intervention) |
| thoracent.html | Intervention — Thoracent portfolio + product carousel |
| diagnostics.html | Risk Assessment — Maverix Diagnostics |
| serpex.html | Diagnosis — Serpex biopsy tools + specs |
| products/*.html | 9 Thoracent product detail pages |
| team.html | Team (leadership bio popups, advisory board) |
| news.html | News archive |
| careers.html | Careers |
| contact-us.html | Contact (working form) |
| terms-of-use.html / privacy-policy.html | Legal |
| 404.html | Branded not-found page |
| sitemap.xml / robots.txt | SEO |

## Configuration

All of it lives at the top of `build.py`:

```python
BASE_URL      = "https://maverixanalytics.github.io/maverix-website-rebuild"
FORM_ENDPOINT = ""                            # see below
CONTACT_EMAIL = "contact@maverixmedical.com"
```

`BASE_URL` drives canonical tags, og:url, and sitemap.xml. **At domain cutover,
change it to `https://www.maverixmedical.com` and rebuild** — that's the only edit needed.

## Contact form

The contact and careers forms post real submissions. Three modes:

1. **Formspree (works on any host, incl. GitHub Pages)** — create a form at
   formspree.io, set the delivery address to contact@maverixmedical.com, then set
   `FORM_ENDPOINT = "https://formspree.io/f/XXXXXXXX"` and rebuild.
2. **Netlify Forms** — if hosted on Netlify, leave `FORM_ENDPOINT` empty; the
   `data-netlify` markup is already in place and Netlify picks it up automatically.
3. **No endpoint (current default)** — falls back to opening the visitor's mail
   client with the message pre-filled. Never a dead end, but weaker UX.

Both forms include a hidden honeypot field (`_gotcha`) for spam protection,
required-field validation, an in-flight "Sending…" state, and inline success/error messages.

## Build

```
python3 build.py        # regenerates everything into site/
```

## Assets

`.github/workflows/fetch-assets.yml` re-downloads the original media from the
Webflow CDN into `assets/` if ever needed (Actions → Fetch CDN assets → Run workflow).

## Sync to Claude Design

From this folder, in Terminal: `claude`, then ask in plain words:

```
Sync this folder of HTML pages to the Maverix Medical Design System project,
under pages/maverix-website/. Update changed files in place.
```
