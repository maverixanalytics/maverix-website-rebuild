/**
 * Homepage patient-journey diagram data (.jpanel), extracted from legacy
 * index.html (build_home). Two .journey blocks:
 *  - "Traditional": jtitle + jnote ABOVE the bar; the bar carries invisible
 *    .tail spacers either side, a .fade.truncated Life Expectancy block and
 *    the red .end-marker (see theme.css v45/v46 comments).
 *  - "Maverix": bar FIRST, then the .jarrow annotation, then the jtitle.
 *
 * Layout data (the flex proportions) lives HERE, not in inline styles in the
 * page — but the rendered markup must still emit each value as a
 * style="flex:…" attribute to match legacy byte behavior, so index.astro maps
 * seg.flex → style attribute. Values are kept as verbatim strings (".72",
 * "1.3") so the emitted attribute matches legacy exactly.
 */

export type JourneySeg = {
  /** Full class attribute of the <span>, verbatim (e.g. "jseg fade truncated"). */
  classes: string;
  /** Visible label; empty string for spacer (.tail) and .end-marker segments. */
  label: string;
  /** Legacy inline flex value, emitted as style="flex:…"; null = no style attribute. */
  flex: string | null;
};

export type JourneyBlock = {
  /** .jtitle text. */
  title: string;
  /** true = jtitle renders AFTER the bar (Maverix block); false = before (traditional). */
  titleAfterBar: boolean;
  /** .jnote text (traditional block only — renders between jtitle and jbar). */
  note?: string;
  /** .jarrow text (Maverix block only — renders between jbar and jtitle). */
  arrow?: string;
  segments: JourneySeg[];
};

export const JOURNEY_BARS: JourneyBlock[] = [
  {
    title: "Traditional lung cancer patient journey",
    titleAfterBar: false,
    note: "Starts later, has longer therapy cycles and shorter life expectancy",
    segments: [
      { classes: "jseg tail", label: "", flex: ".72" },
      { classes: "jseg dark", label: "Risk Assessment", flex: "1.3" },
      { classes: "jseg steel", label: "Diagnosis", flex: ".9" },
      { classes: "jseg light", label: "Intervention", flex: "2.2" },
      { classes: "jseg fade truncated", label: "Life Expectancy", flex: "1.24" },
      { classes: "jseg end-marker", label: "", flex: null },
      { classes: "jseg tail", label: "", flex: ".72" },
    ],
  },
  {
    title: "Maverix lung cancer patient journey",
    titleAfterBar: true,
    arrow: "Earlier diagnosis, shorter time to treatment, improved outcomes.",
    segments: [
      { classes: "jseg dark", label: "Risk Assessment", flex: "1.3" },
      { classes: "jseg steel", label: "Diagnosis", flex: ".8" },
      { classes: "jseg light", label: "Intervention", flex: "1.5" },
      { classes: "jseg fade", label: "Life Expectancy", flex: "4.2" },
    ],
  },
];
