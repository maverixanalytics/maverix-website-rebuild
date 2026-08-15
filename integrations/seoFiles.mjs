// @ts-check
import { writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

/**
 * Generates sitemap.xml, robots.txt, and assets/site.webmanifest at build
 * time (plan §5.4) — replacing legacy build_seo(). Emission order and the
 * priority map are PINNED to the legacy sitemap exactly (same format:
 * <loc> + <priority> only, no changefreq/lastmod). 404 excluded.
 */

/** Legacy emission order (build-call order in build.py). */
const SITEMAP_ORDER = [
  ["", "1.0"],
  ["products.html", "0.9"],
  ["thoracent.html", "0.9"],
  ["diagnostics.html", "0.9"],
  ["serpex.html", "0.9"],
  ["products/y-shaped-tracheal-stent.html", "0.6"],
  ["products/bonastent-tracheobronchial-stent.html", "0.6"],
  ["products/ebus-needles.html", "0.6"],
  ["products/biopsy-forceps.html", "0.6"],
  ["products/hydro-slide-pulmonary-guidewire.html", "0.6"],
  ["products/hilzo-tts-esophageal-stent.html", "0.6"],
  ["products/hilzo-ues-esophageal-stent.html", "0.6"],
  ["products/bonastent-esophogeal-stent.html", "0.6"],
  ["products/netis-retrieval-net.html", "0.6"],
  ["products/narwhal-cryo-system.html", "0.6"],
  ["team.html", "0.8"],
  ["news.html", "0.8"],
  ["careers.html", "0.8"],
  ["contact-us.html", "0.8"],
  ["terms-of-use.html", "0.3"],
  ["privacy-policy.html", "0.3"],
  ["regulatory-information.html", "0.3"],
];

/**
 * @param {string} siteUrl absolute origin, no trailing slash
 * @returns {import('astro').AstroIntegration}
 */
export function maverixSeoFiles(siteUrl) {
  const base = siteUrl.replace(/\/$/, "");
  return {
    name: "maverix-seo-files",
    hooks: {
      "astro:build:done": async ({ dir, pages, logger }) => {
        const outDir = fileURLToPath(dir);

        // Guard: every sitemap entry must exist as a built page, and every
        // built page (except 404) must be in the sitemap — fails loudly on
        // drift instead of silently shipping a stale map.
        const built = new Set(
          pages.map((p) => p.pathname.replace(/\/$/, "")),
        );
        const wanted = new Set(
          SITEMAP_ORDER.map(([p]) => p.replace(/\.html$/, "").replace(/\/$/, "")),
        );
        for (const w of wanted) {
          if (!built.has(w)) throw new Error(`sitemap entry not built: "${w}"`);
        }
        for (const b of built) {
          if (b !== "404" && !wanted.has(b))
            throw new Error(`built page missing from sitemap: "${b}"`);
        }

        const urls = SITEMAP_ORDER.map(
          ([p, pri]) =>
            `  <url><loc>${base}/${p}</loc><priority>${pri}</priority></url>`,
        ).join("\n");
        const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`;
        await writeFile(path.join(outDir, "sitemap.xml"), sitemap);

        const robots = `User-agent: *\nAllow: /\n\nSitemap: ${base}/sitemap.xml\n`;
        await writeFile(path.join(outDir, "robots.txt"), robots);

        const manifest = {
          name: "Maverix Medical",
          short_name: "Maverix",
          start_url: `${base}/`,
          display: "standalone",
          theme_color: "#0D1418",
          background_color: "#F2F2F6",
          icons: [
            { src: "favicon-192.png", sizes: "192x192", type: "image/png" },
            { src: "favicon-512.png", sizes: "512x512", type: "image/png" },
          ],
        };
        await mkdir(path.join(outDir, "assets"), { recursive: true });
        await writeFile(
          path.join(outDir, "assets", "site.webmanifest"),
          JSON.stringify(manifest, null, 2) + "\n",
        );
        logger.info("sitemap.xml, robots.txt, assets/site.webmanifest written");
      },
    },
  };
}
