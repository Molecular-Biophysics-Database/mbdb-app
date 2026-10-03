import React from "react";
import PropTypes from "prop-types";
import { Label } from "mbdb-semantic-ui-react";
import { useVocabularyTitle } from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import {
  isEmptyValue,
  useFieldErrors,
} from "@js/mbdb/forms/building-blocks/errors";
import { formatters } from "./formatters";

// Plain-text formatting of one value, used by cells and nested rows.

export const isValueUnit = (v) =>
  v !== null &&
  typeof v === "object" &&
  !Array.isArray(v) &&
  "value" in v &&
  "unit" in v;

// NOTE (later steps): treats any object with a string `id` as a vocabulary.
// `Entity_and_stoichiometry.entity` ({id, name}, an internal relation) would
// show the UUID; add a rule before measurement blocks use DetailView.
export const isVocabulary = (v) =>
  v !== null &&
  typeof v === "object" &&
  !Array.isArray(v) &&
  typeof v.id === "string";

export const isPlainObject = (v) =>
  v !== null && typeof v === "object" && !Array.isArray(v);

export const isLeafObject = (v) => isValueUnit(v) || isVocabulary(v);

// "18.02 g/mol", or the part of it that exists — the one value-unit text,
// shared with the chemical picker (chemical.js) so the detail view and the
// form read the same. "" when there is no value at all.
export const valueUnitText = (v) =>
  v?.value !== undefined && v?.value !== null
    ? [v.value, v.unit].filter((x) => !isEmptyValue(x)).join(" ")
    : "";

// `{ assessed: "Yes"|"No", …facts }` — the discriminated-optional shape (§3)
export const isAssessed = (v) =>
  isPlainObject(v) && (v.assessed === "Yes" || v.assessed === "No");

// an array of `{ name, description }` items (the Step type, §3)
export const isSteps = (value) =>
  Array.isArray(value) &&
  value.length > 0 &&
  value.every(
    (item) =>
      isPlainObject(item) &&
      !isLeafObject(item) &&
      Object.keys(item).every((k) => k === "name" || k === "description") &&
      !isEmptyValue(item.name)
  );

// §3: No, or Yes — <facts>. A fact that is a nested object (identity's
// by_intact_mass: { method, deviation }) gets one level of expansion here —
// textOf would drop the whole object. Nested facts join with "; " so the
// inner ", " stays readable; flat facts keep the old ", ".
const factText = (key, value, vocabulary) => {
  if (isPlainObject(value) && !isLeafObject(value)) {
    const inner = Object.values(value)
      .map((v) => textOf(v, vocabulary))
      .filter((t) => t !== "");
    return inner.length
      ? `${key.replaceAll("_", " ")}: ${inner.join(", ")}`
      : "";
  }
  return textOf(value, vocabulary);
};

const assessedText = (value, vocabulary) => {
  if (value.assessed === "No") return "No";
  const keys = Object.keys(value).filter((key) => key !== "assessed");
  const facts = keys
    .map((key) => factText(key, value[key], vocabulary))
    .filter((t) => t !== "");
  const hasNested = keys.some(
    (key) => isPlainObject(value[key]) && !isLeafObject(value[key])
  );
  return facts.length ? `Yes — ${facts.join(hasNested ? "; " : ", ")}` : "Yes";
};

// A `{ id }` vocabulary reference resolved to a title through the shared
// per-id cache (`useVocabularyTitle` does a GET once per id). Shows the id
// while loading. Declared by a `{ field, vocabulary }` group entry.
export const VocabularyValue = ({ vocabulary, value }) => {
  // the hook returns the title itself (a string) or undefined while loading;
  // a span wrapper keeps table-cell text selectable (fragment lint)
  const title = useVocabularyTitle(vocabulary, value.id);
  return <span>{title ?? value.id}</span>;
};
VocabularyValue.propTypes = {
  vocabulary: PropTypes.string.isRequired,
  value: PropTypes.shape({ id: PropTypes.string }).isRequired,
};

