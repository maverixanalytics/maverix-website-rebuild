// ESLint flat config — Astro + React 19 + TypeScript.
// Run: npm run lint   (CI runs this alongside `tsc --noEmit`)
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import reactHooks from "eslint-plugin-react-hooks";
import astro from "eslint-plugin-astro";
import prettier from "eslint-config-prettier";

export default tseslint.config(
  { ignores: ["dist/**", ".astro/**", "node_modules/**", "public/**"] },

  js.configs.recommended,
  ...tseslint.configs.recommended,

  // React islands. `configs.flat['recommended-latest']` carries the
  // compiler-powered rules that enforce the Rules of React (incl.
  // exhaustive-deps). Note: plugin's top-level `configs.recommended*` are
  // legacy eslintrc-shaped; the flat-config variants live under `configs.flat`.
  // Do not disable exhaustive-deps casually — fix the code instead.
  {
    files: ["src/islands/**/*.{ts,tsx}"],
    ...reactHooks.configs.flat["recommended-latest"],
  },

  // Astro components.
  ...astro.configs["flat/recommended"],

  // Node-side build tooling (integration + verify harnesses) runs outside the
  // browser, so Node globals are expected there.
  {
    files: ["integrations/**/*.mjs", "scripts/**/*.mjs", "*.config.{js,mjs,ts}"],
    languageOptions: {
      globals: { process: "readonly", console: "readonly" },
    },
    rules: {
      "no-undef": "off", // handled by @types/node + tsc
    },
  },

  // Project rules.
  {
    rules: {
      // `any` is treated as a bug (repo currently has zero).
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-unused-vars": [
        "error",
        { argsIgnorePattern: "^_", varsIgnorePattern: "^_" },
      ],
    },
  },

  // Prettier last so formatting rules never fight the formatter.
  prettier,
);
