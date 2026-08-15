/**
 * Content collections — Astro 6 Content Layer API (plan §2).
 * Every content type is schema-validated; the build FAILS on invalid data.
 * z comes from 'astro/zod' (the astro:content export is deprecated in v6).
 */
import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

/**
 * Products — one MDX file per product page (plan §2.1).
 * Slug = filename, which preserves legacy URLs verbatim, INCLUDING the
 * historical typo `bonastent-esophogeal-stent` (do not "fix" it — plan §1.2).
 */
const products = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/products" }),
  schema: z.object({
    /** Page H1 / <title> form (no ®/™ on pages today). */
    name: z.string(),
    /**
     * Listing-card form — cards say "Bonastent®"/"Hilzo™" where pages don't.
     * Two fields keep the trademark decision explicit for MLR (plan §2.1 D-note).
     */
    cardName: z.string().optional(),
    /** Hand-written; replaces the legacy desc_paras[0][:150] truncation. */
    metaDescription: z.string().max(160),
    /** Breadcrumb parent: thoracent = Intervention, serpex = Diagnosis. */
    parent: z.enum(["thoracent", "serpex"]),
    /** "Distributed by" rail + "Thoracent by Maverix" title suffix. */
    distBy: z.boolean().default(true),
    /**
     * 510(k) clearance — absence must be an EXPLICIT state, never a missing key:
     * a K-number, 'pending' (number not yet supplied), or 'none'.
     */
    k510: z.union([
      z.string().regex(/^K\d{6}$/),
      z.literal("pending"),
      z.literal("none"),
    ]),
    mfgLogo: z.enum(["hilzo", "bonastent", "microtech"]).optional(),
    /** Joined with "510(k) {k510}." by ONE space into one <p class="mfg-note">. */
    mfgNote: z.string().optional(),
    /** Rx-only / availability statements (legacy p.rxnote). */
    rxNote: z.string().optional(),
    features: z.array(z.string()).min(1),
    /** Root-absolute paths (/images/..., /assets/...). */
    images: z.array(z.string().regex(/^\//)),
    resources: z
      .array(z.object({ label: z.string(), url: z.string() }))
      .default([]),
    videos: z
      .array(z.object({ title: z.string(), youtubeId: z.string() }))
      .optional(),
    specs: z
      .object({
        /** 'columns' = spec_block(cols=True); 'keyvalue' = Hydro-Slide's raw 2-col table. */
        variant: z.enum(["columns", "keyvalue"]),
        head: z.string().default("Specifications"),
        showHead: z.boolean().default(true),
        showHint: z.boolean().default(true),
        columns: z.array(z.string()).optional(),
        rows: z.array(z.array(z.string())).min(1),
      })
      .optional(),
    contactThoracent: z.boolean().default(true),
    /** Order within the parent category listing. */
    order: z.number().int().default(0),
  }),
});

/**
 * News — 8 records, NOT 7 (plan §2.3): the featured article never appears in
 * the grid; the grid has its own 7 cells. placement makes that explicit.
 */
const news = defineCollection({
  loader: glob({ pattern: "**/*.yaml", base: "./src/content/news" }),
  schema: z.object({
    source: z.string(),
    logo: z.string().regex(/^\//).optional(),
    date: z.string(),
    headline: z.string(),
    summary: z.string(),
    url: z.string().url(),
    placement: z.enum(["featured", "grid"]),
    /** Position in the news grid (grid items only). */
    gridOrder: z.number().int().optional(),
  }),
});

/**
 * Leaders — one Markdown file per bio (plan §2.2). draft:true keeps the
 * record while suppressing it from team.html (replaces DRAFT_LEADERS).
 */
const leaders = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/leaders" }),
  schema: z.object({
    key: z.string(),
    name: z.string(),
    title: z.string(),
    photo: z.string().regex(/^\//),
    linkedin: z.string().url().optional(),
    order: z.number().int(),
    draft: z.boolean().default(false),
  }),
});

/**
 * Prose pages (legal, etc. — plan §2.5). lastUpdated is OPTIONAL because
 * regulatory-information has no date today; rendering one there would be new
 * visible content on a regulatory page.
 */
const pages = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string(),
    metaDescription: z.string().max(170),
    lastUpdated: z.string().optional(),
  }),
});

export const collections = { products, news, leaders, pages };
