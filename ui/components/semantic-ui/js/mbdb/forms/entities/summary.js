import React from "react";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";

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
