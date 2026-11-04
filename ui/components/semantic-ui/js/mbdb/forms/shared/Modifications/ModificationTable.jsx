import React from "react";
import PropTypes from "prop-types";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { Protocol } from "@js/mbdb/forms/shared/Protocol";
import { stepsLabel } from "./stepsLabel";

// One list of Modification items (type/position, expandable protocol rows).
// Used by Modifications (biological_postprocessing, chemical) and directly
// for a molecular assembly's chemical_modifications. Labels, help and the
// column headers come from the model; a row with an error anywhere below it
// opens by itself (TableArrayField), so a protocol error is never hidden.
export const ModificationTable = ({ fieldPath }) => {
  // The list's model label ("Biological postprocessing" / "Chemical" /
  // "Chemical modifications"): the Modifications group shows two tables with
  // the same "Add modification" button, so the aria-label names the list.
  const { label } = useModelFieldData(fieldPath);
  return (
    <TableArrayField
      fieldPath={fieldPath}
      addButtonLabel="Add modification"
      addButtonAriaLabel={label ? `Add modification to ${label}` : undefined}
      defaultNewValue={{}}
      columns={[
        { field: "type", width: 6 },
        { field: "position", width: 3 },
      ]}
      expandToggle={(row) => stepsLabel(row.protocol)}
      renderExpanded={(itemPath) => (
        <Protocol fieldPath={`${itemPath}.protocol`} />
      )}
    />
  );
};

ModificationTable.propTypes = {
  // the ARRAY path (e.g. `${itemPath}.modifications.chemical`)
  fieldPath: PropTypes.string.isRequired,
};

// The modification array's read-only mini-table columns (design DetailView §2b
// rule 4): the edit table's order, Type | Position | Protocol. All three are
// columns, so a modification row gets no ▸ in the details. Shared by the
// Polymer's `modifications.*` (through `children`) and a molecular assembly's
// `chemical_modifications`, so the two mini tables cannot drift.
export const MODIFICATION_ITEM_SPEC = {
  itemColumns: [
    { field: "type", label: "Type", value: (m) => m?.type ?? "" },
    { field: "position", label: "Position", value: (m) => m?.position ?? "" },
    {
      field: "protocol",
      label: "Protocol",
      value: (m) => (m?.protocol?.length ? stepsLabel(m.protocol) : ""),
    },
  ],
};
