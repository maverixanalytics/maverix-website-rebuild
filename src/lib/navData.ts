/**
 * Site navigation copy — extracted verbatim from legacy build.py header()
 * (lines ~226-280). Category descriptions are marketing copy: treat edits
 * as MLR-reviewable content changes.
 */

export type NavCard = {
  category: "risk" | "diagnosis" | "intervention";
  title: string;
  copy: string;
  href: string;
  cta: string;
};

export type NavSection = {
  label: string;
  href: string;
  kind: "products" | "team" | "news";
  cards?: NavCard[];
};

export const PRODUCTS_CARDS: NavCard[] = [
  {
    category: "risk",
    title: "Risk Assessment",
    copy: "Developing molecular diagnostic tools that aim to triage lung cancer in patients to identify those in need of immediate care.",
    href: "/diagnostics.html",
    cta: "Explore Maverix Diagnostics",
  },
  {
    category: "diagnosis",
    title: "Diagnosis",
    copy: "Endobronchial tissue-sampling instruments designed to help physicians obtain the tissue needed for an accurate diagnosis.",
    href: "/serpex.html",
    cta: "Explore Biopsy Tools",
  },
  {
    category: "intervention",
    title: "Intervention",
    copy: "Minimally invasive devices for managing pleural effusions, restoring airway patency, and improving quality of life, along with an expanded suite of GI tools.",
    href: "/thoracent.html",
    cta: "Explore the interventional portfolio",
  },
];

export const TEAM_CARDS: NavCard[] = [
  {
    category: "risk",
    title: "Leadership",
    copy: "Maverix leadership combines decades of clinical, technical, and operating experience.",
    href: "/team.html#leadership",
    cta: "Learn more about our leadership",
  },
  {
    category: "diagnosis",
    title: "Advisors",
    copy: "The Maverix Medical Advisory Board is comprised of leading pulmonary physicians.",
    href: "/team.html#advisors",
    cta: "Meet our advisors",
  },
];
