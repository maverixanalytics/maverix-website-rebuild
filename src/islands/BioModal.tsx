import { useEffect, useRef, useState } from "react";

/**
 * Team-page bio modal island (plan §2.2/§4). One island per leader owns BOTH
 * the .member trigger card and its .modal — no getElementById reaches; class
 * names keep the legacy contract (.member/.modal/.open/…) so ported team.css
 * applies unchanged. Hydrate with client:idle: the modal is display:none, so
 * client:visible would never intersect (plan §4 hydration rule).
 *
 * Parity with the legacy team.html script:
 *  - open: add .open, lock body scroll (body.style.overflow='hidden'),
 *    move focus to the .close button;
 *  - Tab/Shift+Tab wrap within the open modal's focusables;
 *  - Escape / overlay click / .close click: remove .open, unlock scroll,
 *    return focus to the trigger card.
 *  - A11Y FIX (logged): legacy Escape closed the modal but never restored
 *    focus to the trigger (only overlay/close clicks did). Here all three
 *    close paths restore focus.
 *
 * First bio paragraph renders bold via ported CSS
 * (.modal .bio-text p:first-child) — DOM stays one <p> per paragraph.
 */
type BioModalProps = {
  name: string;
  title: string;
  /** Root-absolute headshot path, e.g. "/assets/carla-resized.png". */
  photo: string;
  linkedin?: string;
  bioParagraphs: string[];
};

export function BioModal({
  name,
  title,
  photo,
  linkedin,
  bioParagraphs,
}: BioModalProps) {
  const [isOpen, setIsOpen] = useState(false);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const closeRef = useRef<HTMLButtonElement>(null);
  const boxRef = useRef<HTMLDivElement>(null);

  const open = () => setIsOpen(true);
  const close = () => setIsOpen(false);

  useEffect(() => {
    if (!isOpen) return;
    // Legacy contract: scroll lock via body.style.overflow, focus to ×.
    document.body.style.overflow = "hidden";
    closeRef.current?.focus();

    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setIsOpen(false);
        return;
      }
      if (e.key !== "Tab" || !boxRef.current) return;
      const focusables = boxRef.current.querySelectorAll<HTMLElement>(
        'button,a[href],input,textarea,[tabindex]:not([tabindex="-1"])',
      );
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", onKeyDown);

    return () => {
      document.removeEventListener("keydown", onKeyDown);
      document.body.style.overflow = "";
      // Every close path (Escape included — logged a11y fix) returns focus.
      triggerRef.current?.focus();
    };
  }, [isOpen]);

  return (
    <>
      <button className="member" ref={triggerRef} onClick={open}>
        <img src={photo} alt={name} loading="lazy" />
        <div className="member-info">
          <div className="member-name">{name}</div>
          <div className="member-role">{title}</div>
        </div>
      </button>
      <div className={`modal${isOpen ? " open" : ""}`}>
        <div className="overlay" onClick={close}></div>
        <div className="modal-box" ref={boxRef}>
          <button
            className="close"
            aria-label="Close"
            ref={closeRef}
            onClick={close}
          >
            &times;
          </button>
          <div className="mphoto">
            <img src={photo} alt={name} />
          </div>
          <div className="mbody">
            <h2>{name}</h2>
            <div className="member-role">{title}</div>
            <div className="bio-text">
              {bioParagraphs.map((paragraph) => (
                <p key={paragraph}>{paragraph}</p>
              ))}
            </div>
            {linkedin && (
              <a
                className="profile-link"
                href={linkedin}
                target="_blank"
                rel="noopener"
              >
                <span className="li-badge">
                  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z" />
                  </svg>
                </span>
                LinkedIn
              </a>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
