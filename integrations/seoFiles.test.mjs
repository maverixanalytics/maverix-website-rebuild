import { readFileSync } from "node:fs";
import { describe, it, expect } from "vitest";
import { SITEMAP_ORDER } from "./seoFiles.mjs";

/**
 * The sitemap's URL set, priorities and emission order are pinned to the
 * pre-migration sitemap so SEO equity carries over unchanged. The build-time
 * integration already fails loudly if a built page is missing from this list
 * (or vice versa); these tests guard the list's own invariants.
 */
describe("sitemap order", () => {
  const paths = SITEMAP_ORDER.map(([p]) => p);

  it("covers all 22 indexable pages (404 excluded)", () => {
    expect(SITEMAP_ORDER).toHaveLength(22);
  });

  it("contains no duplicate paths", () => {
    expect(new Set(paths).size).toBe(paths.length);
  });

  it("lists the homepage first at priority 1.0", () => {
    expect(SITEMAP_ORDER[0]).toEqual(["", "1.0"]);
  });

  it("never includes the 404 page", () => {
    expect(paths.some((p) => p.includes("404"))).toBe(false);
  });

  it("applies the legacy priority tiers", () => {
    const priorityOf = (p) => SITEMAP_ORDER.find(([x]) => x === p)?.[1];
    // Four category pages
    for (const p of ["products", "intervention", "risk-assessment", "diagnosis"]) {
      expect(priorityOf(p)).toBe("0.9");
    }
    // Product detail pages
    expect(paths.filter((p) => p.startsWith("products/"))).toHaveLength(10);
    for (const p of paths.filter((x) => x.startsWith("products/"))) {
      expect(priorityOf(p)).toBe("0.6");
    }
    // Secondary pages
    for (const p of ["team", "news", "careers", "contact-us"]) {
      expect(priorityOf(p)).toBe("0.8");
    }
    // Legal
    for (const p of ["terms-of-use", "privacy-policy", "regulatory-information"]) {
      expect(priorityOf(p)).toBe("0.3");
    }
  });

  it("emits extensionless routes only", () => {
    for (const p of paths) expect(p).not.toMatch(/\.html$/);
  });

  it("uses the corrected esophageal spelling", () => {
    expect(paths).toContain("products/bonastent-esophageal-stent");
    expect(paths).not.toContain("products/bonastent-esophogeal-stent");
  });

  it("uses route names that match the page titles", () => {
    for (const p of ["diagnosis", "risk-assessment", "intervention"]) {
      expect(paths).toContain(p);
    }
    for (const p of ["serpex", "diagnostics", "thoracent"]) {
      expect(paths).not.toContain(p);
    }
  });

  /**
   * The legacy *.html URLs were live on the public Webflow site, so they may be
   * indexed, bookmarked, or printed on collateral. Every one of them must keep
   * a 301 in netlify.toml — dropping a rule breaks an inbound link silently,
   * which is exactly the failure a test should catch.
   */
  it("keeps a 301 in netlify.toml for every legacy .html URL", () => {
    const toml = readFileSync(new URL("../netlify.toml", import.meta.url), "utf8");

    /** legacy stem (no leading slash, no .html) -> current route */
    const RENAMED = {
      serpex: "diagnosis",
      diagnostics: "risk-assessment",
      thoracent: "intervention",
      "products/bonastent-esophogeal-stent": "products/bonastent-esophageal-stent",
    };
    const currentToLegacy = Object.fromEntries(
      Object.entries(RENAMED).map(([legacy, current]) => [current, legacy]),
    );

    // Every sitemap route, expressed as the legacy URL that must redirect to it.
    const expected = paths
      .filter((p) => p !== "")
      .map((p) => [`/${currentToLegacy[p] ?? p}.html`, `/${p}`]);
    expect(expected).toHaveLength(21);

    for (const [from, to] of expected) {
      const idx = toml.indexOf(`from = "${from}"`);
      expect(idx, `missing redirect for ${from}`).toBeGreaterThan(-1);
      const rule = toml.slice(idx, idx + 200);
      expect(rule, `wrong target for ${from}`).toContain(`to = "${to}"`);
      expect(rule, `not a 301 for ${from}`).toContain("status = 301");
    }
  });
});
