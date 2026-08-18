# Maverix Astro — Repo Conventions (read before writing any page)

Astro 6.4.8 + @astrojs/react + @astrojs/mdx. TypeScript strict. Node 22.
Build: `npx astro build` → dist/ with extensionless URLs
(`build.format:'directory'`, `trailingSlash:'never'`, no `base` — Netlify
serves from root).

## Non-negotiables

1. **Copy is regulated.** Body copy is extracted VERBATIM from legacy pages
   (entities → UTF-8). Never paraphrase, trim, or "fix" copy. New copy (only
   meta descriptions) is flagged `# DRAFT-MLR`.
2. **URLs changed once, on 2026-08-18, and are now frozen again.** Routes are
   extensionless and named after the page title: `/diagnosis` (was
   `serpex.html`), `/risk-assessment` (was `diagnostics.html`),
   `/intervention` (was `thoracent.html`), and
   `/products/bonastent-esophageal-stent` (typo `esophogeal` corrected).
   EVERY legacy `.html` URL 301s to its new route in `netlify.toml`, and a
   Vitest case fails if any rule goes missing. Adding or renaming a route means
   adding a redirect in the same commit.
3. **Three footnote schemes, never merged:** homepage `sup.cite` (external
   links, `Cite.astro` when built), Risk Assessment `sup.ref` (in-page
   `#ref-N`), Narwhal `*` (stat+disclaimer bound in one record).
4. **Internal links are root-absolute and extensionless** (`/diagnosis`,
   `/products/x`, `/` for home). Assets: `/images/...`, `/assets/...`.
5. Head/meta comes ONLY from `SiteLayout` props — never hand-roll head tags.

## Page pattern

```astro
---
import SiteLayout from "@/layouts/SiteLayout.astro";
import Btn from "@/components/Btn.astro";
import "@/styles/ported/category-shared.css";   // page-scope CSS imports
---
<SiteLayout path="serpex" title="Diagnosis – Maverix Medical"
  description="…legacy meta description verbatim…"
  dsGroup="Pages" dsSubtitle="…">
  ...body markup, legacy class names verbatim...
</SiteLayout>
```

`path` = output stem ("index", "team", "products/foo"); drives canonical +
og:url + og:image map. `noindex` prop only for 404.

## Existing shared pieces (USE, don't duplicate)

- `SiteLayout.astro` — chrome + head + reveal script (reveal runs site-wide).
- `Btn.astro` — `.btn` atom (`href`, `label`, `dark`).
- `ContactBlock.astro` (`email?`, `showPhone?`), `BrandLockup.astro`,
  `SpecTable.astro`, `VideoEmbed.astro`, `Bodytext.astro` (MDX p→.bodytext).
- Islands: `SiteNav` (chrome, done), `TabBar` (via `TabBarShell.astro`),
  `ExpandCard` (`cardClass`, children; hydrate `client:media="(max-width: 920px)"`).
- Content: `products` + `news` collections (`src/content.config.ts`),
  `src/data/productGroups.ts` (card labels with real ®/™).
- Config: `src/config/site.config.ts` (emails, phone, EIFU_URL, SociableKit,
  FORM_ENDPOINT — mailto fallback is a Privacy Policy commitment).

## CSS rules

> **This project uses GLOBAL flattened CSS, not CSS Modules.** That is a
> deliberate deviation — do not "fix" it by converting to `.module.css`
> without reading this. The legacy global class names (`.dropdown`, `.mcol`,
> `.pcard`, `.is-active`, `.open`) are a live contract shared by three things:
> the flattened CSS, the island state classes toggled in JS, and third-party
> scripts (CookieYes binds to `.cky-banner-element`; the SociableKit widget
> injects `.sk-ww-linkedin-page-jobs`, which `.jobs-empty` keys off). Scoping
> them means renaming them, which breaks that contract and the byte-parity
> guarantee against the legacy site. The specificity problem was solved by
> *flattening* the cascade (winner-per-property, dead overrides dropped)
> rather than by scoping it. Converting to Modules is a legitimate future
> project — it just has to be done deliberately, with the harnesses green.

- Ported flattened CSS lives in `src/styles/ported/*.css`, imported per page.
  Files: chrome-header, chrome-footer, btn (all three loaded by the chrome on
  every page), hero-thin, product-detail (+ text-atoms), category-shared.
- **Never co-load `product-detail.css` with `category-shared.css`** — they
  flatten `section.band>.container` differently (pd: `padding:0`; category:
  the real gutter ladder).
- New page-specific CSS goes in a NEW file `src/styles/ported/<page>.css`,
  flattened winner-per-property from `/home/claude/maverix-legacy/theme.css`.
  Never redeclare a selector another ported file owns.
- Tokens from `src/styles/tokens.css` replace exact-match literals.
  Breakpoints 1080/920/560 (Narwhal keeps 1000; zoomout keeps 640/600).
- State classes JS toggles keep legacy names: `.open`, `.sub-open`,
  `.is-active`, `.is-in-view`.

## Islands (React)

- Boundary rule: an island owns its trigger AND its target (slots carry
  static content through). No `getElementById`/`parentElement` reaches.
- Hydrate minimally: `client:media` for mobile-only, `client:visible` for
  in-page widgets, `client:idle` for modals (display:none never intersects —
  client:visible would NEVER hydrate them).
- Props are serializable data; one component per file; typed function
  components; no `React.FC`; state class names from the legacy contract.

## Verification (every page, before declaring done)

Visible-text parity vs `/home/claude/maverix-legacy/<page>.html`:
strip tags/scripts/styles, unescape entities, collapse whitespace, compare.
Must be IDENTICAL (report any intended exception). Then `npx astro build`
must stay green with zero TS errors (`npx tsc --noEmit`).
