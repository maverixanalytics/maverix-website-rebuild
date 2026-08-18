import { CY_CLIENT, GA4_ID } from "@/config/site.config";

/**
 * Consent Mode v2 + CookieYes + GA4 head block (plan §5.1).
 *
 * ORDER IS LOAD-BEARING and mirrors legacy build.py CONSENT_HEAD verbatim:
 *   1. Consent Mode defaults (all denied) MUST register before any Google tag
 *   2. CookieYes (id="cookieyes" — the script looks itself up by that id)
 *   3. GA4 gtag.js + config
 * Loading GA4 first sets _ga on first paint before consent — the exact bug the
 * legacy source warns about. Rendered via set:html in SiteLayout so Astro
 * cannot reorder, bundle, or prepend to it (define:vars would).
 *
 * If a CSP is ever enabled, these inline scripts need hashes (plan §5.1 note).
 *
 * The 4th block strips GA4's `_gl` linker parameter from the address bar. It is
 * NOT optional cosmetics: `url_passthrough` (set above) tells GA4 to carry the
 * visitor identifier in the URL instead of a cookie whenever analytics consent
 * is denied — which is the default state until the banner is accepted — so
 * every internal click mints a URL like `/diagnosis?_gl=1*rvnzk7*...`. Those
 * URLs get bookmarked, pasted into emails, and printed. Stripping runs on
 * `load`, AFTER the async gtag.js has initialised and read the parameter, so
 * cross-page session stitching is preserved; GA4 re-decorates outbound links
 * from in-memory state, not from the current URL. Do not move it earlier.
 */
export function buildConsentHead(): string {
  return `<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  ad_storage: 'denied',
  ad_user_data: 'denied',
  ad_personalization: 'denied',
  analytics_storage: 'denied',
  functionality_storage: 'denied',
  personalization_storage: 'denied',
  security_storage: 'granted',
  wait_for_update: 500
});
gtag('set', 'ads_data_redaction', true);
gtag('set', 'url_passthrough', true);
</script>
<script id="cookieyes" src="https://cdn-cookieyes.com/client_data/${CY_CLIENT}/script.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=${GA4_ID}"></script>
<script>
gtag('js', new Date());
gtag('config', '${GA4_ID}', { anonymize_ip: true });
</script>
<script>
window.addEventListener('load', function () {
  try {
    var url = new URL(window.location.href);
    if (!url.searchParams.has('_gl')) return;
    url.searchParams.delete('_gl');
    var qs = url.searchParams.toString();
    window.history.replaceState(
      window.history.state,
      '',
      url.pathname + (qs ? '?' + qs : '') + url.hash
    );
  } catch (e) {}
});
</script>`;
}
