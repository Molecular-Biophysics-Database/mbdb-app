/* Read-only view: rows are rendered positionally and never reordered. */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button, Label, Table } from "mbdb-semantic-ui-react";
import { useFieldData } from "@js/oarepo_ui/forms";
import { errorMessages, hasData, hasError, isEmptyValue } from "../errors";
import { formatters } from "./formatters";

// ponytail: no model label in a test ui_model reads `children.…` — use the leaf
const readable = (label, fallback) =>
  label && !label.includes("children") ? label : fallback;

// getFieldData uses hooks, so one tiny component per label (rows are few).
const DetailLabel = ({ path, fallback }) => {
  const { getFieldData } = useFieldData();
  const { label } = getFieldData({
    fieldPath: path,
    fieldRepresentation: "text",
  });
  return <>{readable(label, fallback)}</>;
};
DetailLabel.propTypes = {
  path: PropTypes.string.isRequired,
  fallback: PropTypes.string.isRequired,
};

const isValueUnit = (v) =>
  v !== null &&
  typeof v === "object" &&
  !Array.isArray(v) &&
  "value" in v &&
  "unit" in v;

const isVocabulary = (v) =>
  v !== null &&
  typeof v === "object" &&
  !Array.isArray(v) &&
  typeof v.id === "string";

// Plain-text formatting of one value, used by cells and nested rows.
const textOf = (value, vocabulary) => {
  if (isEmptyValue(value)) return "";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (typeof value === "string" || typeof value === "number")
    return String(value);
  if (Array.isArray(value))
    return value.every(
      (v) => !isVocabulary(v) && (typeof v !== "object" || v === null)
    )
      ? value.map((v) => String(v)).join(", ")
      : "";
  if (isValueUnit(value))
    return [value.value, value.unit].filter((x) => !isEmptyValue(x)).join(" ");
  if (isVocabulary(value)) return vocabulary(value.id) || value.id;
  return "";
};

const vocabularyLookup = (titles, name) => (id) =>
  titles?.[id] ?? titles?.[name]?.[id] ?? null;

// One formatted value; uses the suffix formatter when one is registered.
const Value = ({ name, value, titles }) => {
  const formatter = formatters[name]; // registry is keyed by path suffix
  if (formatter && !isEmptyValue(value)) return formatter(value);
  if (
    value !== null &&
    typeof value === "object" &&
    !Array.isArray(value) &&
    !("id" in value) &&
    !isValueUnit(value) &&
    typeof value.title === "string"
  )
    // manual chemical entry: title plus a grey hint (design §3)
    return (
      <span>
        {textOf(value.title, vocabularyLookup(titles, name))}{" "}
        <Label basic size="mini" content="Manual entry" />
      </span>
    );
  return <>{textOf(value, vocabularyLookup(titles, name))}</>;
};
Value.propTypes = {
  name: PropTypes.string.isRequired,
  value: PropTypes.any,
  titles: PropTypes.object,
};

const ErrorNote = ({ path }) => {
  const { errors } = useFormikContext();
  const messages = errorMessages(errors, path);
  if (messages.length === 0) return null;
  return <div className="ui red text">{messages.join(" ")}</div>;
};
ErrorNote.propTypes = { path: PropTypes.string.isRequired };

// ---- mini table for arrays of complex objects ------------------------------

