import React, { useState } from "react";
import PropTypes from "prop-types";
import { Button, Dropdown, Form, Message } from "semantic-ui-react";
import { OPERATORS, buildQuery, defaultOperator } from "./query";

const JOINS = ["AND", "OR", "AND NOT"].map((join) => ({ value: join, text: join }));
const FIRST_JOINS = [
  { value: "AND", text: "Where" },
  { value: "AND NOT", text: "NOT" },
];

let nextKey = 0;
const newRow = () => ({
  key: nextKey++,
  join: "AND",
  open: false,
  close: false,
  path: "",
  operator: "",
  value: "",
  value2: "",
});

const ValueInput = ({ field, label, value, onChange }) => {
  if (field?.kind === "enum") {
    return (
      <Form.Field className="mbdb-advanced-value">
        <Dropdown
          fluid
          selection
          search
          selectOnBlur={false}
          aria-label={label}
          placeholder="Value"
          options={field.options.map((option) => ({ value: option, text: option }))}
          value={value}
          onChange={(_, data) => onChange(data.value)}
        />
      </Form.Field>
    );
  }
  return (
    <Form.Input
      className="mbdb-advanced-value"
      aria-label={label}
      placeholder="Value"
      type={["number", "date"].includes(field?.kind) ? field.kind : "text"}
      step={field?.kind === "number" ? "any" : undefined}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
};

ValueInput.propTypes = {
  field: PropTypes.object,
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
};

ValueInput.defaultProps = {
  field: undefined,
};

export const AdvancedSearch = ({ fields, targets }) => {
  const [rows, setRows] = useState(() => [newRow()]);
  const [target, setTarget] = useState(targets[0].value);
  const [error, setError] = useState("");

  const update = (key, change) => {
    setError("");
    setRows((previous) =>
      previous.map((row) => (row.key === key ? { ...row, ...change } : row))
    );
  };

  const selectField = (key, path) => {
    const { kind } = fields.find((field) => field.path === path);
    update(key, { path, operator: defaultOperator(kind), value: "", value2: "" });
  };

  const submit = () => {
    try {
      const query = buildQuery(rows, fields);
      window.location.assign(`${target}?${new URLSearchParams({ q: query })}`);
    } catch (e) {
      setError(e.message);
    }
  };

  const fieldOptions = fields.map(({ path, label, group }) => ({
    value: path,
    text: label,
    description: group,
  }));

  return (
    <Form onSubmit={submit} className="mbdb-advanced-search">
      {rows.map((row, index) => {
        const field = fields.find(({ path }) => path === row.path);
        const operators = field ? OPERATORS[field.kind] : {};
        const name = `condition ${index + 1}`;
        return (
          <div className="mbdb-advanced-row" key={row.key} role="group" aria-label={name}>
            <Dropdown
              selection
              compact
              aria-label={`Operator before ${name}`}
              options={index === 0 ? FIRST_JOINS : JOINS}
              value={index === 0 && row.join === "OR" ? "AND" : row.join}
              onChange={(_, { value }) => update(row.key, { join: value })}
            />
            <Button
              type="button"
              basic={!row.open}
              content="("
              aria-label={`Open bracket before ${name}`}
              aria-pressed={row.open}
              onClick={() => update(row.key, { open: !row.open })}
            />
            <Dropdown
              className="mbdb-advanced-field"
              selection
              search
              selectOnBlur={false}
              aria-label={`Field of ${name}`}
              placeholder="Field"
              options={fieldOptions}
              value={row.path}
              onChange={(_, { value }) => selectField(row.key, value)}
            />
            <Dropdown
              selection
              compact
              aria-label={`Comparison of ${name}`}
              disabled={!field}
              options={Object.entries(operators).map(([value, { text }]) => ({
                value,
                text,
              }))}
              value={row.operator}
              onChange={(_, { value }) => update(row.key, { operator: value })}
            />
            <ValueInput
              field={field}
              label={`Value of ${name}`}
              value={row.value}
              onChange={(value) => update(row.key, { value })}
            />
            {row.operator === "between" && (
              <ValueInput
                field={field}
                label={`Upper value of ${name}`}
                value={row.value2}
                onChange={(value2) => update(row.key, { value2 })}
              />
            )}
            <Button
              type="button"
              basic={!row.close}
              content=")"
              aria-label={`Close bracket after ${name}`}
              aria-pressed={row.close}
              onClick={() => update(row.key, { close: !row.close })}
            />
            <Button
              type="button"
              basic
              icon="trash"
              aria-label={`Remove ${name}`}
              disabled={rows.length === 1}
              onClick={() => {
                setError("");
                setRows(rows.filter(({ key }) => key !== row.key));
              }}
            />
          </div>
        );
      })}
      {error && <Message negative role="alert" content={error} />}
      <div className="mbdb-advanced-row">
        <Button
          type="button"
          icon="plus"
          labelPosition="left"
          content="Add condition"
          onClick={() => setRows([...rows, newRow()])}
        />
        <Dropdown
          selection
          aria-label="Search in"
          options={targets}
          value={target}
          onChange={(_, { value }) => setTarget(value)}
        />
        <Button type="submit" primary icon="search" labelPosition="left" content="Search" />
      </div>
    </Form>
  );
};

AdvancedSearch.propTypes = {
  fields: PropTypes.array.isRequired,
  targets: PropTypes.array.isRequired,
};
