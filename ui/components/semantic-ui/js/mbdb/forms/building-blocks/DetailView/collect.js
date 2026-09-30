import { useFieldData } from "@js/oarepo_ui/forms";
import { hasData, isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
import { isAssessed, isLeafObject, isPlainObject, isSteps } from "./values";

// Build the flat row list for one object out of its values. Pure (no hooks):
// error visibility is decided by the caller's `hasErr(path)` predicate, which
// the components fill with useFieldErrors — one hook call per row (F1).

// ponytail: one indent level; deeper nesting joins sub-headings with " › ".
// hasErr (optional): rows with a server error are kept even when empty.
export const collectRows = (
  obj,
  basePath,
  hasErr,
  heading = "",
  indent = false
) => {
  const rows = [];
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    const path = `${basePath}.${name}`;
    // hasErr is advisory (leaves render their own error note); the row is
    // re-checked at render time (Rows/FieldRow), so default to keeping it.
    const errored = !hasErr || hasErr(path);
    if (isEmptyValue(value) && !errored) return;
    const subHeading = heading ? `${heading} › ${name}` : name;
    if (isLeafObject(value) || !isPlainObject(value)) {
      if (
        Array.isArray(value) &&
        value.some((v) => isPlainObject(v) && !isLeafObject(v)) &&
        !isSteps(value)
      ) {
        // array of complex objects: heading + mini table
        rows.push({ kind: "heading", name: subHeading, path, indent });
        rows.push({ kind: "mini", name, path, items: value, indent });
      } else {
        rows.push({ kind: "field", name, path, value, indent, errored });
      }
      return;
    }
    // assessed objects are a single formatted line, not sub-rows (§3/F4c)
    if (isAssessed(value)) {
      rows.push({ kind: "field", name, path, value, indent, errored });
      return;
    }
    const inner = collectRows(value, path, hasErr, subHeading, true);
    if (inner.length > 0)
      rows.push({ kind: "heading", name: subHeading, path, indent });
    rows.push(...inner);
  });
  return rows;
};

// Split the object into per-group sections + an "Other" section. `required`
// is a Set of leaf names that get a red "Missing" row when absent (design §5).
export const groupSections = (
  obj,
  basePath,
  groups,
  exclude,
  required,
  hasErr
) => {
  const known = new Set(exclude);
  const sections = [];
  groups.forEach((group) => {
    const part = {};
    const missing = [];
    (group.fields ?? []).forEach((name) => {
      known.add(name);
      if (exclude.includes(name)) return;
      // a field with a server error stays visible even when empty (design §5)
      if (hasData(obj?.[name]) || hasErr?.(`${basePath}.${name}`))
        part[name] = obj?.[name];
      else if (required.has(name)) missing.push(name);
    });
    const rows = collectRows(part, basePath, hasErr);
    if (rows.length === 0 && missing.length === 0) return; // all-empty group
    sections.push({ title: group.title, rows, missing });
  });
  // keys in no group are never hidden: they go under "Other"
  const other = {};
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    if (!known.has(name) && (hasData(value) || hasErr?.(`${basePath}.${name}`)))
      other[name] = value;
  });
  const otherRows = collectRows(other, basePath, hasErr);
  if (otherRows.length > 0)
    sections.push({ title: "Other", rows: otherRows, missing: [] });
  return sections;
};

// F6: required defaults to the model flag for each group field; a non-empty
// caller-supplied prop replaces the default entirely (the escape hatch for
// polymorphic paths that have no ui_model children yet).
export const useMergedRequired = (fieldPath, groups, requiredPaths) => {
  const { getFieldData } = useFieldData();
  if (requiredPaths.length > 0) return new Set(requiredPaths);
  const merged = new Set();
  groups.forEach((group) =>
    (group.fields ?? []).forEach((name) => {
      const { required } = getFieldData({
        fieldPath: `${fieldPath}.${name}`,
        fieldRepresentation: "text",
      });
      if (required) merged.add(name);
    })
  );
  return merged;
};