const MiniTable = ({ basePath, items, titles }) => {
  const [open, setOpen] = useState(() => new Set());
  const keys = [
    ...new Set(items.flatMap((item) => Object.keys(item ?? {}))),
  ].filter((key) => items.some((item) => hasData(item?.[key])));
  const toggle = (i) =>
    setOpen((prev) => {
      const next = new Set(prev);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      return next;
    });
  return (
    <Table compact="very" size="small">
      <Table.Body>
        {items.map((item, i) => {
          const isOpen = open.has(i);
          return (
            <React.Fragment
              key={
                i
              } /* eslint-disable-line react/no-array-index-key -- read-only */
            >
              <Table.Row>
                <Table.Cell collapsing>
                  <Button
                    basic
                    icon
                    size="mini"
                    type="button"
                    aria-expanded={isOpen}
                    aria-label={`Show details of item ${i + 1}`}
                    onClick={() => toggle(i)}
                  >
                    {isOpen ? "▾" : "▸"}
                  </Button>
                </Table.Cell>
                {keys.map((key) => (
                  <Table.Cell key={key}>
                    {textOf(item?.[key], vocabularyLookup(titles, key))}
                  </Table.Cell>
                ))}
              </Table.Row>
              {isOpen && (
                <Table.Row className="mbdb-details">
                  <Table.Cell colSpan={keys.length + 1}>
                    <SubRows
                      basePath={`${basePath}.${i}`}
                      obj={item}
                      titles={titles}
                    />
                  </Table.Cell>
                </Table.Row>
              )}
            </React.Fragment>
          );
        })}
      </Table.Body>
    </Table>
  );
};
MiniTable.propTypes = {
  basePath: PropTypes.string.isRequired,
  items: PropTypes.array.isRequired,
  titles: PropTypes.object,
};

// ---- flattened row building ------------------------------------------------

const isPlainObject = (v) =>
  v !== null && typeof v === "object" && !Array.isArray(v);

const isLeafObject = (v) => isValueUnit(v) || isVocabulary(v);

// ponytail: one indent level; deeper nesting joins sub-headings with " › "
// errors (optional): rows with a server error are kept even when empty
const collectRows = (
  obj,
  basePath,
  errors = {},
  heading = "",
  indent = false
) => {
  const rows = [];
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    const path = `${basePath}.${name}`;
    if (isEmptyValue(value) && !hasError(errors, path)) return;
    const subHeading = heading ? `${heading} › ${name}` : name;
    if (isLeafObject(value) || !isPlainObject(value)) {
      if (
        Array.isArray(value) &&
        value.some((v) => isPlainObject(v) && !isLeafObject(v))
      ) {
        // array of complex objects: heading + mini table
        rows.push({ kind: "heading", name: subHeading, path, indent });
        rows.push({ kind: "mini", name, path, items: value, indent });
      } else {
        rows.push({ kind: "field", name, path, value, indent });
      }
      return;
    }
    const inner = collectRows(value, path, errors, subHeading, true);
    if (inner.length > 0)
      rows.push({ kind: "heading", name: subHeading, path, indent });
    rows.push(...inner);
  });
  return rows;
};

// Renders the collected rows of one object (used for the expanded mini row).
const SubRows = ({ basePath, obj, titles }) => {
  const { errors } = useFormikContext();
  const rows = collectRows(obj, basePath, errors);
  return (
    <Table definition basic="very" compact>
      <Table.Body>
        {rows.map((row, i) => {
          if (row.kind === "heading")
            return (
              <Table.Row
                key={
                  i
                } /* eslint-disable-line react/no-array-index-key -- read-only */
              >
                <Table.HeaderCell colSpan="2">{row.name}</Table.HeaderCell>
              </Table.Row>
            );
          if (row.kind === "mini")
            return (
              <Table.Row
                key={
                  i
                } /* eslint-disable-line react/no-array-index-key -- read-only */
              >
                <Table.Cell colSpan="2">
                  <MiniTable
                    basePath={row.path}
                    items={row.items}
                    titles={titles}
                  />
                </Table.Cell>
              </Table.Row>
            );
          return (
            <Table.Row
              key={
                i
              } /* eslint-disable-line react/no-array-index-key -- read-only */
            >
              <Table.Cell
                width={5}
                className={row.indent ? "mbdb-details-indent" : undefined}
              >
                <DetailLabel path={row.path} fallback={row.name} />
              </Table.Cell>
              <Table.Cell>
                <Value name={row.name} value={row.value} titles={titles} />
                <ErrorNote path={row.path} />
              </Table.Cell>
            </Table.Row>
          );
        })}
      </Table.Body>
    </Table>
  );
};
SubRows.propTypes = {
  basePath: PropTypes.string.isRequired,
  obj: PropTypes.object.isRequired,
  titles: PropTypes.object,
};

