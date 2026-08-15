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
</script>`;
}
