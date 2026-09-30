import React from "react";
import PropTypes from "prop-types";
import { HelpIcon, Table } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// One column header; the label and required flag default to the model entry
// of `<fieldPath>.<column.field>` (explicit column props win, design/API).
// A component per column, so the hook is not called in a loop.
export const ColumnHeader = ({ fieldPath, column }) => {
  const data = useModelFieldData(`${fieldPath}.${column.field}`, {
    label: column.label,
    required: column.required,
  });
  return (
    <Table.HeaderCell width={column.width}>
      {data.label}
      {data.required ? <span className="mbdb-required"> *</span> : null}
      {data.helpText && (
        <>
          {" "}
          <HelpIcon help={data.helpText} label={data.label} />
        </>
      )}
    </Table.HeaderCell>
  );
};
ColumnHeader.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  column: PropTypes.object.isRequired,
};

// The table's header row: # + one ColumnHeader per column + the empty
// expand-toggle and actions columns.
export const HeaderRow = ({ fieldPath, columns, renderExpanded }) => (
  <Table.Header>
    <Table.Row>
      <Table.HeaderCell>#</Table.HeaderCell>
      {columns.map((column) => (
        <ColumnHeader
          key={column.field}
          fieldPath={fieldPath}
          column={column}
        />
      ))}
      {renderExpanded && <Table.HeaderCell />}
      <Table.HeaderCell />
    </Table.Row>
  </Table.Header>
);
HeaderRow.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  columns: PropTypes.arrayOf(PropTypes.object).isRequired,
  renderExpanded: PropTypes.func,
};
