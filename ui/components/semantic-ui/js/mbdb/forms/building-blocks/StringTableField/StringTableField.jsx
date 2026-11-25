import React from "react";
import PropTypes from "prop-types";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";

// A flat array of strings (model: `type: array`, `items: keyword`) edited as a
// one-column table — one row per string, a remove button per row — instead of
// the taller labelled list oarepo's StringArrayField renders (one full-width
// field per row). It is the one-column sibling of the two-column
// ExternalDatabases table and is built on TableArrayField, which owns the table
// layout (design/building-blocks/StringTableField.md).
//
// The stored value is the string itself; the row shape ({ value }) lives only
// while editing and is serialized away on every write.
const serialize = (row) => row.value ?? "";
const deserialize = (stored) => ({ value: stored ?? "" });

export const StringTableField = ({
  fieldPath,
  columnLabel = "Value",
  addButtonLabel = "Add",
}) => (
  // minItems is deliberately not passed: these arrays are optional, so no
  // virtual empty row is shown (the model's `minItems: 1` holds because the key
  // only exists once a row is added, and an emptied array is dropped on save).
  <TableArrayField
    fieldPath={fieldPath}
    addButtonLabel={addButtonLabel}
    // a plain list of notes is never referred to by number, so no `#` column
    showIndex={false}
    // the column header is the table's own text: a table column is not a model
    // concept, and a keyword item has no model label (guide §6)
    columns={[{ field: "value", label: columnLabel }]}
    defaultNewValue=""
    serialize={serialize}
    deserialize={deserialize}
  />
);

StringTableField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  // the column header (e.g. "Specification") — the table's own text, not a
  // model label; the model has none for the item of a keyword array
  columnLabel: PropTypes.string,
  addButtonLabel: PropTypes.string,
};
