import React, { useRef, useState } from "react";
import PropTypes from "prop-types";
import { FieldArray, getIn, useFormikContext } from "formik";
import {
  Button,
  FieldHelp,
  Form,
  HelpLabel,
  Icon,
  Label,
  Table,
  useDisclosureDefault,
} from "mbdb-semantic-ui-react";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";
import { randomUUID } from "@js/mbdb/forms/building-blocks/randomUUID";
import { DataCell } from "./Cell";
import { HeaderRow } from "./Header";

const identity = (x) => x;

// One data row. A component (not a render callback) so hooks can be used per
// row: the expand state and the row-level error read formik context.
const Row = ({
  fieldPath,
  itemPath,
  index,
  storedItem,
  columns,
  deserialize,
  expanded,
  onToggleExpand,
  onRowChange,
  onRemove,
  renderExpanded,
  expandToggle,
  rowHint,
  showIndex,
  colSpan,
}) => {
  const row = deserialize(storedItem);
  // The open state is derived on every render — an explicit user toggle
  // wins; otherwise the playground's one-shot "Expand/Collapse all" default
  // (DisclosureDefaultProvider); otherwise a row with errors under it opens
  // automatically (initialErrors count, including new ones set on this SAME
  // mounted form after a failed save)
  const rowHasError = useFieldErrors(itemPath).hasError;
  const disclosure = useDisclosureDefault();
  const defaultOpen =
    disclosure === "open"
      ? true
      : disclosure === "closed"
      ? false
      : rowHasError;
  const isOpen = expanded ?? defaultOpen;
  // A string/{message} error AT the item itself (serialize tables store
  // strings, so `dbs.0: "…"` lands here) is shown in the actions cell
  const rowMessages = useOwnErrorMessages(itemPath);
  const hint = rowHint?.(row);
  // An open row and its expanded content read as one (plan 4R Y12 /
  // TableArrayField-review P8-F1, option A): the data row and the expanded
  // <tr>s share `mbdb-row-open` (tint + left accent). `isOpen` covers the
  // user's toggle AND the error-driven auto-open. The expanded row also
  // carries `mbdb-details`, so the LESS can tint it lighter than the leading
  // row (2026-10-04, lead's request: a two-tone pair stays readable when every
  // pair is open).
  const openClass = isOpen ? "mbdb-row-open" : undefined;

  const setCell = (column, cellValue) =>
    onRowChange({ ...row, [column.field]: cellValue });

  return (
    <>
      <Table.Row className={openClass}>
        {showIndex && <Table.Cell collapsing>{index + 1}</Table.Cell>}
        {columns.map((column) => (
          <Table.Cell key={column.field}>
            {column.render ? (
              column.render(row, index)
            ) : (
              <DataCell
                fieldPath={fieldPath}
                itemPath={itemPath}
                column={column}
                row={row}
                onChange={(next) => setCell(column, next)}
              />
            )}
          </Table.Cell>
        ))}
        {renderExpanded && (
          <Table.Cell collapsing>
            <Button
              basic
              size="mini"
              type="button"
              aria-expanded={isOpen}
              onClick={() => onToggleExpand(isOpen)}
            >
              {`${expandToggle?.(row) ?? "Details"} ${isOpen ? "▾" : "▸"}`}
            </Button>
          </Table.Cell>
        )}
        <Table.Cell collapsing textAlign="right">
          <ErrorMessages messages={rowMessages} />{" "}
          {hint && (
            <Label basic color="yellow" size="mini">
              {hint}
            </Label>
          )}{" "}
          {onRemove && (
            <Button
              basic
              icon
              size="mini"
              type="button"
              aria-label={`Remove row ${index + 1}`}
              onClick={onRemove}
            >
              <Icon name="close" />
            </Button>
          )}
        </Table.Cell>
      </Table.Row>
      {renderExpanded && isOpen && (
        <Table.Row className={`mbdb-details ${openClass}`}>
          <Table.Cell colSpan={colSpan}>
            {renderExpanded(itemPath, index)}
          </Table.Cell>
        </Table.Row>
      )}
    </>
  );
};
Row.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  itemPath: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  storedItem: PropTypes.any,
  columns: PropTypes.arrayOf(PropTypes.object).isRequired,
  deserialize: PropTypes.func.isRequired,
  expanded: PropTypes.bool,
  onToggleExpand: PropTypes.func.isRequired,
  onRowChange: PropTypes.func.isRequired,
  onRemove: PropTypes.func,
  renderExpanded: PropTypes.func,
  expandToggle: PropTypes.func,
  rowHint: PropTypes.func,
  showIndex: PropTypes.bool,
  colSpan: PropTypes.number.isRequired,
};

