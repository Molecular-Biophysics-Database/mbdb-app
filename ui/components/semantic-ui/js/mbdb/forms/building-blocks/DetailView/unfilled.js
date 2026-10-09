import { getIn } from "formik";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
import { isAssessed, isLeafObject } from "./values";

// Pure (design ReviewMode.md rule 4): from a (variant-resolved) ui_model node
// and the stored value, the relative paths of the HIGHEST absent nodes, so a
// detail view can list what is not filled. `node.children` are the model's
// fields for the item's variant (the caller resolves the variant).
//
// - a present object's absent nested fields are listed recursively
//   (`storage.duration`), never the object itself when it is present;
// - an absent object is reported as the object (`storage`), not its children;
// - arrays of objects are NOT walked (an absent array is reported by its label;
//   a present one leaves each item's own details to list its own);
// - required-and-empty fields are skipped (they have their red "Missing" row);
// - `exclude` keys (id, the discriminator, the row's own columns, …) are never
//   listed.
const isObjectValue = (v) =>
  v !== null && typeof v === "object" && !Array.isArray(v);

// A present object the details recurse into: a plain object that is NOT a leaf
// reference (vocabulary / value-unit), NOT an assessed value and NOT a manual
// chemical — the same things `collectRows` renders as one row, not a descent.
// An assessed value (`{ assessed: "Yes", … }`) is exactly the "Not filled:
// Identity, Homogeneity" case: when present it is a single line, so its method
// fields (by_intact_mass / by_sequencing / by_fingerprinting — alternatives)
// must never be listed individually.
const recursable = (v) =>
  isObjectValue(v) &&
  !isLeafObject(v) &&
  !isAssessed(v) &&
  !(
    v.id === undefined &&
    (typeof v.title === "string" || typeof v.title?.en === "string")
  );

export const unfilledPaths = (node, value, { exclude = [] } = {}) => {
  const excluded = new Set(exclude);
  const walk = (n, v, prefix) => {
    const out = [];
    Object.entries(n?.children ?? {}).forEach(([name, child]) => {
      // `@v` (and any `@…`) is a server-added version field, never data
      if (excluded.has(name) || name.startsWith("@")) return;
      const path = prefix ? `${prefix}.${name}` : name;
      const fieldValue = getIn(v, name);
      if (isEmptyValue(fieldValue)) {
        if (child.required) return; // "Missing" row instead
        out.push(path);
        return;
      }
      // a present plain object: recurse into its absent nested fields. A
      // vocabulary ({id} or {title}) / value-unit object is a LEAF reference
      // (its keys are model internals, not user fields): never recurse.
      if (child.children && recursable(fieldValue)) {
        out.push(...walk(child, fieldValue, path));
      }
      // arrays of objects and leaves: nothing more to list
    });
    return out;
  };
  return walk(node, value, "");
};
