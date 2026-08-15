/**
 * Homepage `sup.cite` footnote scheme — EXTERNAL-link stat citations on the
 * Challenge block, numbered 1–6 in reading order down the page (renumbered
 * 13 Aug 2026; the earlier statistics spec had the U.S./global sources
 * reversed). Rendered by Cite.astro as <sup class="cite"> markers that link
 * straight OUT to the source.
 *
 * INDEPENDENT of the Risk Assessment `sup.ref` scheme (in-page #ref-N list,
 * src/content/references/risk.ts) and of the Narwhal `*` scheme — three
 * schemes, three pages, three markups. NEVER merge or cross-number them.
 *
 * URLs verbatim from legacy src/build.py CITES:
 *  1  American Cancer Society, Key Statistics for Lung Cancer — headline
 *  2  IARC GLOBOCAN world fact sheet — the 19% share-of-deaths figure
 *  3  WHO Lung cancer fact sheet — the 2.5M annual-incidence figure only
 *  4  American Lung Association, State of Lung Cancer — the four U.S. grid
 *     stats (18.2%, 28.1%, 21%, 29.7%)
 *  5  Sabatino SA, Prev Chronic Dis 2025;22:250139 — the >63% figure
 *  6  CDC, Lung Cancer Among People Who Never Smoked — the 10–20% figure
 */
export const HOME_CITES: Record<number, string> = {
  1: "https://www.cancer.org/cancer/types/lung-cancer/about/key-statistics.html",
  2: "https://gco.iarc.who.int/media/globocan/factsheets/populations/900-world-fact-sheet.pdf",
  3: "https://www.who.int/news-room/fact-sheets/detail/lung-cancer",
  4: "https://www.lung.org/research/state-of-lung-cancer/key-findings",
  5: "https://www.cdc.gov/pcd/issues/2025/25_0139a.htm",
  6: "https://www.cdc.gov/lung-cancer/nonsmokers/index.html",
};
