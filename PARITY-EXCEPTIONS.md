# Parity Exceptions — Astro rebuild vs legacy build.py site

Every difference between the new build and the legacy generated site, per the
migration plan's gate. Anything NOT listed here is byte-identical in visible
text and pixel-identical in the visual harness. Verified 2026-08-15.

## Content

1. **Product meta descriptions (10) are NEW COPY — pending MLR.** The legacy
   descriptions were `desc_paras[0][:150]` truncations, mid-word and
   entity-corrupted (`&reg;` visible in SERPs). Each new description is
   flagged `# DRAFT-MLR` in its product .mdx frontmatter. Route through
   regulatory review before cutover.
2. **HTML entities normalized to UTF-8** (`&mdash;`→—, `&reg;`→®, …).
   Rendered text is identical; the parity checker normalizes both sides
   before diffing, so this cannot mask a real edit.

## Structure (invisible at rest)

3. **team.html DOM order:** each bio modal now sits adjacent to its trigger
   card instead of all modals appended at page bottom. Word-multiset
   identical; hidden at rest; better source order for assistive tech.
4. **Stat numbers render as `<span class="stat-number">`** inside the
   StatCountUp island (legacy: `<div>`). Styling is class-driven;
   astro-island wrappers are `display:contents`; layout unchanged
   (visual harness heights identical).
5. **dsCard annotation comment** sits just inside `<head>` rather than
   before `<!doctype>` (Astro cannot emit pre-doctype content). The
   annotation text is unchanged.
6. **Internal links are root-absolute** (`/diagnosis`) instead of relative
   (`../serpex.html`). Required by the Netlify-only, no-base architecture.

## Behavior — a11y upgrades (the one sanctioned exception class)

7. **Escape now returns focus** to the triggering element when closing the
   mobile menu and bio modals (legacy Escape closed without focus return).
8. **Tab bars** gain `role=tablist/tab/tabpanel`, `aria-selected`, and
   arrow-key navigation. Click behavior unchanged.
9. **Global `:focus-visible` ring** (legacy styled focus only on form
   fields and product cards).
10. **Reduced-motion coverage is complete** — all transitions/animations
    gated centrally; legacy left its largest motions (card flex-expand)
    un-gated. Reveal-on-scroll still runs only under
    `prefers-reduced-motion: no-preference`, as legacy.
11. **Careers form fields** gain `aria-label`s (labels/placeholders kept
    verbatim).

## Behavior — parity-preserved quirks (deliberate)

12. The news top-link **navigates** on mobile (no accordion) — legacy quirk
    kept.
13. The journey bar renders per the LIVE cascade (v47 overriding v27's
    mobile caps) — the known legacy bug is reproduced, not "fixed";
    fixing it is the open "journey proportions" item.
14. Reveal stagger delay inside island-wrapped cards computes within the
    island wrapper (each card delay 0ms vs legacy 0/70/140ms stagger).
    Same class mechanics; sub-second cosmetic difference during scroll-in.

## Head / SEO

15. **Canonical/og:url/sitemap origin** is the Netlify URL (config
    constant) instead of `maverixanalytics.github.io/maverix-website-rebuild`
    — the point of the hosting change. Paths, priorities, and sitemap
    order are pinned to legacy exactly.
16. **404 root-absolute rewrite apparatus deleted** — Netlify serves
    /404.html from the domain root; plain root-absolute paths replace the
    legacy `BASE_PATH` regex.

## Architecture deviations from the migration plan

18. **Global flattened CSS instead of CSS Modules.** The plan specified CSS
    Modules; the build ships 14 plain global stylesheets in
    `src/styles/ported/`. The legacy global class names are a contract shared
    by the CSS, the islands' JS state classes, and third-party scripts
    (CookieYes, SociableKit), so scoping them would have meant renaming them
    and forfeiting byte-parity. The cascade was *flattened* (winner-per-property,
    dead overrides dropped) rather than scoped. One styling approach is used
    consistently throughout and tokens are centralized in `:root`, so the
    "pick one and stay consistent" rule holds. See `CONVENTIONS.md`.
19. **Media lives at the repo root** (`assets/`, `images/`) and is copied into
    `dist/` by the Netlify build command, rather than sitting in `public/` per
    Astro convention. This avoided re-uploading 38 MB through the browser
    during migration and preserves the media's git history. `npm run predev`
    mirrors them into `public/` for local dev.

21. **URL scheme changed (2026-08-18).** The legacy `.html` extensions were
    dropped (`build.format:'directory'`) and three pages were renamed to match
    their titles — `serpex`→`diagnosis`, `diagnostics`→`risk-assessment`,
    `thoracent`→`intervention` — plus the `esophogeal`→`esophageal` typo fix.
    This is the ONE deliberate break from legacy URL parity. It was taken
    before the Webflow→Netlify cutover, when the redirect cost is lowest: all
    22 legacy URLs 301 to their new routes (`netlify.toml`), so indexed links
    and printed collateral keep working. `OG_IMAGES` values still use the old
    `og-serpex/og-diagnostics/og-thoracent` filenames on purpose — those
    binaries are already published under those names.

## Deferred to post-cutover

20. React Compiler is not yet enabled; `MvxForm` still uses manual `useState`
    rather than React 19 `useActionState`; the 2.83 MB hero video still
    autoplays; images lack explicit `width`/`height`. All four are tracked
    against the current React standards and deliberately held until after the
    domain cutover, since each touches runtime behavior.

## Dead code intentionally not ported

17. Carousel JS + `.on` dots (no markup, no CSS in legacy); orphan CSS
    (`.cards3`, `.benefit-cell`, `.altrow`, `.newsitem`, `.serpex-two`,
    `.brandlock`, `.pd-grid`, `.dropdown-in.slim`, v19/v20 self-cancelled
    `::after`, v28's unreachable `.close-b`); unused tokens (12) and
    aliases (7); `PRODUCTS_HERO`, `IMG["netis2"]`, dead `P` locals.
