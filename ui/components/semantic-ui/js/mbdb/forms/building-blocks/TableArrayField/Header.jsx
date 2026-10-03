import React from "react";
import PropTypes from "prop-types";
import { HelpIcon, Table } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// One column title; the label and required flag default to the model entry
// of `<fieldPath>.<column.field>` (explicit column props win, design/API).
// A component per column, so the hook is not called in a loop.
export const ColumnTitle = ({ fieldPath, column }) => {
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
ColumnTitle.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  column: PropTypes.object.isRequired,
};

// The table's header row: `#` (unless showIndex is false) + one ColumnTitle per
// column + the empty expand-toggle and actions columns.
export const HeaderRow = ({
  fieldPath,
  columns,
  renderExpanded,
  showIndex,
}) => (
  <Table.Header>
    <Table.Row>
      {showIndex && <Table.HeaderCell>#</Table.HeaderCell>}
      {columns.map((column) => (
        <ColumnTitle key={column.field} fieldPath={fieldPath} column={column} />
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
  // false hides the leading `#` column (a plain list, not referred to by number)
  showIndex: PropTypes.bool,
};
