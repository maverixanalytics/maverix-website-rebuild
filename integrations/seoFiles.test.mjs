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
    for (const p of ["products.html", "thoracent.html", "diagnostics.html", "serpex.html"]) {
      expect(priorityOf(p)).toBe("0.9");
    }
    // Product detail pages
    expect(paths.filter((p) => p.startsWith("products/"))).toHaveLength(10);
    for (const p of paths.filter((x) => x.startsWith("products/"))) {
      expect(priorityOf(p)).toBe("0.6");
    }
    // Secondary pages
    for (const p of ["team.html", "news.html", "careers.html", "contact-us.html"]) {
      expect(priorityOf(p)).toBe("0.8");
    }
    // Legal
    for (const p of ["terms-of-use.html", "privacy-policy.html", "regulatory-information.html"]) {
      expect(priorityOf(p)).toBe("0.3");
    }
  });

  it("preserves the historical filenames, including the known typo slug", () => {
    // Renaming any of these breaks inbound links and SEO equity.
    expect(paths).toContain("products/bonastent-esophogeal-stent.html"); // sic
    expect(paths).toContain("serpex.html"); // = Diagnosis
    expect(paths).toContain("diagnostics.html"); // = Risk Assessment
    expect(paths).toContain("thoracent.html"); // = Intervention
  });
});
