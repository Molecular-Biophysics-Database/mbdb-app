import { getIn, setIn, useFormikContext } from "formik";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";

// Formik's setFieldValue(path, undefined) drops the leaf but leaves empty
// parent objects behind (C15: clearing the last field of `location` leaves
// `location: {}`). Guide §7 forbids `{}` in the form data, so a clear must
// walk up and drop plain-object parents that no longer hold data. It stops
// at arrays and at objects that sit inside an array (removing an item would
// shift indexes; the serializer strips empty items there).
// `values` must be the current Formik `values` from the same render.

const isPlainObject = (v) =>
  v !== null && typeof v === "object" && !Array.isArray(v);

const parentOf = (path) => path.split(".").slice(0, -1).join(".");

// Replaces every `setFieldValue(path, undefined)` that means "clear this field".
// Removes the leaf and every now-empty plain-object parent up to (but never
// touching) an array or the form root.
export const unsetFieldValue = (values, setFieldValue, path) => {
  let next = setIn(values, path, undefined);
  setFieldValue(path, undefined);
  let parentPath = parentOf(path);
  while (parentPath) {
    const parent = getIn(next, parentPath);
    if (!isPlainObject(parent)) break;
    if (Array.isArray(getIn(next, parentOf(parentPath)))) break;
    if (!isEmptyValue(parent)) break;
    next = setIn(next, parentPath, undefined);
    setFieldValue(parentPath, undefined);
    parentPath = parentOf(parentPath);
  }
};

// Hook sugar for the common case inside a block.
export const useUnsetField = () => {
  const { values, setFieldValue } = useFormikContext();
  return (path) => unsetFieldValue(values, setFieldValue, path);
};
