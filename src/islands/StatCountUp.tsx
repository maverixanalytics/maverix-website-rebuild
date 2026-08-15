import { useEffect, useRef } from "react";

/**
 * Homepage stat count-up island — replaces the legacy inline counter
 * (build.py page script: nio IntersectionObserver over
 * `.statgrid .stat-number,.bigstat .stat-number`).
 *
 * Boundary rule: the island owns its trigger AND its target — the span IS
 * both (the observer watches it, the animation writes to it). SSR output is
 * the full final text, so no-JS / pre-hydration rendering is already exact.
 *
 * Legacy contract, preserved verbatim:
 *  - parse with /^([^0-9]*)([0-9]+(?:\.[0-9]+)?)(.*)$/ — prefix (m[1]),
 *    number (m[2]), suffix (m[3]); decimals = m[2]'s fraction length;
 *  - first intersection at threshold .6, then unobserve;
 *  - 1200ms, cubic ease-out p = 1 - Math.pow(1 - p, 3);
 *  - each frame writes pre + (end * p).toFixed(dec) + suf;
 *  - gated: prefers-reduced-motion or no IntersectionObserver → static text.
 *
 * Fragile cases (unit notes — the final frame must equal the input EXACTLY):
 *  - ">63%"   → pre ">", number "63" (dec 0), suffix "%" — the ">" prefix
 *    must survive every frame, not just the last.
 *  - "10–20%" → pre "", number "10" (dec 0), suffix "–20%" — only the 10
 *    animates; the en-dash range reads as suffix.
 *  - "2.5M"   → pre "", number "2.5" (dec 1), suffix "M" — toFixed(1) keeps
 *    one decimal the whole run so the text never jitters in width.
 * The last frame writes the raw input `text` (mathematically identical to
 * pre + end.toFixed(dec) + suf, but exact by construction).
 */

const STAT_RE = /^([^0-9]*)([0-9]+(?:\.[0-9]+)?)(.*)$/;
const DURATION_MS = 1200;

type StatCountUpProps = {
  /** Final stat text, e.g. "19%", "2.5M", ">63%", "10–20%". */
  text: string;
  /** Class for the rendered span; legacy markup uses "stat-number". */
  className?: string;
};

export function StatCountUp({
  text,
  className = "stat-number",
}: StatCountUpProps) {
  const spanRef = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    const el = spanRef.current;
    if (!el) return;
    // Same gate as legacy: reduced motion or no IO → leave the static text.
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if (!("IntersectionObserver" in window)) return;

    const match = text.match(STAT_RE);
    if (!match) return;
    const pre = match[1];
    const end = parseFloat(match[2]);
    const suf = match[3];
    const dec = (match[2].split(".")[1] || "").length;

    let rafId = 0;
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          observer.unobserve(entry.target);
          let t0: number | null = null;
          const step = (ts: number) => {
            if (t0 === null) t0 = ts;
            let p = Math.min((ts - t0) / DURATION_MS, 1);
            p = 1 - Math.pow(1 - p, 3);
            el.textContent =
              p < 1 ? pre + (end * p).toFixed(dec) + suf : text;
            if (p < 1) rafId = requestAnimationFrame(step);
          };
          rafId = requestAnimationFrame(step);
        });
      },
      { threshold: 0.6 },
    );
    observer.observe(el);

    return () => {
      observer.disconnect();
      cancelAnimationFrame(rafId);
      el.textContent = text;
    };
  }, [text]);

  return (
    <span className={className} ref={spanRef}>
      {text}
    </span>
  );
}