const TableArrayFieldInner = ({
  fieldPath,
  arrayHelpers,
  columns,
  minItems,
  addButtonLabel,
  addButtonAriaLabel,
  defaultNewValue,
  serialize,
  deserialize,
  renderExpanded,
  expandToggle,
  rowHint,
  showIndex,
}) => {
  const { values, setFieldValue } = useFormikContext();
  const unset = useUnsetField();
  const items = getIn(values, fieldPath) ?? [];
  // minItems rows are VIRTUAL — rendered from defaultNewValue but not
  // written to Formik until the user edits one (the old push-on-render
  // seeded [{}], marked the form dirty and never re-ran after a save)
  const rowCount = Math.max(items.length, minItems);
  // Items have no stable identity (steps, stored strings), so client-only
  // keys live in a ref parallel to the rows: grown on render (covers initial
  // values and virtual rows), spliced on remove, pushed on add. Nothing is
  // written into the values, so it works for string arrays too.
  // CEILING: render-phase ref growth breaks StrictMode assumptions (double
  // render mints unused keys) and a value replaced outside this block's
  // handlers (form reinit) invents fresh keys without remounting rows —
  // contained today because keys only matter within one mount. PoC only.
  // NOTE: the shared useArrayRows hook owns this bookkeeping for
  // ModalArrayField. It is NOT used here on purpose: the table's keys must
  // serve VIRTUAL minItems rows (rowCount > items.length), and the hook's
  // shrink-to-items truncation would drop those virtual-row keys.
  const keysRef = useRef([]);
  while (keysRef.current.length < rowCount) keysRef.current.push(randomUUID());
  // Only the user's explicit toggles are state; errors decide the rest
  const [toggles, setToggles] = useState({});
  // A string/{message} error AT the list itself (e.g.
  // `steps: "Missing data for required field."`) shows under the table
  const listMessages = useOwnErrorMessages(fieldPath);

  const setRow = (index, newRowObject) => {
    if (index <= items.length) {
      // a real row, or the virtual row right after the last real one:
      // writing the path creates the array entry in place (formik setIn)
      setFieldValue(`${fieldPath}.${index}`, serialize(newRowObject));
    } else {
      // a virtual row past the end (minItems >= 2, edited before earlier
      // virtual rows): materialize the whole array, filling the gap with
      // defaultNewValue (the stored shape — "" for a serialize table)
      const next = items.slice();
      for (let i = next.length; i < index; i++) next.push(defaultNewValue);
      next[index] = serialize(newRowObject);
      setFieldValue(fieldPath, next);
    }
  };

  const removeRow = (index) => {
    keysRef.current.splice(index, 1);
    // formik's remove leaves [] behind when the array empties; guide §7
    // wants the key gone entirely (many arrays have minItems: 1). unset
    // also drops parents that become empty (modifications: {} must not stay)
    if (items.length <= 1) unset(fieldPath);
    else arrayHelpers.remove(index);
  };

  // defaultNewValue IS the stored shape (a string table passes "");
  // push it unchanged — deserialize() maps it to the row shape at render
  const addRow = () => {
    arrayHelpers.push(defaultNewValue);
    keysRef.current.push(randomUUID());
  };

  const toggleExpand = (key, current) =>
    setToggles((prev) => ({ ...prev, [key]: !current }));

  // `#` (unless showIndex is false) + one cell per column + expand + actions
  const colSpan =
    (showIndex ? 1 : 0) + 1 + columns.length + (renderExpanded ? 1 : 0);

  return (
    <>
      <Table compact celled>
        <HeaderRow
          fieldPath={fieldPath}
          columns={columns}
          renderExpanded={renderExpanded}
          showIndex={showIndex}
        />
        <Table.Body>
          {Array.from({ length: rowCount }, (_, index) => {
            const key = keysRef.current[index];
            return (
              <Row
                key={key}
                fieldPath={fieldPath}
                itemPath={`${fieldPath}.${index}`}
                index={index}
                storedItem={
                  index < items.length ? items[index] : defaultNewValue
                }
                columns={columns}
                deserialize={deserialize}
                expanded={toggles[key]}
                onToggleExpand={(current) => toggleExpand(key, current)}
                onRowChange={(newRow) => setRow(index, newRow)}
                onRemove={
                  index >= minItems ? () => removeRow(index) : undefined
                }
                renderExpanded={renderExpanded}
                expandToggle={expandToggle}
                rowHint={rowHint}
                showIndex={showIndex}
                colSpan={colSpan}
              />
            );
          })}
        </Table.Body>
      </Table>
      <ErrorMessages messages={listMessages} />
      <Button
        type="button"
        icon
        labelPosition="left"
        size="small"
        // optional: distinguishes two tables with the same button text for a
        // screen reader (e.g. the two Modifications tables)
        aria-label={addButtonAriaLabel}
        onClick={addRow}
      >
        <Icon name="add" />
        {addButtonLabel}
      </Button>
    </>
  );
};
TableArrayFieldInner.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  arrayHelpers: PropTypes.object.isRequired,
  columns: PropTypes.arrayOf(PropTypes.object).isRequired,
  minItems: PropTypes.number.isRequired,
  addButtonLabel: PropTypes.string.isRequired,
  addButtonAriaLabel: PropTypes.string,
  defaultNewValue: PropTypes.any,
  serialize: PropTypes.func.isRequired,
  deserialize: PropTypes.func.isRequired,
  renderExpanded: PropTypes.func,
  expandToggle: PropTypes.func,
  rowHint: PropTypes.func,
  // false hides the leading `#` column (default true)
  showIndex: PropTypes.bool,
};

