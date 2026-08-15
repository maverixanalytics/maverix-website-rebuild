/**
 * Product listing groups — extracted from the legacy build
 * (maverix-legacy/src/build.py, INTERVENTION_GROUPS / DIAGNOSIS_TOOLS,
 * lines ~538-559). Card labels are the LISTING-CARD form and carry the
 * real ®/™ characters (converted from the legacy &reg;/&trade; entities);
 * product-page H1 forms live in each product's MDX frontmatter (`name`).
 * Image keys are mapped through the legacy IMG dict to root-absolute paths.
 */

export interface ProductGroupItem {
  slug: string;
  name: string;
  image?: string;
  abbr?: string;
}

export interface ProductGroup {
  label: string;
  items: ProductGroupItem[];
}

/** Intervention (Thoracent) products, grouped for the static product boxes. */
export const interventionGroups: ProductGroup[] = [
  {
    label: "Airway",
    items: [
      {
        slug: "bonastent-tracheobronchial-stent",
        name: "Bonastent® Tracheobronchial Stent",
        image: "/images/bonastent-tb.jpg",
      },
      {
        slug: "y-shaped-tracheal-stent",
        name: "Y-Shaped Tracheal Stent",
        image: "/images/ystent.png",
      },
    ],
  },
  {
    label: "Esophageal",
    items: [
      {
        slug: "bonastent-esophogeal-stent",
        name: "Bonastent® Esophageal Stent",
        image: "/images/bonastent-esoph.jpg",
      },
      {
        slug: "hilzo-tts-esophageal-stent",
        name: "Hilzo™ TTS Esophageal Stent",
        image: "/images/hilzo-tts.jpg",
      },
      {
        slug: "hilzo-ues-esophageal-stent",
        name: "Hilzo™ UES Esophageal Stent",
        image: "/images/hilzo-ues.jpg",
      },
    ],
  },
  {
    label: "Accessories",
    items: [
      {
        slug: "hydro-slide-pulmonary-guidewire",
        name: "Hydro-Slide Pulmonary Guide Wire",
        image: "/images/guidewire.jpg",
      },
      {
        slug: "netis-retrieval-net",
        name: "Netis Retrieval Net",
        image: "/assets/netis-retrieval-net.jpg",
      },
    ],
  },
];

/** Diagnosis (biopsy / tissue-sampling) tools. */
export const diagnosisTools: ProductGroupItem[] = [
  {
    slug: "biopsy-forceps",
    name: "Biopsy Forceps",
    image: "/images/forceps.jpg",
  },
  {
    slug: "ebus-needles",
    name: "EBUS Needles",
    image: "/images/ebus.jpg",
  },
  {
    slug: "narwhal-cryo-system",
    name: "Narwhal Cryo System",
    image: "/images/narwhal-cryo.jpg",
  },
];
