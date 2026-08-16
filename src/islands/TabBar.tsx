import { useState, type ReactNode } from "react";

/**
 * Product-page tab bar island (plan §4).
 *
 * Owns the buttons AND the panes AND the section wrapper between them, so it
 * never reaches into DOM it doesn't own (island boundary rule) while emitting
 * exactly the legacy structure: .tabbar sits above the band section, panes
 * live inside .pd-panel, the static right rail passes through the `side`
 * slot. Hydrated (client:visible) ONLY on pages with a videos tab; other
 * pages render it with no client directive — pure static HTML, zero JS.
 *
 * State classes .is-active are the legacy CSS contract.
 *
 * A11y note: this deliberately does NOT use role=tablist/tab/tabpanel. The
 * legacy tab bar also holds external resource links (Size Chart, IFU) as
 * siblings of the buttons, and ARIA forbids non-tab children inside a
 * tablist — axe flags it as a CRITICAL aria-required-children violation.
 * Real <button>s with aria-expanded + aria-controls are valid, keyboard
 * accessible, and announce correctly. Arrow-key navigation is kept as a
 * convenience.
 */

export type TabDef = { id: "pane-features" | "pane-videos"; label: string };
export type ExternalLink = { label: string; url: string };

/**
 * Note on the optional slot props: `paneFeatures`, `paneVideos` and `side` are
 * always supplied in practice — but via Astro *named slots*
 * (`<Fragment slot="side">`), which Astro maps onto React props at runtime.
 * TypeScript cannot see that mapping, so declaring them required makes
 * `astro check` reject every real call site. Optional is the honest type here.
 */
type TabBarProps = {
  tabs: TabDef[];
  links: ExternalLink[];
  paneFeatures?: ReactNode;
  paneVideos?: ReactNode;
  side?: ReactNode;
};

export function TabBar({
  tabs,
  links,
  paneFeatures,
  paneVideos,
  side,
}: TabBarProps) {
  const [activeId, setActiveId] = useState<TabDef["id"]>(
    tabs[0]?.id ?? "pane-features",
  );

  const handleKeyDown = (e: React.KeyboardEvent, index: number) => {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    e.preventDefault();
    const delta = e.key === "ArrowRight" ? 1 : -1;
    const next = tabs[(index + delta + tabs.length) % tabs.length];
    if (next) setActiveId(next.id);
  };

  const paneFor = (id: TabDef["id"]): ReactNode =>
    id === "pane-features" ? paneFeatures : paneVideos;

  return (
    <>
      <div className="tabbar">
        <div className="container tabbar-in">
          {tabs.map((tab, index) => (
            <button
              key={tab.id}
              type="button"
              aria-expanded={activeId === tab.id}
              aria-controls={tab.id}
              className={activeId === tab.id ? "is-active" : undefined}
              onClick={() => setActiveId(tab.id)}
              onKeyDown={(e) => handleKeyDown(e, index)}
            >
              {tab.label}
            </button>
          ))}
          {links.map((link) => (
            <a key={link.url} href={link.url} target="_blank" rel="noopener">
              {link.label} <span className="ext-icon">↗</span>
            </a>
          ))}
        </div>
      </div>
      <section className="band light">
        <div className="container" style={{ padding: 0 }}>
          <div className="pd-wrap">
            <div className="pd-panel">
              {tabs.map((tab) => (
                <div
                  key={tab.id}
                  id={tab.id}
                  className={`tabpane${activeId === tab.id ? " is-active" : ""}`}
                >
                  {paneFor(tab.id)}
                </div>
              ))}
            </div>
            <div className="pd-side">{side}</div>
          </div>
        </div>
      </section>
    </>
  );
}
