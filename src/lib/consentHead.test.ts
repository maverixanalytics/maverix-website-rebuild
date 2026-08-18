import { describe, it, expect } from "vitest";
import { buildConsentHead } from "./consentHead";
import { CY_CLIENT, GA4_ID } from "@/config/site.config";

/**
 * The consent block is ORDER-SENSITIVE and compliance-relevant: Consent Mode
 * defaults must register before CookieYes, and CookieYes before the GA4 tag.
 * Getting this wrong sets a _ga cookie on first paint, before consent.
 * These assertions exist so a future refactor can't silently reorder it.
 */
describe("consent head block", () => {
  const html = buildConsentHead();

  it("registers Consent Mode defaults before CookieYes and before GA4", () => {
    const defaults = html.indexOf("gtag('consent', 'default'");
    const cookieyes = html.indexOf("cdn-cookieyes.com");
    const ga4 = html.indexOf("googletagmanager.com/gtag/js");

    expect(defaults).toBeGreaterThan(-1);
    expect(cookieyes).toBeGreaterThan(-1);
    expect(ga4).toBeGreaterThan(-1);
    expect(defaults).toBeLessThan(cookieyes);
    expect(cookieyes).toBeLessThan(ga4);
  });

  it("denies every non-essential storage type by default", () => {
    for (const key of [
      "ad_storage",
      "ad_user_data",
      "ad_personalization",
      "analytics_storage",
      "functionality_storage",
      "personalization_storage",
    ]) {
      expect(html).toMatch(new RegExp(`${key}:\\s*'denied'`));
    }
    // security_storage is the one legitimately granted by default.
    expect(html).toMatch(/security_storage:\s*'granted'/);
  });

  it("keeps the CookieYes element id the vendor script looks itself up by", () => {
    expect(html).toContain('id="cookieyes"');
  });

  it("interpolates the configured client and measurement IDs", () => {
    expect(html).toContain(CY_CLIENT);
    expect(html).toContain(GA4_ID);
  });

  it("anonymizes IPs and sets wait_for_update", () => {
    expect(html).toContain("anonymize_ip");
    expect(html).toMatch(/wait_for_update:\s*500/);
  });
});

describe("_gl stripping", () => {
  const head = buildConsentHead();

  it("strips the _gl linker parameter", () => {
    expect(head).toContain("searchParams.delete('_gl')");
    expect(head).toContain("history.replaceState");
  });

  /**
   * Stripping before gtag.js has read _gl would silently break cross-page
   * session stitching for every visitor who has not accepted cookies — the
   * exact group url_passthrough exists to serve. Bind to `load`, never earlier.
   */
  it("defers stripping until after gtag.js has loaded", () => {
    expect(head).toContain("window.addEventListener('load'");
    const gtagConfig = head.indexOf("gtag('config'");
    const strip = head.indexOf("searchParams.delete('_gl')");
    expect(gtagConfig).toBeGreaterThan(-1);
    expect(strip).toBeGreaterThan(gtagConfig);
  });

  it("keeps url_passthrough on (stripping is cosmetic, not a consent change)", () => {
    expect(head).toContain("gtag('set', 'url_passthrough', true)");
  });
});
