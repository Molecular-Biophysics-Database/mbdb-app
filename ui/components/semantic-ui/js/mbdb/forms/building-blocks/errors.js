import { getIn } from "formik";

// Shared helpers for the building blocks: Formik error walking and the
// "does this value hold user data" check.

// Formik errors are nested objects/arrays of strings; OARepo server errors may
// also be `{ message, severity }` objects. Collect every message string.
const collectMessages = (node, out) => {
  if (node === undefined || node === null) return out;
  if (typeof node === "string") {
    if (node !== "") out.push(node);
  } else if (Array.isArray(node)) {
    node.forEach((child) => collectMessages(child, out));
  } else if (typeof node === "object") {
    // ponytail: {message, severity} counts as one error via its message
    if (typeof node.message === "string") out.push(node.message);
    else Object.values(node).forEach((child) => collectMessages(child, out));
  }
  return out;
};

// Number of leaf error strings under path (0 when none).
export const countErrors = (errors, path) =>
  collectMessages(getIn(errors, path), []).length;

export const hasError = (errors, path) => countErrors(errors, path) > 0;

// Unique message strings under path, for display.
export const errorMessages = (errors, path) => [
  ...new Set(collectMessages(getIn(errors, path), [])),
];

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
