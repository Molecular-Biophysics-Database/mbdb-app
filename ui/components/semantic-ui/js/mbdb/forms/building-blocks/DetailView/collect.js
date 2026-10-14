import { getIn, useFormikContext } from "formik";
import { useReviewMode } from "mbdb-semantic-ui-react";
import { useModelResolver } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  collectMessages,
  hasData,
  isEmptyValue,
  mergedErrorNode,
} from "@js/mbdb/forms/building-blocks/errors";
import { formatters } from "./formatters";
import { unfilledPaths } from "./unfilled";
import { isAssessed, isLeafObject, isPlainObject, isSteps } from "./values";

// A group field entry is a plain name or
// `{ field, vocabulary?, itemColumns?, itemGroups? }`:
// - `vocabulary`: declared per field so details can resolve vocabulary titles
//   by GET (the shared per-id cache);
// - `itemColumns` + `itemGroups`: for a field that is an ARRAY of complex
//   objects, the array's own columns (the read-only mini table inside these
//   details shows the same columns as the array's edit table) and its items'
//   details groups (the mini row's own ▸ opens the item's details grouped
//   exactly like its form, resolving vocabularies — design DetailView §3/§4).
//   `itemGroups` may also be `(itemValue) => groups` for a polymorphic item.
// - `children`: for an array of complex objects that lives INSIDE a nested
//   object (e.g. `modifications.biological_postprocessing`), an object mapping
//   each child array's name to its `{ itemColumns, itemGroups }` spec (design §2b
//   rule 4).
export const fieldEntryOf = (entry) =>
  typeof entry === "string"
    ? { name: entry }
    : {
        name: entry.field,
        vocabulary: entry.vocabulary,
        itemColumns: entry.itemColumns,
        itemGroups: entry.itemGroups,
        children: entry.children,
      };

// Build the flat row list for one object out of its values. Pure (no hooks):
// error visibility is decided by the caller's `hasErr(path)` predicate, which
// the components fill with useFieldErrors — one hook call per row.

// ponytail: one indent step per level; deeper nesting joins sub-headings with
// " › ". `depth` is the indentation level (design §2a): a group's own field rows
// are depth 1, a nested object's rows one more, and so on.
// hasErr (optional): rows with a server error are kept even when empty.
export const collectRows = (obj, basePath, hasErr, depth = 1) => {
  const rows = [];
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    const path = `${basePath}.${name}`;
    // hasErr is advisory (leaves render their own error note); the row is
    // re-checked at render time (Rows/FieldRow), so default to keeping it.
    const errored = !hasErr || hasErr(path);
    if (isEmptyValue(value) && !errored) return;
    // §2b rule 3: a sub-heading shows only its own label; the indentation shows
    // the hierarchy, so the parents' chain is redundant.
    const subHeading = name;
    // A registered formatter replaces the generic output for this leaf name
    // (design §3): it renders the value itself, so never recurse into it. This
    // is what shows a `location` as one line plus the map link, and a
    // `basic_information` with its formula and weight.
    if (formatters[name] && !isEmptyValue(value)) {
      rows.push({ kind: "field", name, path, value, depth, errored });
      return;
    }
    if (isLeafObject(value) || !isPlainObject(value)) {
      if (
        Array.isArray(value) &&
        value.some((v) => isPlainObject(v) && !isLeafObject(v)) &&
        !isSteps(value)
      ) {
        // array of complex objects: heading + mini table (both at this depth;
        // the mini table's cell is the field's row)
        rows.push({ kind: "heading", name: subHeading, path, depth });
        rows.push({ kind: "mini", name, path, items: value, depth });
      } else {
        rows.push({ kind: "field", name, path, value, depth, errored });
      }
      return;
    }
    // assessed objects are a single formatted line, not sub-rows (§3)
    if (isAssessed(value)) {
      rows.push({ kind: "field", name, path, value, depth, errored });
      return;
    }
    // a manual chemical ({ id } missing, title/string-or-i18n-dict present):
    // one formatted line with the grey hint (§3), not a recursive descent
    if (
      isPlainObject(value) &&
      value.id === undefined &&
      (typeof value.title === "string" || typeof value.title?.en === "string")
    ) {
      rows.push({ kind: "field", name, path, value, depth, errored });
      return;
    }
    // a nested object: its sub-heading is at this depth, its rows one deeper
    const inner = collectRows(value, path, hasErr, depth + 1);
    if (inner.length > 0)
      rows.push({ kind: "heading", name: subHeading, path, depth });
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
  hasErr,
  review = {}
) => {
  const { reviewMode = false, node: itemNode } = review;
  const known = new Set(exclude);
  const sections = [];
  const vocabularies = {};
  // per-field spec for an array of complex objects (its mini columns + the
  // items' details groups), carried onto the collected "mini" row so the
  // read-only mini table can use it
  const arraySpecs = {};
  groups.forEach((group) => {
    const part = {};
    const missing = [];
    const fieldNames = [];
    (group.fields ?? []).forEach((entry) => {
      const { name, vocabulary, itemColumns, itemGroups, children } =
        fieldEntryOf(entry);
      known.add(name);
      if (exclude.includes(name)) return;
      fieldNames.push(name);
      // an array-of-complex field declares its mini columns + item groups here,
      // keyed by the mini row's PATH, so an array inside a nested object
      // (modifications.biological_postprocessing) can declare one too, through
      // the entry's `children` (design §2b rule 4)
      if (itemColumns || itemGroups)
        arraySpecs[`${basePath}.${name}`] = { itemColumns, itemGroups };
      Object.entries(children ?? {}).forEach(([child, spec]) => {
        arraySpecs[`${basePath}.${name}.${child}`] = spec;
      });
      // a field with a server error stays visible even when empty (design §5)
      if (hasData(obj?.[name]) || hasErr?.(`${basePath}.${name}`)) {
        part[name] = obj?.[name];
        if (vocabulary) vocabularies[name] = vocabulary;
      } else if (required.has(name)) missing.push(name);
    });
    const rows = collectRows(part, basePath, hasErr).map((row) => {
      if (row.kind === "field" && vocabularies[row.name])
        return { ...row, vocabulary: vocabularies[row.name] };
      if (row.kind === "mini" && arraySpecs[row.path])
        return { ...row, ...arraySpecs[row.path] };
      return row;
    });
    // §2a rule 3: no duplicated headings. A group with exactly one field does
    // not repeat the field's own heading:
    // - a plain value needs no group header at all (the field row is enough);
    // - an array (mini table) or a nested object keeps the group header and
    //   drops the field's sub-heading, and its rows move up one depth.
    const one = (group.fields ?? []).length === 1;
    let title = group.title;
    let finalRows = rows;
    if (one) {
      if (rows[0]?.kind === "heading")
        finalRows = rows
          .slice(1)
          .map((row) => ({ ...row, depth: Math.max(1, row.depth - 1) }));
      else {
        // §2b rule 2: a header-less one-field plain group's row is a sibling of
        // the groups (depth 0, aligned with the headers), not a row of the
        // group above, and takes the group's top spacing.
        title = undefined;
        finalRows = rows.map((row) => ({ ...row, depth: 0, groupGap: true }));
      }
    }
    // review mode (design ReviewMode.md rules 4, 5): the group's absent fields,
    // highest node only, required-and-empty skipped (they are `missing`). A
    // header-less one-field group shows its row as "not filled" instead.
    let notFilled = [];
    if (reviewMode) {
      if (one && title === undefined) {
        if (finalRows.length === 0)
          finalRows = [
            {
              kind: "field",
              name: fieldNames[0],
              path: `${basePath}.${fieldNames[0]}`,
              value: undefined,
              depth: 0,
              groupGap: true,
              notFilled: true,
              errored: false,
            },
          ];
      } else {
        const sub = {};
        fieldNames.forEach((name) => {
          if (missing.includes(name)) return;
          const childNode = itemNode?.children?.[name];
          if (childNode) sub[name] = childNode;
        });
        notFilled = unfilledPaths({ children: sub }, obj ?? {}, { exclude });
      }
    }
    if (
      finalRows.length === 0 &&
      missing.length === 0 &&
      notFilled.length === 0
    )
      return; // all-empty (and not review mode)
    sections.push({ title, rows: finalRows, missing, notFilled });
  });
  // keys in no group are never hidden: they go under "Other"
  const other = {};
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    if (!known.has(name) && (hasData(value) || hasErr?.(`${basePath}.${name}`)))
      other[name] = value;
  });
  const otherRows = collectRows(other, basePath, hasErr);
  // NOTE (design ReviewMode.md rule 6): "Other" gets no not-filled line. The
  // ui_model's polymorphic node stores the UNION of every variant's fields in
  // `children` (variants[value] holds only the diff, not the field set), so a
  // field no group lists cannot be told from another variant's field here. The
  // per-type "every model field is in its group spec" test keeps Other empty
  // (no rows, no line).
  if (otherRows.length > 0)
    sections.push({
      title: "Other",
      rows: otherRows,
      missing: [],
      notFilled: [],
    });
  return sections;
};

