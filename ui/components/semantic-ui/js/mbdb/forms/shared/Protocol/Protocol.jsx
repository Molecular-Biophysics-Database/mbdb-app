import React from "react";
import PropTypes from "prop-types";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";

// An ordered list of steps (name + description) as an editable two-column
// table. Label, help, required and both column headers come from the model
// through fieldPath. Pass minItems={1} only where the model field is required
// (preparation_protocol); the optional uses start with no rows.
export const Protocol = ({ fieldPath, minItems = 0 }) => (
  <TableArrayField
    fieldPath={fieldPath}
    minItems={minItems}
    addButtonLabel="Add step"
    defaultNewValue={{}}
    columns={[
      { field: "name", width: 4 },
      { field: "description", type: "textarea" },
    ]}
  />
);

Protocol.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  minItems: PropTypes.number,
};
