// @ts-check
import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import mdx from "@astrojs/mdx";
import { SITE_URL } from "./src/config/site.config.ts";
import { maverixSeoFiles } from "./integrations/seoFiles.mjs";

// Netlify-only hosting (plan §1.2 / §7):
// - served from the domain root -> NO `base`
// - build.format 'file' -> exact legacy URLs (serpex.html, products/foo.html)
// - trailingSlash 'never' -> canonicals match served .html paths exactly
//   (Netlify "Pretty URLs" asset optimization must stay OFF in the dashboard)
export default defineConfig({
  site: SITE_URL,
  trailingSlash: "never",
  build: { format: "file" },
  integrations: [react(), mdx(), maverixSeoFiles(SITE_URL)],
});
