import {type FormEvent, useRef, useState} from "react";

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
 *  - empty endpoint → POST to "/" as application/x-www-form-urlencoded
 *    (Netlify's own submission capture path — see commit 4436726
 *    "fix/netlify-forms"); ok → hide form + success; HTTP error → default
 *    error text; network error → fall back to mailto: URL (subject from the
 *    "Subject" field, else "Website enquiry from {First Name|Name|a visitor}";
 *    body from all fields except keys starting "_" and "form-name" and blank
 *    values), navigate to it, then after 600ms restore the button and show
 *    "Thanks — your email app should be opening…";
 *
 *    NOTE: this fetch must NOT set `redirect: "error"`. A successful Netlify
 *    form submission answers with a 302 to the success page, which that mode
 *    turns into a rejected promise — sending every successful send down the
 *    mailto path and making the form look broken.
 *
 *    Netlify wiring (docs.netlify.com/manage/forms/setup, "JavaScript-rendered
 *    forms"): detection happens at deploy time against the built HTML, so the
 *    form must be server-rendered — `client:visible` only hydrates markup Astro
 *    already emitted, so the bot sees it. Required pieces, all below: the
 *    `data-netlify="true"` flag, the `<input type="hidden" name="form-name">`
 *    carrying the same value as the form's `name`, and a submission body that
 *    is URL-encoded (Netlify does not accept JSON).
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
        const sendMailto = () => {
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
        };
        if (!endpoint) {
            fetch("/", {
                method: "POST",
                headers: {"Content-Type": "application/x-www-form-urlencoded"},
                body: new URLSearchParams(
                    Array.from(data.entries()).map(([k, v]) => [k, String(v)]),
                ).toString(),
            })
                .then((r) => {
                    if (r.ok) {
                        setFormHidden(true);
                        setShown("ok");
                    } else {
                        // Server rejected the submission (e.g. the form name is
                        // not registered). Surface the error rather than opening
                        // the user's mail app — the site is reachable.
                        setSending(false);
                        setShown("err");
                    }
                })
                // Network-level failure only: the POST never reached Netlify,
                // so mailto is the sole remaining way to get the message out.
                .catch(() => {
                    sendMailto();
                });
            return;
        }
        fetch(endpoint, {
            method: "POST",
            body: data,
            headers: {Accept: "application/json"},
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
                netlify-honeypot="_gotcha"
                action={endpoint || undefined}
                data-endpoint={endpoint}
                data-mailto={mailto}
                style={formHidden ? {display: "none"} : undefined}
                onSubmit={handleSubmit}
            >
                <input type="hidden" name="form-name" defaultValue={name}/>
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
                style={shown === "ok" ? {display: "block"} : undefined}
            >
                {okText}
            </div>
            <div
                className={msgCls("form-msg form-error")}
                style={shown === "err" ? {display: "block"} : undefined}
            >
                {errText}
            </div>
        </div>
    );
}
