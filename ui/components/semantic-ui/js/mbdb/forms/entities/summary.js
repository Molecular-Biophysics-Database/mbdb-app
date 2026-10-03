import React from "react";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";

// The parts of a summary line are positional (title, then the facts) and never
// reorder, so the index is a legitimate key (carries meaning, not identity).
/* eslint-disable react/no-array-index-key */

// Joins the non-empty parts of a one-line entity summary with ", ", dropping
// empty/absent parts together with their separator. Written once for every
// entity summary (plan step 4); no input → "". No JSX: this file stays .js.
export const joinParts = (parts) => {
  const kept = parts.filter((part) => !isEmptyValue(part));
  if (kept.length === 0) return "";
  return React.createElement(
    React.Fragment,
    null,
    kept.map((part, i) =>
      React.createElement(React.Fragment, { key: i }, i > 0 ? ", " : "", part)
    )
  );
};

// "3 components" / "1 component"; "" when the list has no item. Shared by the
// molecular assembly and the lipid assembly summaries (plan 4R, Y3).
export const componentCount = (components) => {
  const n = components?.length;
  if (!n) return "";
  return `${n} component${n === 1 ? "" : "s"}`;
};

// One `{ id }` vocabulary reference as a title from the shared cache, or "" when
// absent. The `?.id` guard means an empty object renders nothing (a bare
// VocabularyValue without an id would). Shared by the entity summaries (plan
// 4R, Y3); a component, so no hook here.
export const vocabularyPart = (vocabulary, value) =>
  value?.id ? React.createElement(VocabularyValue, { vocabulary, value }) : "";