// ---- the top-level block ---------------------------------------------------

const groupSections = (obj, basePath, groups, exclude, required, errors) => {
  const known = new Set(exclude);
  const sections = [];
  groups.forEach((group) => {
    const part = {};
    const missing = [];
    (group.fields ?? []).forEach((name) => {
      known.add(name);
      if (exclude.includes(name)) return;
      // a field with a server error stays visible even when empty (design §5)
      if (hasData(obj?.[name]) || hasError(errors, `${basePath}.${name}`))
        part[name] = obj?.[name];
      else if (required.has(name))
        missing.push({ name, path: `${basePath}.${name}` });
    });
    const rows = collectRows(part, basePath, errors);
    if (rows.length === 0 && missing.length === 0) return; // all-empty group
    sections.push({ title: group.title, rows, missing });
  });
  // keys in no group are never hidden: they go under "Other"
  const other = {};
  Object.entries(obj ?? {}).forEach(([name, value]) => {
    if (
      !known.has(name) &&
      (hasData(value) || hasError(errors, `${basePath}.${name}`))
    )
      other[name] = value;
  });
  const otherRows = collectRows(other, basePath, errors);
  if (otherRows.length > 0)
    sections.push({ title: "Other", rows: otherRows, missing: [] });
  return sections;
};

export const DetailView = ({
  fieldPath,
  groups = [],
  exclude = [],
  requiredPaths = [],
  vocabularyTitles = {},
}) => {
  const { values, errors } = useFormikContext();
  const obj = getIn(values, fieldPath);
  if (obj === undefined || obj === null) return null;
  const sections = groupSections(
    isPlainObject(obj) ? obj : {},
    fieldPath,
    groups,
    exclude,
    new Set(requiredPaths),
    errors
  );
  if (sections.length === 0)
    return <span className="ui grey text">Nothing filled in yet</span>;
  return (
    <Table definition basic="very" compact>
      <Table.Body>
        {sections.map((section, si) => (
          <React.Fragment key={si}>
            <Table.Row>
              <Table.HeaderCell colSpan="2">{section.title}</Table.HeaderCell>
            </Table.Row>
            {section.rows.map((row, i) => {
              if (row.kind === "heading")
                return (
                  <Table.Row key={`h${i}`}>
                    <Table.HeaderCell colSpan="2">{row.name}</Table.HeaderCell>
                  </Table.Row>
                );
              if (row.kind === "mini")
                return (
                  <Table.Row key={`m${i}`}>
                    <Table.Cell
                      colSpan="2"
                      className={row.indent ? "mbdb-details-indent" : undefined}
                    >
                      <MiniTable
                        basePath={row.path}
                        items={row.items}
                        titles={vocabularyTitles}
                      />
                    </Table.Cell>
                  </Table.Row>
                );
              return (
                <Table.Row key={`f${i}`}>
                  <Table.Cell
                    width={5}
                    className={row.indent ? "mbdb-details-indent" : undefined}
                  >
                    <DetailLabel path={row.path} fallback={row.name} />
                  </Table.Cell>
                  <Table.Cell>
                    <Value
                      name={row.name}
                      value={row.value}
                      titles={vocabularyTitles}
                    />
                    <ErrorNote path={row.path} />
                  </Table.Cell>
                </Table.Row>
              );
            })}
            {section.missing.map((m) => (
              <Table.Row key={`miss-${m.name}`}>
                <Table.Cell width={5}>
                  <DetailLabel path={m.path} fallback={m.name} />
                </Table.Cell>
                <Table.Cell>
                  <Label color="red" size="small">
                    Missing
                  </Label>
                </Table.Cell>
              </Table.Row>
            ))}
          </React.Fragment>
        ))}
      </Table.Body>
    </Table>
  );
};

DetailView.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  groups: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      fields: PropTypes.arrayOf(PropTypes.string).isRequired,
    })
  ),
  exclude: PropTypes.arrayOf(PropTypes.string),
  requiredPaths: PropTypes.arrayOf(PropTypes.string),
  vocabularyTitles: PropTypes.object,
};
