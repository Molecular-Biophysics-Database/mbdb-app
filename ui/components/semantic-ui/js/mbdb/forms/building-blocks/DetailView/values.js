import React from "react";
import PropTypes from "prop-types";
import { Label } from "mbdb-semantic-ui-react";
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

// §3: No, or Yes — <facts>, the remaining non-empty fields comma-joined
const assessedText = (value, vocabulary) => {
  if (value.assessed === "No") return "No";
  const facts = Object.keys(value)
    .filter((key) => key !== "assessed")
    .map((key) => textOf(value[key], vocabulary))
    .filter((t) => t !== "");
  return facts.length ? `Yes — ${facts.join(", ")}` : "Yes";
};

// Resolves a vocabulary id to a display title: a flat {id: title} map wins,
// otherwise a per-field {name: {id: title}} map. Exported for Rows.jsx's
// mini-table cells, which reuse the same resolution.
export const vocabularyLookup = (titles, name) => (id) =>
  titles?.[id] ?? titles?.[name]?.[id] ?? null;

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
  if (isValueUnit(value))
    return [value.value, value.unit].filter((x) => !isEmptyValue(x)).join(" ");
  if (isAssessed(value)) return assessedText(value, vocabulary);
  if (isVocabulary(value))
    // fall back to the record's own title before showing the raw id
    return vocabulary(value.id) ?? value.title?.en ?? value.id;
  return "";
};

const hasText = (v) => !isEmptyValue(v);

// string/number arrays longer than this become a bulleted list (§3)
const BULLET_THRESHOLD = 5;

// One formatted value; uses the suffix formatter when one is registered.
export const Value = ({ name, value, titles }) => {
  const vocabulary = vocabularyLookup(titles, name);
  const formatter = formatters[name]; // registry is keyed by path suffix
  if (formatter && !isEmptyValue(value)) return formatter(value);
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
          <li key={String(item)}>{textOf(item, vocabulary)}</li>
        ))}
      </ul>
    );
  if (
    isPlainObject(value) &&
    !isLeafObject(value) &&
    typeof value.title === "string"
  )
    // manual chemical entry: title plus a grey hint (design §3)
    return (
      <span>
        {textOf(value.title, vocabulary)}{" "}
        <Label basic size="mini" content="Manual entry" />
      </span>
    );
  if (isVocabulary(value) && !isEmptyValue(value.rank))
    // vocabulary with a saved rank: title plus extra info in grey (§3)
    return (
      <span>
        {textOf(value, vocabulary)}{" "}
        <span className="ui grey text">({value.rank})</span>
      </span>
    );
  const text = textOf(value, vocabulary);
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
  titles: PropTypes.object,
};

// The red message(s) under a value (design §5); survives Formik's errors
// reset via useFieldErrors, and opens the editor when onEdit is given.
export const ErrorNote = ({ path, onEdit }) => {
  const { messages } = useFieldErrors(path);
  if (messages.length === 0) return null;
  const text = messages.join(" ");
  if (!onEdit) return <div className="ui red text">{text}</div>;
  return (
    <button type="button" className="ui red text mbdb-link" onClick={onEdit}>
      {text}
    </button>
  );
};
ErrorNote.propTypes = {
  path: PropTypes.string.isRequired,
  onEdit: PropTypes.func,
};