export const textOf = (value, vocabulary) => {
  if (isEmptyValue(value)) return "";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (typeof value === "string" || typeof value === "number")
    return String(value);
  if (Array.isArray(value)) {
    // steps: every item has only name + description → "1. name — description"
    if (isSteps(value))
      return value
        .map(
          (item, i) =>
            `${i + 1}. ${textOf(item.name, vocabulary)}${
              hasText(item.description)
                ? ` — ${textOf(item.description, vocabulary)}`
                : ""
            }`
        )
        .join("\n");
    // plain-scalar arrays join with ", " (the >5-items bulleted list is the
    // <Value> component's job — it returns JSX)
    return value.every(
      (v) => !isVocabulary(v) && (typeof v !== "object" || v === null)
    )
      ? value.map((v) => String(v)).join(", ")
      : "";
  }
  if (isValueUnit(value)) return valueUnitText(value);
  if (isAssessed(value)) return assessedText(value, vocabulary);
  // i18n dicts (a manual chemical's title, { en: "…" }) show their value
  if (isPlainObject(value) && typeof value.en === "string") return value.en;
  if (isVocabulary(value))
    // fall back to the record's own title before showing the raw id; the
    // lookup fn comes from a caller-declared vocabulary (see Value), else id
    return (
      (typeof vocabulary === "function" ? vocabulary(value.id) : null) ??
      value.title?.en ??
      value.id
    );
  return "";
};

const hasText = (v) => !isEmptyValue(v);

// string/number arrays longer than this become a bulleted list (§3)
const BULLET_THRESHOLD = 5;

// One formatted value; uses the suffix formatter when one is registered.
// `vocabulary` (a declared vocabulary type) switches `{ id }` display to
// the shared title cache instead of the raw id.
export const Value = ({ name, value, vocabulary }) => {
  const formatter = formatters[name]; // registry is keyed by path suffix
  if (formatter && !isEmptyValue(value)) return formatter(value);
  // a group entry declared the vocabulary: resolve title(s) via the cache
  if (vocabulary && isVocabulary(value))
    return <VocabularyValue vocabulary={vocabulary} value={value} />;
  if (
    vocabulary &&
    Array.isArray(value) &&
    value.length > 0 &&
    value.every(isVocabulary)
  )
    return value.map((v, i) => (
      <span key={v.id}>
        {i > 0 ? ", " : ""}
        <VocabularyValue vocabulary={vocabulary} value={v} />
      </span>
    ));
  if (
    Array.isArray(value) &&
    value.length > BULLET_THRESHOLD &&
    value.every(
      (v) => !isVocabulary(v) && (typeof v !== "object" || v === null)
    )
  )
    return (
      <ul>
        {value.map((item) => (
          <li key={String(item)}>{textOf(item)}</li>
        ))}
      </ul>
    );
  // manual chemical entry: title ({ en: "…" } or a plain string) plus the
  // grey hint (design §3). The marker is a plain-object value with a title
  // and NO id — a picked chemical always has one. The title itself is
  // localized first, so `{ en: "…" }` dicts render the same.
  const manualTitle =
    isPlainObject(value) && !isLeafObject(value) && value.id === undefined
      ? value.title?.en ?? value.title
      : undefined;
  if (typeof manualTitle === "string")
    return (
      <span>
        {textOf(manualTitle)} <Label basic size="mini" content="Manual entry" />
      </span>
    );
  if (isVocabulary(value) && value.id.startsWith("manual:"))
    return (
      <span>
        {value.title?.en ?? value.id}{" "}
        <Label basic size="mini" content="Manual entry" />
      </span>
    );
  if (isVocabulary(value) && !isEmptyValue(value.rank))
    // vocabulary with a saved rank: title plus extra info in grey (§3)
    return (
      <span>
        {textOf(value)} <span className="mbdb-muted-text">({value.rank})</span>
      </span>
    );
  const text = textOf(value);
  // numbered "steps" and long wrapped text keep their line breaks
  return text.includes("\n") ? (
    <span className="mbdb-pre-line">{text}</span>
  ) : (
    text
  );
};
Value.propTypes = {
  name: PropTypes.string.isRequired,
  value: PropTypes.any,
  vocabulary: PropTypes.string,
};

// The red message(s) under a value (design §5); survives Formik's errors
// reset via useFieldErrors, and opens the editor when onEdit is given.
export const ErrorNote = ({ path, onEdit }) => {
  const { messages } = useFieldErrors(path);
  if (messages.length === 0) return null;
  const text = messages.join(" ");
  if (!onEdit) return <div className="mbdb-error-text">{text}</div>;
  return (
    <button
      type="button"
      className="mbdb-error-text mbdb-link"
      onClick={onEdit}
    >
      {text}
    </button>
  );
};
ErrorNote.propTypes = {
  path: PropTypes.string.isRequired,
  onEdit: PropTypes.func,
};