// Required defaults to the model flag for each group field, resolved the
// variant-aware way (R0): the union ui_model says `organ` is optional (Cell
// fraction has it so), so a Solid tissue sample would never be Missing. A
// non-empty caller-supplied prop replaces the default entirely (the escape
// hatch for polymorphic paths with no ui_model children yet).
export const useMergedRequired = (fieldPath, groups, requiredPaths) => {
  const resolve = useModelResolver();
  if (requiredPaths.length > 0) return new Set(requiredPaths);
  const merged = new Set();
  groups.forEach((group) =>
    (group.fields ?? []).forEach((entry) => {
      const { name } = fieldEntryOf(entry);
      if (resolve(`${fieldPath}.${name}`).data.required) merged.add(name);
    })
  );
  return merged;
};

// The grouped sections of the object at `fieldPath`, memo-free: the one place
// that turns Formik `values` + `errors` ∪ `initialErrors` into the section
// list a detail table renders. `DetailView` (the top level) and a mini row's
// own ▸ (its item's groups) both read it, so they render identically. Returns
// null when the object is absent (nothing to show).
export const useSections = (fieldPath, groups, exclude, requiredPaths) => {
  const formik = useFormikContext();
  const resolve = useModelResolver();
  const reviewMode = useReviewMode();
  const required = useMergedRequired(fieldPath, groups, requiredPaths);
  // Rows with a server error stay visible even when empty (design §5). collect
  // is pure (no hooks), so it cannot call useFieldErrors; mergedErrorNode is
  // the same errors∪initialErrors selection as a plain function, and the row
  // is kept when that node holds any message. Each leaf row still re-checks
  // via useFieldErrors at render.
  const hasErr = (path) =>
    collectMessages(mergedErrorNode(formik, path), []).length > 0;
  const obj = getIn(formik.values, fieldPath);
  if (obj === undefined || obj === null) return null;
  return groupSections(
    isPlainObject(obj) ? obj : {},
    fieldPath,
    groups,
    exclude,
    required,
    hasErr,
    { reviewMode, node: resolve(fieldPath).node }
  );
};
