import { useRef, useState, type FormEvent } from "react";

/**
 * Contact / careers form island — replaces the legacy inline
 * `form[data-mvxform]` handler (build.py JS lines 153-181) 1:1.
 *
 * Boundary rule (CONVENTIONS §Islands): the island owns the form AND its
 * `.form-msg` sibling divs, so the legacy `f.parentElement.querySelector`
 * reach becomes plain component state — no DOM lookups outside the island.
 *
 * Behavior parity with the legacy script, message strings verbatim:
 *  - honeypot `_gotcha` filled → hide the form, show the (fake) success msg;
 *  - empty endpoint → build a mailto: URL (subject from the "Subject" field,
 *    else "Website enquiry from {First Name|Name|a visitor}"; body from all
 *    fields except keys starting "_" and "form-name" and blank values),
 *    navigate to it, then after 600ms restore the button and show
 *    "Thanks — your email app should be opening…";
 *  - non-empty endpoint → fetch POST FormData with Accept: application/json;
 *    ok → hide form + success; HTTP error → default error text; network
 *    error → "Network error — please try again, or email {data-mailto}.";
 *  - while sending: submit button disabled + label "Sending…", restored on
 *    error (legacy captured/restored `btn.textContent`).
 *
 * Like legacy, a message shown WITHOUT an override keeps whatever text the
 * div currently has (the verbatim defaults below, unless a previous send
 * already swapped in a custom string).
 *
 * A11y upgrade over legacy (intended exception, attribute-level only): the
 * careers fields keep their visible <label>s AND placeholders and now also
 * carry aria-labels; the contact fields already had aria-labels in legacy.
 *
 * NOTE for the orchestrator: the form is now client-rendered markup inside
 * an island. Netlify's build-time form detection only sees the SSR'd HTML in
 * dist/ (present, since islands server-render) — irrelevant today because
 * FORM_ENDPOINT is "" (mailto fallback, a Privacy Policy commitment).
 */

export type MvxField = {
  /** FormData key, e.g. "First Name" — feeds the mailto body verbatim. */
  name: string;
  type: "text" | "email" | "tel" | "textarea";
  required?: boolean;
  placeholder: string;
  /** A11y name; legacy contact had these, careers gains them (see header). */
  ariaLabel: string;
  autocomplete?: string;
  /** Visible label text (careers layout only). */
  label?: string;
  /** id pairing the visible label with its control (careers layout only). */
  id?: string;
  /** textarea rows (careers Message uses 5; contact omits it like legacy). */
  rows?: number;
  /** Column placement for the contact .colL/.colR layout. */
  col?: "L" | "R";
};

type MvxFormProps = {
  /** careers = .form labelled layout; contact = .cform .colL/.colR layout. */
  variant: "careers" | "contact";
  /** Legacy form name attribute + hidden form-name value. */
  name: string;
  /** FORM_ENDPOINT — empty string means the mailto fallback path. */
  endpoint: string;
  /** CONTACT_EMAIL — mailto target + the "or email …" error string. */
  mailto: string;
  fields: MvxField[];
  /** "Send message" (careers) / "Send Message" (contact). */
  submitLabel: string;
  /** Class for the submit button: "form-send-inline" / "send". */
  submitClass?: string;
  /** Class for the island's wrapper div (careers "form-wrap-inline"). */
  wrapClass?: string;
  /** Extra class for both .form-msg divs (contact "form-msg-gap-inline"). */
  msgClass?: string;
};

/** Verbatim defaults from the legacy .form-msg divs. */
const OK_DEFAULT = "Thank you! Your submission has been received!";
const ERR_DEFAULT = "Oops! Something went wrong while submitting the form.";

