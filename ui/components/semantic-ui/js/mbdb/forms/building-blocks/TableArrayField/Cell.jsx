import React from "react";
import PropTypes from "prop-types";
import { Form, Input, Label } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";
import { toOption } from "@js/mbdb/forms/building-blocks/options";
import { autoRows } from "@js/mbdb/forms/building-blocks/TextField";

// Label-less cell input; the column header is its label (aria-label).
// Clearing any cell kind maps "" to undefined (guide §7: never write "").
export const Cell = ({ column, row, label, onChange, error }) => {
  const value = row?.[column.field];
  const common = {
    "aria-label": label,
    error: error !== undefined,
    value: value ?? "",
    onChange: (e, { value: next }) => onChange(next === "" ? undefined : next),
  };
  if (column.type === "textarea")
    // SUIR 2.1.5 TextArea has no autoHeight; size rows to the content
    // (floor of 1: table cells stay one line high until the text grows).
    return <Form.TextArea rows={autoRows(value, { min: 1 })} {...common} />;
  if (column.type === "number")
    return (
      <Input
        type="number"
        {...common}
        onChange={(e) =>
          onChange(e.target.value === "" ? undefined : Number(e.target.value))
        }
      />
    );
  if (column.type === "select") {
    // allowAdditions: a stored value that is not in the options (an added
    // database, or one from a saved record) would render as the placeholder —
    // append it so Semantic can display it
    const options = (column.options ?? []).map((opt) =>
      typeof opt === "string"
        ? toOption(opt)
        : { key: opt.value, value: opt.value, text: opt.label ?? opt.value }
    );
    if (
      column.allowAdditions &&
      value != null &&
      value !== "" &&
      !options.some((opt) => opt.value === value)
    )
      options.push({ key: value, value, text: value });
    return (
      <Form.Dropdown
        search
        selection
        clearable
        selectOnBlur={false}
        allowAdditions={column.allowAdditions}
        options={options}
        aria-label={label}
        error={error !== undefined}
        value={value ?? ""}
        onChange={(e, { value: next }) =>
          onChange(next === "" ? undefined : next)
        }
      />
    );
  }
  return <Input {...common} />;
};
Cell.propTypes = {
  column: PropTypes.object.isRequired,
  row: PropTypes.any,
  label: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  error: PropTypes.string,
};

// One editable data cell: resolves the column label from the model (the same
// resolution the ColumnTitle uses — the LIST path, so input aria-labels match
// the header) and the cell's own errors via useFieldErrors.
export const DataCell = ({ fieldPath, itemPath, column, row, onChange }) => {
  const data = useModelFieldData(`${fieldPath}.${column.field}`, {
    label: column.label,
    required: column.required,
  });
  const { messages } = useFieldErrors(`${itemPath}.${column.field}`);
  const cellError = messages.join(" ");
  return (
    <>
      <Cell
        column={column}
        row={row}
        label={data.label ?? column.field}
        error={cellError || undefined}
        onChange={onChange}
      />
      {cellError !== "" && (
        <Label basic color="red" pointing>
          {cellError}
        </Label>
      )}
    </>
  );
};
DataCell.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  itemPath: PropTypes.string.isRequired,
  column: PropTypes.object.isRequired,
  row: PropTypes.any,
  onChange: PropTypes.func.isRequired,
};
