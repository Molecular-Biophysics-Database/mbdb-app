import { useRef } from "react";
import { getIn, useFormikContext } from "formik";
import { randomUUID } from "./randomUUID";

// Shared bookkeeping for the two array blocks (TableArrayField and
// ModalArrayField): reads the item list from Formik, keeps client-only keys
// in a ref parallel to the rows, and removes/pushes/replaces items with
// setFieldValue (never arrayHelpers) so all three live in one place.
// Entities keep their own `id` as the key; items without one (components,
// steps) get a minted key. Using setFieldValue means an empty list becomes
// `undefined` — guide §7 forbids writing `[]`.
//
// CEILING (PoC only): the ref grows during render, which breaks StrictMode
// assumptions (a double render mints unused keys) and a value replaced
// outside the block's own handlers (form reinit) mints fresh keys without
// remounting rows. Contained today because keys only matter within one
// mount. Do not copy into production code blindly.
export const useArrayRows = (fieldPath) => {
  const { values, setFieldValue } = useFormikContext();
  const items = getIn(values, fieldPath) ?? [];
  const keysRef = useRef(null);
  if (keysRef.current === null) keysRef.current = items.map(() => randomUUID());
  while (keysRef.current.length < items.length)
    keysRef.current.push(randomUUID());
  // external replacement (serializer round trip, reinit) can shrink the list;
  // truncate so a replaced item keeps its slot's key instead of minting anew
  if (keysRef.current.length > items.length)
    keysRef.current.length = items.length;

  const keyFor = (item, index) => item?.id ?? keysRef.current[index];

  const remove = (index) => {
    const next = items.filter((_, i) => i !== index);
    keysRef.current.splice(index, 1);
    setFieldValue(fieldPath, next.length === 0 ? undefined : next);
  };

  const push = (value) => {
    keysRef.current.push(randomUUID());
    setFieldValue(fieldPath, [...items, value]);
  };

  const replace = (index, value) =>
    setFieldValue(`${fieldPath}.${index}`, value);

  return { items, keyFor, remove, push, replace };
};
