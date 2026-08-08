# Maverix Medical — Website Rebuild

A static recreation of www.maverixmedical.com. 23 HTML pages plus one shared
stylesheet, served by GitHub Pages.

> **Read this first: do not edit the HTML files.**
> Every `.html` file and `theme.css` in this repo is **generated output**. They are
> overwritten wholesale on the next build. All edits go into `src/build.py` or
> `src/theme.css.tpl` — see [Making a change](#making-a-change).

---

## How the site is built

Two source files produce the entire site:

| Source | Produces | What lives in it |
|---|---|---|
| `src/build.py` | all 23 `.html`, `sitemap.xml`, `robots.txt`, `assets/site.webmanifest` | page structure, **all copy**, the shared header/footer, and the site's JavaScript |
| `src/theme.css.tpl` | `theme.css` | every style rule |

```bash
python3 src/build.py     # writes into src/site/
```

The generator writes into a local `src/site/` directory. The **contents** of that
directory are what is committed to the root of this repo — so `src/site/index.html`
becomes `/index.html` here. Copy the changed files up when you commit.

No dependencies, no build tools, no package manager. Python 3 standard library only.
The build is deterministic: same input, byte-identical output.

Everything else in the repo (`images/`, `assets/`) is static and checked in by hand.

### Why a generator

The header, footer, nav dropdowns, contact block and product-page chrome are
identical across 23 pages. Generating them means a change to the footer is one edit
in one place rather than 23 edits that drift apart. Site copy also lives in Python
data structures near the top of each section, so changing wording never means
hunting through markup.

---

## Layout

```
src/build.py        ← generator: structure, copy, JS
src/theme.css.tpl   ← source stylesheet
README.md

index.html          ← ↓ all generated — do not edit ↓
products.html
thoracent.html          Intervention   (category page)
diagnostics.html        Risk Assessment (category page)
serpex.html             Diagnosis      (category page)
team.html
news.html
careers.html
contact-us.html
privacy-policy.html
terms-of-use.html
regulatory-information.html
404.html
theme.css
sitemap.xml
robots.txt
products/           ← 10 generated product detail pages

images/             ← 28 static files, hand-managed
assets/             ← 32 static files: favicons, og cards, logos, hero video
```

Note the three category pages have historical filenames that no longer match their
titles: `thoracent.html` is **Intervention**, `diagnostics.html` is **Risk
Assessment**, `serpex.html` is **Diagnosis**. Renaming them would break inbound
links, so the filenames stayed.

---

## Making a change

**Copy edits** — find the text in `src/build.py`. It is stored close to where it is
used: `INTERVENTION_GROUPS` and `DIAGNOSIS_TOOLS` for product listings, the
`pd_page(...)` calls in `build_product_pages()` for product detail pages, `NEWS`
for the news archive, `LEADERS` / `ADVISORS` for the team page.

**Style edits** — `src/theme.css.tpl`. It is organised as a base layer followed by
dated append blocks (`/* --- v43: … */`). New rules go at the bottom in a new
block, with a comment explaining what and why. Do not reformat old blocks; the
regression harness compares rendered output, and needless churn makes review harder.

**Structural edits** — the page shell is `page()`; the header and footer are
`header()` and `footer()`; product detail pages are `pd_page()`.

Then:

```bash
python3 src/build.py
```

then copy the changed files out of `src/site/` to the repo root and commit them
together with your source edit.

### Domain cutover

`BASE_URL` at the top of `src/build.py` drives canonical tags, `og:url`, `sitemap.xml`,
and the root-absolute paths in `404.html`. At cutover, change it to
`https://www.maverixmedical.com` and rebuild. That is the only edit required.

---

## Naming conventions

Class names are descriptive and stable across rebuilds. A section is named for what
it is: the homepage Challenge block is `.challenge`, containing `.statgrid` and
`.bigstat`; the patient-journey diagram is `.journey` / `.jbar` / `.jseg`.

Two conventions worth knowing:

- **State classes are prefixed `is-`** — `.is-active` (selected tab), `.is-in-view`
  (element has scrolled into view). These are applied by JavaScript at runtime and
  will not appear in the generated HTML.
- **`.btn` and `.nav`** are kept short deliberately, as universal idioms.

Class names are hand-written, never generated. Rebuilding does not change them.

---

## JavaScript

There is no framework and no build step. Roughly 8 KB of vanilla JS is inlined at
the bottom of every page from the `JS` constant in `src/build.py`, covering: nav
dropdowns and the mobile menu, bio modals with focus trapping, product-page tabs,
scroll reveals, the statistic count-up, carousels, and form handling.

It is currently duplicated across all 23 pages. Extracting it to a shared `site.js`
the way the CSS was extracted is a known, un-done improvement.

**If you rename a class, check the JS.** Thirteen selectors reference classes by
name (`.pathcard`, `.tabbar [data-tab]`, `.statgrid .stat-number`, `.overlay`,
`.modal.open`). A missed rename there breaks a behaviour without changing a single
pixel, so visual comparison will not catch it.

---

## Third-party services

Everything else is self-hosted — no Webflow CDN, no jQuery.

| Service | Purpose | Notes |
|---|---|---|
| **CookieYes** (`b0481c682f112a57de13418a`) | consent banner | Same client ID as the live site. The rebuild's domain must be added to the allowed-domains list in the CookieYes dashboard or the banner will not render. |
| **Google Analytics 4** (`G-QFMYMJ9YWX`) | analytics | Gated behind Google Consent Mode v2, defaults denied. Sets no cookies until the visitor opts in. |
| **Google Fonts** | Poppins, Jost | No cookies. |
| **SociableKit** | LinkedIn job listings | Careers page only. |
| **YouTube** (`youtube-nocookie.com`) | product demo videos | 5 product pages, 7 videos. |
| **Calendly** | "Book a Virtual Demo" | Outbound link, not an embed. |

The consent block in `page()` is order-sensitive: Consent Mode defaults must be
registered **before** the GA4 tag loads, or GA4 sets `_ga` on first paint.

### Forms

`FORM_ENDPOINT` is currently empty, so the contact and careers forms fall back to
opening the visitor's mail client with the message pre-filled — nothing is
transmitted to a server. Setting `FORM_ENDPOINT` to a Formspree URL switches them to
real submissions with no other change. Both forms carry a honeypot field
(`.honeypot`), required-field validation, and inline success/error messages.

---

## Deployment

GitHub Pages, `main` branch, `/` root. Pushing to `main` publishes within a minute
or two.

Branch `archive-pre-cleanup-2026-08-05-do-not-use` is a frozen snapshot from before
a code cleanup. It is 13 commits behind and exists only as a rollback point —
**do not branch from it or treat it as current.**

---

## Verifying a change

Two harnesses backstop edits. Both run against a local HTTP server, not `file://` —
Chromium refuses to load the stylesheet cross-origin over `file://`.

**Visual regression** — loads all 23 pages at 1440 / 768 / 390 with animations
frozen and fingerprints every element (13,725 of them): position, size, and 15
computed style properties. Compare before and after; anything nonzero is either
intentional or a bug.

**Interaction** — separately exercises the behaviours the fingerprint cannot see:
nav dropdowns, all 13 bio modals, overlay-click-to-close, card hover reveals,
whole-card click-through, tab switching, the stat count-up, mobile menu and submenu.

The visual harness alone is not sufficient. A broken event listener changes nothing
at rest, so both matter.

One known quirk: `404.html` uses root-absolute paths (`/maverix-website-rebuild/…`)
because GitHub Pages serves it at any depth. Testing it locally therefore requires
serving from a parent directory that reproduces the repo-name path segment.