export function MvxForm({
  variant,
  name,
  endpoint,
  mailto,
  fields,
  submitLabel,
  submitClass,
  wrapClass,
  msgClass,
}: MvxFormProps) {
  const gotchaRef = useRef<HTMLInputElement>(null);
  const [sending, setSending] = useState(false);
  const [formHidden, setFormHidden] = useState(false);
  const [shown, setShown] = useState<"none" | "ok" | "err">("none");
  const [okText, setOkText] = useState(OK_DEFAULT);
  const [errText, setErrText] = useState(ERR_DEFAULT);

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    if (!form.reportValidity()) return;
    // Honeypot: pretend success, hide the form, never send anything.
    if (gotchaRef.current?.value) {
      setFormHidden(true);
      setShown("ok");
      return;
    }
    const data = new FormData(form);
    setSending(true);
    if (!endpoint) {
      const lines: string[] = [];
      data.forEach((v, k) => {
        if (k.charAt(0) !== "_" && k !== "form-name" && String(v).trim()) {
          lines.push(k + ": " + String(v));
        }
      });
      const subject =
        data.get("Subject") ||
        "Website enquiry from " +
          String(data.get("First Name") || data.get("Name") || "a visitor");
      window.location.href =
        "mailto:" +
        mailto +
        "?subject=" +
        encodeURIComponent(String(subject)) +
        "&body=" +
        encodeURIComponent(lines.join("\n"));
      window.setTimeout(() => {
        setSending(false);
        setOkText(
          "Thanks — your email app should be opening with this message ready to send.",
        );
        setShown("ok");
      }, 600);
      return;
    }
    fetch(endpoint, {
      method: "POST",
      body: data,
      headers: { Accept: "application/json" },
    })
      .then((r) => {
        if (r.ok) {
          setFormHidden(true);
          setShown("ok");
        } else {
          setSending(false);
          setShown("err");
        }
      })
      .catch(() => {
        setSending(false);
        setErrText(
          "Network error — please try again, or email " + (mailto || "us") + ".",
        );
        setShown("err");
      });
  };

  const control = (f: MvxField) =>
    f.type === "textarea" ? (
      <textarea
        key={f.name}
        id={f.id}
        name={f.name}
        rows={f.rows}
        required={f.required}
        placeholder={f.placeholder}
        aria-label={f.ariaLabel}
        autoComplete={f.autocomplete}
      />
    ) : (
      <input
        key={f.name}
        id={f.id}
        name={f.name}
        type={f.type}
        required={f.required}
        placeholder={f.placeholder}
        aria-label={f.ariaLabel}
        autoComplete={f.autocomplete}
      />
    );

  const msgCls = (base: string) => (msgClass ? `${base} ${msgClass}` : base);

  return (
    <div className={wrapClass}>
      <form
        className={variant === "careers" ? "form" : "cform"}
        data-mvxform=""
        name={name}
        method="POST"
        data-netlify="true"
        /* rendered legacy contact-us.html carries a bare netlify-form
           attribute that build.py does not emit — reproduced from the
           rendered truth on the contact variant only */
        netlify-form={variant === "contact" ? "" : undefined}
        netlify-honeypot="_gotcha"
        action={endpoint}
        data-endpoint={endpoint}
        data-mailto={mailto}
        style={formHidden ? { display: "none" } : undefined}
        onSubmit={handleSubmit}
      >
        <input type="hidden" name="form-name" defaultValue={name} />
        <p className="honeypot">
          <label>
            Do not fill this in{" "}
            <input
              ref={gotchaRef}
              type="text"
              name="_gotcha"
              tabIndex={-1}
              autoComplete="off"
            />
          </label>
        </p>
        {variant === "careers" ? (
          fields.map((f) => (
            <div key={f.name}>
              <label htmlFor={f.id}>{f.label}</label>
              {control(f)}
            </div>
          ))
        ) : (
          <>
            <div className="colL">
              {fields.filter((f) => f.col !== "R").map(control)}
            </div>
            <div className="colR">
              {fields.filter((f) => f.col === "R").map(control)}
            </div>
          </>
        )}
        <button type="submit" className={submitClass} disabled={sending}>
          {sending ? "Sending…" : submitLabel}
        </button>
      </form>
      <div
        className={msgCls("form-msg form-success")}
        style={shown === "ok" ? { display: "block" } : undefined}
      >
        {okText}
      </div>
      <div
        className={msgCls("form-msg form-error")}
        style={shown === "err" ? { display: "block" } : undefined}
      >
        {errText}
      </div>
    </div>
  );
}
