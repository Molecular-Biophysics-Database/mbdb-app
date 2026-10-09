import { getIn, useFormikContext } from "formik";
import isEqual from "lodash/isEqual";

// Shared helpers for the building blocks: Formik error walking and the
// "does this value hold user data" check.

// Formik errors are nested objects/arrays of strings; OARepo server errors may
// also be `{ message, severity }` objects. Only real errors count: severity
// undefined (client errors have none) or "error". oarepo may also send
// "info"/"warning" — those must NOT turn cells red, so they count 0 and are
// excluded from messages. Non-message objects are walked recursively.
// Exported for DetailView's pure collect path: it resolves the merged node
// via mergedErrorNode and needs to know whether that node holds any message
// (without running the hooks).
export const collectMessages = (node, out = []) => {
  if (node === undefined || node === null) return out;
  if (typeof node === "string") {
    if (node !== "") out.push(node);
  } else if (Array.isArray(node)) {
    node.forEach((child) => collectMessages(child, out));
  } else if (typeof node === "object") {
    if (typeof node.message === "string") {
      if (node.severity === undefined || node.severity === "error")
        out.push(node.message);
    } else Object.values(node).forEach((child) => collectMessages(child, out));
  }
  return out;
};

// Number of leaf error strings under path (0 when none). Duplicates are
// counted (three "Too short." = 3) — badges show the count of raw leaves, as
// the server sent them; errorMessages() is the deduped display variant.
export const countErrors = (errors, path) =>
  collectMessages(getIn(errors, path), []).length;

export const hasError = (errors, path) => countErrors(errors, path) > 0;

// Unique message strings under path, for display.
export const errorMessages = (errors, path) => [
  ...new Set(collectMessages(getIn(errors, path), [])),
];

// errors-else-initialErrors selection. The deposit form passes server errors
// as Formik `initialErrors`; it has no `validate` and keeps validateOnChange,
// so the first change anywhere in the form resets `errors` to {} (formik's
// SET_ERRORS). The live `errors` node wins while it has messages; otherwise
// the `initialErrors` node applies — but only while the value at `path` still
// equals `initialValues` at `path` (a changed value means the server error no
// longer applies).
//
// Exported pure so callers that cannot run hooks (DetailView's collect,
// which builds rows outside a component) can pass a hand-built formik-ish
// { errors, initialErrors, values, initialValues } and get the same selection.
export const mergedErrorNode = (
  { errors, initialErrors, values, initialValues },
  path
) => {
  const current = getIn(errors, path);
  if (collectMessages(current, []).length > 0) return current;
  const unchanged = isEqual(getIn(values, path), getIn(initialValues, path));
  return unchanged ? getIn(initialErrors, path) : undefined;
};

// THE way building blocks read errors for a path. Covers everything under
// the path (cells, list, nested rows) and survives the formik errors-reset:
// an unrelated edit clears `errors` but `initialErrors` survive, so the
// fallback keeps showing the server error until its own value is edited.
export const useFieldErrors = (path) => {
  const formik = useFormikContext();
  const raw = collectMessages(mergedErrorNode(formik, path), []);
  return {
    count: raw.length,
    messages: [...new Set(raw)],
    hasError: raw.length > 0,
  };
};

// Only the message(s) sitting exactly at `path` — a string or {message}
// object — never messages from nested sub-paths. For list/object-level
// errors (`dbs: "Missing data for required field."`, `dbs.0: "…"`), which
// would otherwise double-report errors already shown at their own inputs.
export const useOwnErrorMessages = (path) => {
  const formik = useFormikContext();
  const node = mergedErrorNode(formik, path);
  return collectOwnMessages(node, []);
};

const collectOwnMessages = (node, out) => {
  if (typeof node === "string") {
    if (node !== "") out.push(node);
  } else if (
    node !== null &&
    typeof node === "object" &&
    !Array.isArray(node) &&
    typeof node.message === "string" &&
    (node.severity === undefined || node.severity === "error")
  ) {
    out.push(node.message);
  }
  return out;
};

// A value is empty when it holds no user-entered data: undefined, null, "",
// an empty array, or an object/array whose entries are all empty.
export const isEmptyValue = (value) => {
  if (value === undefined || value === null || value === "") return true;
  if (Array.isArray(value)) return value.every(isEmptyValue);
  if (typeof value === "object")
    return Object.values(value).every(isEmptyValue);
  return false;
};

// 0 and false count as data.
export const hasData = (value) => !isEmptyValue(value);