export const TableArrayField = ({
  fieldPath,
  label,
  help,
  required,
  minItems = 0,
  addButtonLabel = "Add",
  addButtonAriaLabel,
  columns,
  defaultNewValue = {},
  serialize = identity,
  deserialize = identity,
  renderExpanded,
  expandToggle,
  rowHint,
  showIndex = true,
}) => (
  <FieldArray
    name={fieldPath}
    render={(arrayHelpers) => (
      <FieldBox
        fieldPath={fieldPath}
        label={label}
        help={help}
        required={required}
      >
        <TableArrayFieldInner
          fieldPath={fieldPath}
          arrayHelpers={arrayHelpers}
          columns={columns}
          minItems={minItems}
          addButtonLabel={addButtonLabel}
          addButtonAriaLabel={addButtonAriaLabel}
          defaultNewValue={defaultNewValue}
          serialize={serialize}
          deserialize={deserialize}
          renderExpanded={renderExpanded}
          expandToggle={expandToggle}
          rowHint={rowHint}
          showIndex={showIndex}
        />
      </FieldBox>
    )}
  />
);

// Form.Field wrapper with the model's label/help (explicit props win) and an
// error header when anything under fieldPath has an error.
const FieldBox = ({ fieldPath, label, help, required, children }) => {
  const { hasError } = useFieldErrors(fieldPath);
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // NO error prop on Form.Field: .field.error would colour EVERY input of the
  // table red (cells mark themselves). The header label carries the state.
  return (
    <Form.Field required={data.required}>
      {data.label && (
        // htmlFor points at the field path for OARepo error scrolling; the
        // table rows below are the labelled controls (cell aria-labels).
        <label
          htmlFor={fieldPath}
          className={hasError ? "mbdb-error-text" : undefined}
        >
          <HelpLabel label={data.label} help={data.helpText} />
        </label>
      )}
      {data.helpText && <FieldHelp help={data.helpText} placement="label" />}
      {children}
    </Form.Field>
  );
};
FieldBox.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  required: PropTypes.bool,
  children: PropTypes.node.isRequired,
};

TableArrayField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  required: PropTypes.bool,
  minItems: PropTypes.number,
  addButtonLabel: PropTypes.string,
  addButtonAriaLabel: PropTypes.string,
  columns: PropTypes.arrayOf(
    PropTypes.shape({
      field: PropTypes.string.isRequired,
      // defaults to the model label of `<fieldPath>.<field>`
      label: PropTypes.string,
      required: PropTypes.bool,
      width: PropTypes.number,
      type: PropTypes.oneOf(["text", "textarea", "number", "select"]),
      options: PropTypes.array,
      allowAdditions: PropTypes.bool,
      render: PropTypes.func,
    })
  ).isRequired,
  defaultNewValue: PropTypes.any,
  serialize: PropTypes.func,
  deserialize: PropTypes.func,
  renderExpanded: PropTypes.func,
  expandToggle: PropTypes.func,
  rowHint: PropTypes.func,
  // false hides the leading `#` column (default true); a plain list is never
  // referred to by number (e.g. StringTableField)
  showIndex: PropTypes.bool,
};
