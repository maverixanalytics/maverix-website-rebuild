/**
 * Scroll-reveal — port of the legacy inline behavior (plan §4: presentational,
 * stays vanilla in the layout; bundled ONCE instead of inlined per page).
 *
 * Selector list trimmed to classes that exist in the new build (the legacy
 * list carried five orphans). Gated on prefers-reduced-motion and
 * IntersectionObserver support exactly like legacy, including the 3s
 * failsafe that reveals everything if observation never fires.
 */
const REVEAL_SELECTORS = [
  ".pathcard",
  ".photo-card",
  ".pcard",
  ".member",
  ".advcard",
  ".newsgrid .ncell",
  ".featured",
  ".statgrid .cell",
  ".why-cell",
  ".sechead",
  ".biglead",
  ".journey",
  ".challenge .headline",
  ".spec",
].join(",");

export function initReveal(): void {
  if (
    window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
    !("IntersectionObserver" in window)
  ) {
    return;
  }
  const elements = Array.from(
    document.querySelectorAll<HTMLElement>(REVEAL_SELECTORS),
  );
  if (elements.length === 0) return;

  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in-view");
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" },
  );

  elements.forEach((el, index) => {
    el.classList.add("reveal-on-scroll");
    const siblingIndex = el.parentElement
      ? Array.from(el.parentElement.children).indexOf(el)
      : index;
    el.style.transitionDelay = `${(siblingIndex % 6) * 70}ms`;
    observer.observe(el);
  });

  // Failsafe: never leave content hidden.
  window.setTimeout(() => {
    for (const el of elements) el.classList.add("is-in-view");
  }, 3000);
}

initReveal();
