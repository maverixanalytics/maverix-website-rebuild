import { useEffect, useRef, useState } from "react";
import type { NavCard } from "@/lib/navData";

/**
 * Site navigation island (plan §4).
 *
 * SSRs the complete nav markup on every page; hydrates ONLY at ≤920px
 * (client:media in SiteHeader). Desktop mega-menu open/close is pure CSS
 * hover — this component adds zero desktop JS, matching legacy.
 *
 * Owns BOTH the hamburger trigger and the .nav-links panel (island boundary
 * rule: trigger + target in one component — the legacy sibling lookup is
 * retired). State classes .open / .sub-open are the legacy contract and are
 * styled by the ported chrome CSS.
 *
 * Mobile behavior parity with legacy inline JS, plus two logged a11y
 * upgrades: Escape closes the menu, and focus returns to the hamburger.
 * Legacy quirk preserved: the news top-link NAVIGATES on mobile (the legacy
 * accordion binding skips .newsmega).
 */

export type NewsTeaser = {
  source: string;
  date: string;
  headline: string;
  url: string;
};

type SiteNavProps = {
  productsCards: NavCard[];
  teamCards: NavCard[];
  featured: NewsTeaser;
  sideCell: NewsTeaser;
};

const MOBILE_QUERY = "(max-width: 920px)";

function ArrowIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="#1A4A5D"
      strokeWidth={3}
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M6 5l7 7-7 7" />
      <path d="M12.5 5l7 7-7 7" />
    </svg>
  );
}

function CardCol({ card }: { card: NavCard }) {
  return (
    <div className={`mcol cat-${card.category}`}>
      <h4>{card.title}</h4>
      <p>{card.copy}</p>
      <a className="btn" href={card.href}>
        <span className="circ">
          <ArrowIcon />
        </span>
        <span className="btn-label">{card.cta}</span>
      </a>
    </div>
  );
}

export function SiteNav({
  productsCards,
  teamCards,
  featured,
  sideCell,
}: SiteNavProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [openSub, setOpenSub] = useState<number | null>(null);
  const hamburgerRef = useRef<HTMLButtonElement>(null);

  // Sync with the media query: leaving mobile resets all mobile-only state.
  useEffect(() => {
    const mq = window.matchMedia(MOBILE_QUERY);
    const onChange = () => {
      if (!mq.matches) {
        setIsOpen(false);
        setOpenSub(null);
      }
    };
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, []);

  // Escape closes the open mobile menu and returns focus (a11y upgrade,
  // logged in PARITY-EXCEPTIONS.md).
  useEffect(() => {
    if (!isOpen) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setIsOpen(false);
        setOpenSub(null);
        hamburgerRef.current?.focus();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [isOpen]);

  const handleToggleMenu = () => {
    setIsOpen((open) => {
      if (open) setOpenSub(null);
      return !open;
    });
  };

  const handleTopLink = (index: number) => (e: React.MouseEvent) => {
    // Only intercept on mobile; desktop keeps plain navigation + CSS hover.
    if (!window.matchMedia(MOBILE_QUERY).matches) return;
    e.preventDefault();
    setOpenSub((current) => (current === index ? null : index));
  };

  const subClass = (index: number) => (openSub === index ? " sub-open" : "");

  return (
    <>
      <button
        ref={hamburgerRef}
        className="hamburger"
        aria-label="Menu"
        aria-expanded={isOpen}
        onClick={handleToggleMenu}
        type="button"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
      <nav className={`nav-links${isOpen ? " open" : ""}`}>
        <div className={subClass(0)}>
          <a
            className="nav-top-link"
            href="/products.html"
            onClick={handleTopLink(0)}
          >
            products <span className="plus">+</span>
            <span className="arrow">→</span>
          </a>
          <div className="dropdown mega">
            <div className="dropdown-in">
              {productsCards.map((card) => (
                <CardCol key={card.category} card={card} />
              ))}
            </div>
          </div>
        </div>
        <div className={subClass(1)}>
          <a
            className="nav-top-link"
            href="/team.html"
            onClick={handleTopLink(1)}
          >
            team <span className="plus">+</span>
            <span className="arrow">→</span>
          </a>
          <div className="dropdown mega">
            <div className="dropdown-in cols2">
              {teamCards.map((card) => (
                <CardCol key={card.category} card={card} />
              ))}
            </div>
          </div>
        </div>
        <div>
          {/* Legacy parity: no accordion handler — news navigates on mobile */}
          <a className="nav-top-link" href="/news.html">
            news <span className="plus">+</span>
            <span className="arrow">→</span>
          </a>
          <div className="dropdown mega newsmega">
            <div className="dropdown-in newsdd">
              <div className="ncol feat">
                <div className="most-recent-article">Most Recent Article</div>
                <div className="news-source">{featured.source}</div>
                <div className="date">{featured.date}</div>
                <h4>
                  <a href={featured.url} target="_blank" rel="noopener">
                    {featured.headline}
                  </a>
                </h4>
                <a
                  className="read-more"
                  href={featured.url}
                  target="_blank"
                  rel="noopener"
                >
                  Read More
                </a>
              </div>
              <div className="ncol side">
                <div className="cell">
                  <div className="news-source">{sideCell.source}</div>
                  <div className="date">{sideCell.date}</div>
                  <h5>
                    <a href={sideCell.url} target="_blank" rel="noopener">
                      {sideCell.headline}
                    </a>
                  </h5>
                  <a
                    className="read-more"
                    href={sideCell.url}
                    target="_blank"
                    rel="noopener"
                  >
                    Read More
                  </a>
                </div>
                <div className="cell view-all">
                  <a href="/news.html">
                    <span className="circ">
                      <ArrowIcon />
                    </span>
                    Read all news
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="mobile-extra">
          <a href="/contact-us.html">Contact</a>
          <a href="/careers.html">Careers</a>
        </div>
      </nav>
    </>
  );
}
