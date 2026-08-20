/**
 * Legacy Webflow anchor redirects.
 *
 * The old Webflow site kept all three product families on ONE page and linked
 * to them by fragment (/products#thoracent). Each family is now its own page,
 * so those inbound links — indexed, bookmarked, and printed on collateral —
 * need to reach the new routes.
 *
 * WHY THIS ISN'T IN netlify.toml:
 * A URL fragment is never transmitted. The browser strips everything from the
 * `#` onward before the request leaves the machine, so `/products#thoracent`
 * arrives at Netlify as a bare `GET /products`. No server-side rule — Netlify
 * [[redirects]], GoDaddy forwarding, Cloudflare Transform Rules, nginx — can
 * read it, because none of them ever receive it. The browser is the only place
 * this information exists, so the redirect has to happen here.
 *
 * CONSEQUENCE: this is a client-side `location.replace()`, NOT a 301. The
 * response for /products has already gone out as a 200 by the time this runs.
 * Crawlers won't treat it as a permanent move and no link equity transfers.
 * For human traffic off old collateral that's the expected tradeoff; if these
 * paths ever need real 301s, the destinations have to become real paths
 * (e.g. /products/thoracent) rather than fragments.
 *
 * Must run inline in <head>, before paint — see products.astro. If this is
 * ever moved into the bundled module graph it will be deferred, and visitors
 * will see the products page render before being redirected away.
 */

/** Legacy fragment (lowercase) -> current route. */
const LEGACY_HASH_ROUTES: Record<string, string> = {
    "#thoracent": "/intervention/",
    "#maverix-diagnostics": "/risk-assessment/",
    "#maverix-biopsy-tools": "/diagnosis/",
};

/**
 * The redirect as a self-contained inline snippet.
 *
 * Rendered into <head> via `set:html` so it runs before paint. Built from
 * LEGACY_HASH_ROUTES above so the mapping is declared exactly once — add a
 * legacy fragment there and it flows through to the page automatically.
 *
 * replace() rather than assign(): keeps /products out of session history so
 * the Back button returns the visitor to wherever they came from instead of
 * re-triggering this redirect and trapping them in a loop.
 */
export function buildLegacyHashRedirectScript(): string {
    return `<script>(function(){var m=${JSON.stringify(
        LEGACY_HASH_ROUTES,
    )};var d=m[location.hash.toLowerCase()];if(d)location.replace(d);})();</script>`;
}