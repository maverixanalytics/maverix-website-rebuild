/**
 * Single source of truth for every environment-ish constant.
 * Domain cutover = change SITE_URL only (plan §1.2).
 *
 * Replaces the constants block at the top of legacy src/build.py.
 */

/**
 * Production origin.
 *
 * DNS cuts over to Netlify on Tuesday; HTTPS is enabled the same day. Setting
 * this to the final maverixmedical.com URL now means canonical/og:url/sitemap
 * are correct from the moment DNS flips — no second rebuild required.
 *
 * Between now and Tuesday, canonicals in the review build on
 * inspiring-salamander-23b62b.netlify.app will point at maverixmedical.com,
 * which is fine: Netlify auto-serves `X-Robots-Tag: noindex` on the .netlify.app
 * subdomain whenever a custom domain is set as primary (already configured),
 * so the preview subdomain won't get crawled.
 *
 * If you decide www is canonical instead of the bare domain, change to
 * https://www.maverixmedical.com and configure Netlify to redirect one to the
 * other (dashboard: Domain management → Domains → set primary).
 */
export const SITE_URL = "https://maverixmedical.com";

/**
 * Form endpoint. Empty string = mailto fallback (the CURRENT live behavior, and a
 * published Privacy Policy commitment — see plan §9 risk 12 before ever setting this).
 */
export const FORM_ENDPOINT = "";

/**
 * Maverix-facing contact address — footer, Contact Us, Careers, and the
 * ContactBlock on product / risk-assessment pages all use this ONE constant.
 *
 * Was split across CONTACT_EMAIL (contact@maverixmedical.com) and MVX_EMAIL
 * until 2026-09-10, when the user moved everything to customer care. The two
 * constants were merged rather than both set to the same string: two names for
 * one address is how they drift apart again.
 */
export const MVX_EMAIL = "customercare@maverixmedical.com";

/**
 * Thoracent's own customer-care address. Deliberately SEPARATE from MVX_EMAIL
 * and NOT changed with it: different domain, different inbox, and the
 * Regulatory Information page routes device complaints and adverse-event
 * reports here. Changing this is a regulatory decision, not a branding one.
 */
export const THOR_EMAIL = "customercare@thoracent.com";
export const THOR_PHONE = "(888) 978-0232";

/** Thoracent "Distributed by" lockup shown on every product page right rail. */
export const THOR_LOGO = "/assets/thoracent-by-maverix-logo.png";

/** eIFU library link on the Regulatory Information page.
 *  TODO(user): UNVERIFIED placeholder carried over from build.py — confirm before cutover
 *  (plan §9 risk 11). */
export const EIFU_URL = "https://thoracent.com/ifu/";

// --- Analytics / consent (order-sensitive at render time — see consentHead.ts) ---
export const CY_CLIENT = "b0481c682f112a57de13418a";
export const GA4_ID = "G-QFMYMJ9YWX";

// --- Careers page third parties ---
export const SK_MAVERIX = "25606228";
export const SK_THORACENT = "25605798";
export const LI_MAVERIX =
  "https://www.linkedin.com/company/maverix-medical/jobs/";
export const LI_THORACENT = "https://www.linkedin.com/company/thoracent/jobs/";

/**
 * Pages that ship an og:image. Key = page stem, value = filename under /assets.
 * Build fails if a mapped file is missing (fixes the legacy silent-404 hazard).
 */
export const OG_IMAGES: Record<string, string> = {
  index: "og-index.jpg",
  products: "og-products.jpg",
  // Keys follow the 2026-08-18 route rename; the image FILENAMES still carry
  // the legacy stems (og-thoracent/og-diagnostics/og-serpex) because those are
  // binaries already published under those names. Renaming the files buys
  // nothing and breaks any cached social-card scrape.
  intervention: "og-thoracent.jpg",
  "risk-assessment": "og-diagnostics.jpg",
  diagnosis: "og-serpex.jpg",
  team: "og-team.jpg",
  news: "og-news.jpg",
  careers: "og-careers.jpg",
  "contact-us": "og-contact-us.jpg",
};

/** Absolute URL for canonicals / og:url / sitemap locs. */
export function absoluteUrl(path: string): string {
  return new URL(path, SITE_URL).href;
}
