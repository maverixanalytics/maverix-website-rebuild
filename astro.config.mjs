// @ts-check
import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import mdx from "@astrojs/mdx";
import { SITE_URL } from "./src/config/site.config.ts";
import { maverixSeoFiles } from "./integrations/seoFiles.mjs";

// Netlify-only hosting (plan §1.2 / §7):
// - served from the domain root -> NO `base`
// - build.format 'directory' -> extensionless URLs (/diagnosis, /products/foo)
// - trailingSlash 'never' -> canonicals have no trailing slash
//   Legacy .html URLs are 301'd in netlify.toml (see [[redirects]]).
export default defineConfig({
  site: SITE_URL,
  trailingSlash: "never",
  build: { format: "directory" },
  integrations: [react(), mdx(), maverixSeoFiles(SITE_URL)],
});
