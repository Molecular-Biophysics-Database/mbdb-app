import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";

// The help placement a row gives its fields (guide §8, help placement):
// `undefined` = not in a row, so a field uses its own default; `"control"` =
// a Form.Group row, where every field puts its help directly under its control
// so the row's columns line up. Without this a row that mixes a composite
// (a button group) with a simple control put the two helps at different
// heights — the Purity row: `Method` (select) below its control, `Purity
// percentage` (buttons) under its label (lead, 2026-10-04).
export const RowHelpPlacement = React.createContext(undefined);

// Read by the composite blocks (ButtonGroupField, DiscriminatorField) to prefer
// the row's placement over their own "label" default. A plain field already
// defaults to "control", so it needs no special handling; the tall blocks (a
// table, a string list) always pass "label" and ignore this on purpose.
export const useRowHelpPlacement = () => React.useContext(RowHelpPlacement);

// A `Form.Group` row for this design: it takes the same props as Semantic's
// `Form.Group` and additionally provides the row help placement ("control") to
// every field inside it.
export const FieldRow = ({ children, ...groupProps }) => (
  <RowHelpPlacement.Provider value="control">
    <Form.Group {...groupProps}>{children}</Form.Group>
  </RowHelpPlacement.Provider>
);

FieldRow.propTypes = {
  children: PropTypes.node.isRequired,
};
