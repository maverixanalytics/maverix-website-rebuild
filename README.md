# Maverix Medical — Astro rebuild

The [maverixmedical.com](https://www.maverixmedical.com) site rebuilt from the
legacy Python generator (`build.py` + `theme.css.tpl`) as an **Astro 6 +
React islands** app, per `REACT-MIGRATION-PLAN.md`. All 23 pages, byte-parity
on visible text, pixel-parity in the visual harness, targeting **Netlify-only**
hosting.

Read `CONVENTIONS.md` before changing anything; `PARITY-EXCEPTIONS.md` lists
every known difference from the legacy site.

## Commands

```bash
npm ci               # Node >= 22.12
npm run build        # → dist/ (23 pages + sitemap.xml/robots.txt/webmanifest)
npm run check        # astro check + tsc --noEmit
node scripts/verify/interact.mjs   # interaction harness (needs a prior build)
```

## Layout

- `src/content/` — ALL copy as schema-validated collections (products, news,
  leaders, legal pages) + citation/reference data. Editing copy = editing a
  content file; the build fails on schema violations.
- `src/pages/` — one file per legacy URL (filenames frozen, including
  `serpex.html`=Diagnosis, `diagnostics.html`=Risk Assessment,
  `thoracent.html`=Intervention, and the `bonastent-esophogeal-stent` typo).
- `src/components/` — static Astro components; `src/islands/` — the seven
  React islands (nav, tabs, modals, cards, count-up, forms).
- `src/styles/ported/` — the legacy stylesheet flattened (winner-per-property,
  dead overrides dropped) into per-area files; `tokens.css` is the palette.
- `src/config/site.config.ts` — the ONLY place URLs/IDs/emails live.
  **Domain cutover = change `SITE_URL`, rebuild.**
- `public/` — legacy `assets/` + `images/` verbatim (not in the source zip if
  you received one — copy from the legacy repo).

## Review workflow

Netlify site: `inspiring-salamander-23b62b`
(`https://inspiring-salamander-23b62b.netlify.app`).
Primary domain: `maverixmedical.com` (DNS + HTTPS cut over Tuesday).

- **Before Tuesday:** the `.netlify.app` subdomain IS the review URL. Every push
  to `main` builds there for review; nothing is user-facing until DNS flips.
- **After Tuesday:** `main` builds publish to `maverixmedical.com`. To preview
  a change before it goes public, either:
  - **Push a branch** — Netlify builds it at
    `<branch>--inspiring-salamander-23b62b.netlify.app` (Branch Deploys), OR
  - **Open a pull request** — Netlify builds a unique Deploy Preview URL, adds
    it as a check on the PR, merging to `main` publishes.
  Both preview types get `X-Robots-Tag: noindex, nofollow` (see `netlify.toml`).

## Before Tuesday (user actions — see plan §7-§9)

1. Confirm `EIFU_URL` in `site.config.ts` (flagged placeholder).
2. Decide bare `maverixmedical.com` vs `www.maverixmedical.com` as canonical.
   Currently set to bare — change `SITE_URL` if you prefer www, then set the
   matching primary in Netlify's Domain management on Tuesday.
3. MLR review: 10 new product meta descriptions (`# DRAFT-MLR`) + the Privacy
   Policy hosting paragraph (currently names GitHub Pages; must name Netlify
   before public cutover).
4. Netlify dashboard: Pretty URLs OFF, HTTPS on (Tuesday), CookieYes allowlist
   entries for BOTH `maverixmedical.com` and the `.netlify.app` subdomain.
5. Hero video (2.8 MB, autoplay) — compress and/or media-gate; it's the
   dominant bandwidth cost at 20 credits/GB.
