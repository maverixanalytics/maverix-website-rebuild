import { describe, it, expect } from "vitest";
import { SITE_URL, absoluteUrl, OG_IMAGES, FORM_ENDPOINT } from "./site.config";

describe("site config", () => {
  it("builds absolute canonical URLs on the production origin", () => {
    expect(absoluteUrl("/")).toBe(`${SITE_URL}/`);
    expect(absoluteUrl("/serpex.html")).toBe(`${SITE_URL}/serpex.html`);
    expect(absoluteUrl("/products/ebus-needles.html")).toBe(
      `${SITE_URL}/products/ebus-needles.html`,
    );
  });

  it("has no trailing slash on SITE_URL (would produce // in canonicals)", () => {
    expect(SITE_URL.endsWith("/")).toBe(false);
    expect(absoluteUrl("/serpex.html")).not.toContain(".app//");
    expect(absoluteUrl("/serpex.html")).not.toContain(".com//");
  });

  it("maps og:image entries to plausible asset filenames", () => {
    for (const [page, file] of Object.entries(OG_IMAGES)) {
      expect(file).toMatch(/^og-[a-z-]+\.jpg$/);
      expect(page).not.toMatch(/\.html$/); // keys are stems, not filenames
    }
  });

  /**
   * The published Privacy Policy states the forms "do not submit to a server we
   * control" — true only while FORM_ENDPOINT is empty. If this ever becomes
   * non-empty, the policy copy must be revised FIRST (plan §9 risk 12).
   */
  it("keeps FORM_ENDPOINT empty while the privacy policy claims mailto-only", () => {
    expect(FORM_ENDPOINT).toBe("");
  });
});
