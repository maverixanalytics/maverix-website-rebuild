# Maverix Medical — Astro rebuild

The [maverixmedical.com](https://www.maverixmedical.com) site rebuilt from the
legacy Python generator (`build.py` + `theme.css.tpl`) as an **Astro 6 +
React islands** app, per `REACT-MIGRATION-PLAN.md`. All 23 pages, byte-parity
on visible text, pixel-parity in the visual harness, targeting **Netlify-only**
hosting.

URLs are extensionless as of 2026-08-18 (`/diagnosis`, not `/serpex.html`);
every legacy URL 301s to its new route — see `netlify.toml`.

Read `CONVENTIONS.md` before changing anything; `PARITY-EXCEPTIONS.md` lists
every known difference from the legacy site.

## Commands

```bash
npm ci               # Node >= 22.12
npm run build        # → dist/ (23 pages + sitemap.xml/robots.txt/webmanifest)
npm run lint         # ESLint (flat config, react-hooks compiler rules)
npm run test         # Vitest unit tests
npm run format       # Prettier
npm run check        # everything: astro check + tsc --noEmit + eslint + vitest
node scripts/verify/interact.mjs   # interaction harness (needs a prior build)
```

CI (`.github/workflows/ci.yml`) runs types, lint, tests and a full build on
every push and PR. It deploys nothing — Netlify owns publishing.

**Styling note:** this project uses global flattened CSS, *not* CSS Modules.
That's deliberate; see the boxed explanation in `CONVENTIONS.md` before
changing it.

## Layout

- `src/content/` — ALL copy as schema-validated collections (products, news,
  leaders, legal pages) + citation/reference data. Editing copy = editing a
  content file; the build fails on schema violations.
- `src/pages/` — one file per route. Routes are extensionless and named after
  the page title (`/diagnosis`, `/risk-assessment`, `/intervention`). The
  legacy `serpex.html` / `diagnostics.html` / `thoracent.html` /
  `bonastent-esophogeal-stent` URLs all 301 to them via `netlify.toml`;
  changing a route means adding a redirect in the same commit.
- `src/components/` — static Astro components; `src/islands/` — the seven
  React islands (nav, tabs, modals, cards, count-up, forms).
- `src/styles/ported/` — the legacy stylesheet flattened (winner-per-property,
  dead overrides dropped) into per-area files; `tokens.css` is the palette.
- `src/config/site.config.ts` — the ONLY place URLs/IDs/emails live.
  **Domain cutover = change `SITE_URL`, rebuild.**
- `public/` — legacy `assets/` + `images/` verbatim (not in the source zip if
  you received one — copy from the legacy repo).

## ⚠️ Production publishing is LOCKED

Netlify auto-publishing is **locked** (Deploys → "Auto Publishing Locked").
Pushes to `main` still **build**, but they do **not go live** until a human
clicks **Publish deploy** on that build in the Netlify Deploys page.

This is deliberate: the site is under MLR/regulatory review, and no copy or
layout change should reach the public domain without an explicit approval
step. Do not unlock it to "make deploys easier."

To ship a change: push → wait for the build → open the deploy in Netlify →
review the deploy preview link → **Publish deploy**.

## Review workflow

Netlify site: `inspiring-salamander-23b62b`
(`https://inspiring-salamander-23b62b.netlify.app`).
Primary domain: `maverixmedical.com` (DNS + HTTPS cut over Tuesday).

- **Before Tuesday:** the `.netlify.app` subdomain IS the review URL. Every push
  to `main` builds there for review; nothing is user-facing until DNS flips.
- **After Tuesday:** `main` builds are held unpublished by the lock above, so
  production never changes without a click. For an isolated preview URL per
  change (recommended for anything a reviewer needs to see in context), use
  either:
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
