import { useState, type ReactNode } from "react";

/**
 * Mobile tap-expand card island (plan §4). Wraps ONE card (pathcard or
 * photo-card); hydrated with client:media="(max-width:920px)" — desktop
 * hover reveal stays pure CSS, zero desktop JS.
 *
 * Parity with legacy: click OR Enter/Space toggles .open; clicks that land
 * on a link inside the card navigate instead of toggling.
 */
type ExpandCardProps = {
  /** Full class string for the card element, e.g. "pathcard" / "photo-card has-reveal". */
  cardClass: string;
  children: ReactNode;
};

const MOBILE_QUERY = "(max-width: 920px)";

export function ExpandCard({ cardClass, children }: ExpandCardProps) {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    if (!window.matchMedia(MOBILE_QUERY).matches) return;
    setIsOpen((open) => !open);
  };

  const handleClick = (e: React.MouseEvent) => {
    if ((e.target as HTMLElement).closest("a")) return;
    toggle();
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key !== "Enter" && e.key !== " ") return;
    if ((e.target as HTMLElement).closest("a")) return;
    e.preventDefault();
    toggle();
  };

  return (
    <div
      className={`${cardClass}${isOpen ? " open" : ""}`}
      tabIndex={0}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
    >
      {children}
    </div>
  );
}
