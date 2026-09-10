import { describe, it, expect } from "vitest";
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";
import {
  SITE_URL,
  absoluteUrl,
  OG_IMAGES,
  FORM_ENDPOINT,
  MVX_EMAIL,
  THOR_EMAIL,
} from "./site.config";

describe("site config", () => {
  it("builds absolute canonical URLs on the production origin", () => {
    // Routes are extensionless as of 2026-08-18 (build.format 'directory').
    // A canonical that still ends in .html means SiteLayout regressed.
    expect(absoluteUrl("/")).toBe(`${SITE_URL}/`);
    expect(absoluteUrl("/diagnosis")).toBe(`${SITE_URL}/diagnosis`);
    expect(absoluteUrl("/products/ebus-needles")).toBe(
      `${SITE_URL}/products/ebus-needles`,
    );
  });

  it("has no trailing slash on SITE_URL (would produce // in canonicals)", () => {
    expect(SITE_URL.endsWith("/")).toBe(false);
    expect(absoluteUrl("/diagnosis")).not.toContain(".app//");
    expect(absoluteUrl("/diagnosis")).not.toContain(".com//");
  });

  it("maps og:image entries to plausible asset filenames", () => {
    for (const [page, file] of Object.entries(OG_IMAGES)) {
      expect(file).toMatch(/^og-[a-z-]+\.jpg$/);
      expect(page).not.toMatch(/\.html$/); // keys are route stems, not filenames
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

  it("routes the Maverix contact address to customer care", () => {
    expect(MVX_EMAIL).toBe("customercare@maverixmedical.com");
  });

  /**
   * Thoracent's address is a separate inbox on a separate domain, and the
   * Regulatory Information page sends complaints and adverse-event reports to
   * it. It must NOT get swept along by a Maverix-side branding change.
   */
  it("keeps the Thoracent address independent of the Maverix one", () => {
    expect(THOR_EMAIL).toBe("customercare@thoracent.com");
    expect(THOR_EMAIL).not.toBe(MVX_EMAIL);
  });

  /**
   * site.config.ts is the only place addresses may live. A hardcoded mailto in
   * a template silently survives every future address change — exactly how
   * contact@maverixmedical.com outlived its own retirement on the Contact Us
   * page until 2026-09-10. Content collections are excluded: legal pages quote
   * the Thoracent address as prose on purpose.
   */
  it("has no hardcoded maverixmedical.com address in any template", () => {
    const roots = ["src/pages", "src/components", "src/islands", "src/layouts"];
    const offenders: string[] = [];
    const walk = (dir: string) => {
      for (const entry of readdirSync(dir)) {
        const full = join(dir, entry);
        if (statSync(full).isDirectory()) walk(full);
        else if (/\.(astro|tsx|ts)$/.test(entry) && !entry.endsWith(".test.ts")) {
          if (/[\w.-]+@maverixmedical\.com/.test(readFileSync(full, "utf8"))) {
            offenders.push(full);
          }
        }
      }
    };
    for (const r of roots) walk(r);
    expect(offenders).toEqual([]);
  });
});