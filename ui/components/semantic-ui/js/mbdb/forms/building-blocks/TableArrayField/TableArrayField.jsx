import React, { useRef, useState } from "react";
import PropTypes from "prop-types";
import { FieldArray, getIn, useFormikContext } from "formik";
import {
  Button,
  FieldHelp,
  Form,
  Icon,
  Input,
  Label,
  Table,
} from "mbdb-semantic-ui-react";
import { countErrors, errorMessages } from "../errors";
import { useModelFieldData } from "../fieldData";

const identity = (x) => x;

// Label-less cell input; the column header is its label (aria-label).
const Cell = ({ column, row, onChange, error }) => {
  const value = row?.[column.field];
  const common = {
    "aria-label": column.label,
    error: error !== undefined,
    value: value ?? "",
    onChange: (e, { value: next }) => onChange(next),
  };
  if (column.type === "textarea")
    return <Form.TextArea autoHeight rows={1} {...common} />;
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
  if (column.type === "select")
    return (
      <Form.Dropdown
        search
        selection
        clearable
        selectOnBlur={false}
        allowAdditions={column.allowAdditions}
        options={(column.options ?? []).map((opt) =>
          typeof opt === "string"
            ? { key: opt, value: opt, text: opt }
            : { key: opt.value, value: opt.value, text: opt.label ?? opt.value }
        )}
        aria-label={column.label}
        error={error !== undefined}
        value={value ?? ""}
        onChange={(e, { value: next }) =>
          onChange(next === "" ? undefined : next)
        }
      />
    );
  return <Input {...common} />;
};
Cell.propTypes = {
  column: PropTypes.object.isRequired,
  row: PropTypes.any,
  onChange: PropTypes.func.isRequired,
  error: PropTypes.string,
};

// minItems rows are seeded once inside the FieldArray render (guide §8: no
// useEffect writing values); the ref guard makes it a one-time action.
const TableArrayFieldInner = ({
  fieldPath,
  arrayHelpers,
  columns,
  minItems,
  addButtonLabel,
  defaultNewValue,
  serialize,
  deserialize,
  renderExpanded,
  expandToggle,
  rowHint,
}) => {
  const { values, errors, setFieldValue, initialValues } = useFormikContext();
  // ponytail: minItems rows are pushed inside render (task-specified pattern);
  // React 16 logs a dev-only setState-in-render warning on first mount, but
  // the push is otherwise deferred and applied before paint.
  const initializedRef = useRef(false);
  const items = getIn(values, fieldPath) ?? [];

  if (!initializedRef.current) {
    initializedRef.current = true;
    const missing = minItems - items.length;
    if (missing > 0) {
      // push once (Formik applies each push on top of the previous)
      for (let i = 0; i < missing; i++)
        arrayHelpers.push(deserialize(defaultNewValue));
    }
  }

  // one-time: rows with errors start expanded (computed from initial values)
  const [expanded, setExpanded] = useState(() => {
    const initialItems = getIn(initialValues, fieldPath) ?? [];
    const open = new Set();
    initialItems.forEach((_, i) => {
      if (renderExpanded && countErrors(errors, `${fieldPath}.${i}`) > 0)
        open.add(i);
    });
    return open;
  });

  const rows = items.map(deserialize);

  const setCell = (index, column, cellValue) => {
    const next = { ...rows[index], [column.field]: cellValue };
    setFieldValue(`${fieldPath}.${index}`, serialize(next));
  };

  const toggleExpand = (index) =>
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(index)) next.delete(index);
      else next.add(index);
      return next;
    });

  const colSpan = 2 + columns.length + (renderExpanded ? 1 : 0); // # + … + expand + actions

  return (
    <>
      <Table compact celled>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>#</Table.HeaderCell>
            {columns.map((column) => (
              <Table.HeaderCell key={column.field} width={column.width}>
                {column.label}
                {column.required ? " *" : ""}
              </Table.HeaderCell>
            ))}
            {renderExpanded && <Table.HeaderCell />}
            <Table.HeaderCell />
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {rows.map((row, index) => {
            const itemPath = `${fieldPath}.${index}`;
            const isOpen = expanded.has(index);
            const hint = rowHint?.(row);
            // ponytail: plain FieldArray gives no __key, so the row key may
            // fall back to the index; reordering costs a re-render at worst
            return (
              <React.Fragment
                key={items[index]?.__key ?? items[index]?.id ?? index}
              >
                <Table.Row>
                  <Table.Cell collapsing>{index + 1}</Table.Cell>
                  {columns.map((column) => {
                    const cellError = errorMessages(
                      errors,
                      `${itemPath}.${column.field}`
                    ).join(" ");
                    return (
                      <Table.Cell key={column.field}>
                        {column.render ? (
                          column.render(row, index)
                        ) : (
                          <>
                            <Cell
                              column={column}
                              row={row}
                              error={cellError || undefined}
                              onChange={(next) => setCell(index, column, next)}
                            />
                            {cellError !== "" && (
                              <Label basic color="red" pointing>
                                {cellError}
                              </Label>
                            )}
                          </>
                        )}
                      </Table.Cell>
                    );
                  })}
                  {renderExpanded && (
                    <Table.Cell collapsing>
                      <Button
                        basic
                        size="mini"
                        type="button"
                        aria-expanded={isOpen}
                        onClick={() => toggleExpand(index)}
                      >
                        {`${expandToggle?.(row) ?? "Details"} ${
                          isOpen ? "▾" : "▸"
                        }`}
                      </Button>
                    </Table.Cell>
                  )}
                  <Table.Cell collapsing textAlign="right">
                    {hint && (
                      <Label basic color="yellow" size="mini">
                        {hint}
                      </Label>
                    )}{" "}
                    {index >= minItems && (
                      <Button
                        basic
                        icon
                        size="mini"
                        type="button"
                        aria-label={`Remove row ${index + 1}`}
                        onClick={() => arrayHelpers.remove(index)}
                      >
                        <Icon name="close" />
                      </Button>
                    )}
                  </Table.Cell>
                </Table.Row>
                {renderExpanded && isOpen && (
                  <Table.Row>
                    <Table.Cell colSpan={colSpan}>
                      {renderExpanded(itemPath, index)}
                    </Table.Cell>
                  </Table.Row>
                )}
              </React.Fragment>
            );
          })}
        </Table.Body>
      </Table>
      <Button
        type="button"
        icon
        labelPosition="left"
        size="small"
        onClick={() => arrayHelpers.push(deserialize(defaultNewValue))}
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
  columns: PropTypes.array.isRequired,
  minItems: PropTypes.number.isRequired,
  addButtonLabel: PropTypes.string.isRequired,
  defaultNewValue: PropTypes.any,
  serialize: PropTypes.func.isRequired,
  deserialize: PropTypes.func.isRequired,
  renderExpanded: PropTypes.func,
  expandToggle: PropTypes.func,
  rowHint: PropTypes.func,
};

export const TableArrayField = ({
  fieldPath,
  label,
  help,
  required,
  minItems = 0,
  addButtonLabel = "Add",
  columns,
  defaultNewValue = {},
  serialize = identity,
  deserialize = identity,
  renderExpanded,
  expandToggle,
  rowHint,
}) => (
  <FieldArray
    name={fieldPath}
    render={(arrayHelpers) => (
      <Header
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
          defaultNewValue={defaultNewValue}
          serialize={serialize}
          deserialize={deserialize}
          renderExpanded={renderExpanded}
          expandToggle={expandToggle}
          rowHint={rowHint}
        />
      </Header>
    )}
  />
);

// Form.Field wrapper with the model's label/help (explicit props win) and an
// error header when anything under fieldPath has an error.
const Header = ({ fieldPath, label, help, required, children }) => {
  const { errors } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  return (
    <Form.Field
      required={data.required}
      error={countErrors(errors, fieldPath) > 0}
    >
      {data.label && <label>{data.label}</label>}
      {children}
      {data.helpText && <FieldHelp help={data.helpText} />}
    </Form.Field>
  );
};
Header.propTypes = {
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
  columns: PropTypes.arrayOf(
    PropTypes.shape({
      field: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
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
};
