/* Rows in the read-only details are positional and never reorder, so the
   index is a legitimate key (carries meaning, not identity). See collect.js. */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import { Button, Label, Table } from "mbdb-semantic-ui-react";
import {
  hasData,
  isEmptyValue,
  useFieldErrors,
} from "@js/mbdb/forms/building-blocks/errors";
// formatters by leaf name (sequence, location, …): mini cells use them too,
// so a mini table never dumps a full sequence into a cell
import { ErrorNote, Value, textOf } from "./values";
import { formatters } from "./formatters";
import { DetailLabel } from "./DetailLabel";
import { collectRows, useSections } from "./collect";

// The shared renderer for the collected rows — used for the top-level table
// and inside an expanded mini row. Details are read-only and never reordered,
// so the positional key carries meaning (not identity).

// A nested sub-heading: every level resolves its own model label, joined
// with " › " (design §2, §4). The last N path segments of row.path match the
// N joined names, so each level gets its path-aware label.
const Heading = ({ row }) => {
  const parts = row.name.split(" › ");
  const pathParts = row.path.split(".");
  const start = pathParts.length - parts.length;
  return (
    <Table.HeaderCell colSpan="2">
      {parts.map((part, i) => (
        <React.Fragment key={i}>
          {i > 0 ? " › " : ""}
          <DetailLabel
            path={pathParts.slice(0, start + i + 1).join(".")}
            fallback={part}
          />
        </React.Fragment>
      ))}
    </Table.HeaderCell>
  );
};
Heading.propTypes = {
  row: PropTypes.object.isRequired,
};

// One group of the form becomes a section: a header row plus its rows and the
// red "Missing" rows for required-but-absent fields (design §5). Used by the
// top-level DetailView and by a mini row's own ▸ (the item's groups).
export const Section = ({ fieldPath, section, onEdit }) => (
  <>
    <Table.Row>
      <Table.HeaderCell colSpan="2">{section.title}</Table.HeaderCell>
    </Table.Row>
    <Rows rows={section.rows} onEdit={onEdit} />
    {section.missing.map((name) => (
      <Table.Row key={`miss-${name}`}>
        <Table.Cell width={5}>
          <DetailLabel path={`${fieldPath}.${name}`} fallback={name} />
        </Table.Cell>
        <Table.Cell>
          <Label color="red" size="small">
            Missing
          </Label>
        </Table.Cell>
      </Table.Row>
    ))}
  </>
);
Section.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  section: PropTypes.object.isRequired,
  onEdit: PropTypes.func,
};

// One field row; kept visible even when empty while it has a server error
// (design §5). The error comes through useFieldErrors so it survives edits.
const FieldRow = ({ row, onEdit }) => {
  const { hasError } = useFieldErrors(row.path);
  if (isEmptyValue(row.value) && !hasError) return null;
  return (
    <>
      <Table.Cell
        width={5}
        className={row.indent ? "mbdb-details-indent" : undefined}
      >
        <DetailLabel path={row.path} fallback={row.name} />
      </Table.Cell>
      <Table.Cell>
        <Value name={row.name} value={row.value} vocabulary={row.vocabulary} />
        <ErrorNote path={row.path} onEdit={onEdit} />
      </Table.Cell>
    </>
  );
};
FieldRow.propTypes = {
  row: PropTypes.object.isRequired,
  onEdit: PropTypes.func,
};

// The mini row's own ▸: the item's details, grouped exactly like its form (the
// group entry declared the item's groups), so vocabularies resolve and the
// columns already in the mini row are not repeated. Falls back to the flat
// rows when the array declares no groups.
const MiniDetails = ({ fieldPath, groups, exclude }) => {
  const sections = useSections(fieldPath, groups, exclude, []);
  if (!sections || sections.length === 0)
    return <span className="mbdb-muted-text">Nothing filled in yet</span>;
  return (
    <Table definition basic="very" compact>
      <Table.Body>
        {sections.map((section, si) => (
          <Section key={si} fieldPath={fieldPath} section={section} />
        ))}
      </Table.Body>
    </Table>
  );
};
MiniDetails.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  groups: PropTypes.array.isRequired,
  exclude: PropTypes.arrayOf(PropTypes.string).isRequired,
};

// A mini-table row with its own ▸; expansion renders the item's details inline.
// Columns are the array's declared `itemColumns` (the array's edit-table
// columns) when given, else the union of keys (`keys`).
const MiniRow = ({ basePath, index, item, keys, itemColumns, itemGroups }) => {
  const [open, setOpen] = useState(false);
  const groups =
    typeof itemGroups === "function" ? itemGroups(item) : itemGroups;
  // the fields already shown as columns are not repeated in the details
  const exclude = itemColumns
    ? itemColumns.filter((column) => column.field).map((column) => column.field)
    : [];
  const cellCount = (itemColumns ?? keys).length + 1;
  return (
    <>
      <Table.Row>
        <Table.Cell collapsing>
          <Button
            basic
            icon
            size="mini"
            type="button"
            aria-expanded={open}
            aria-label={`${open ? "Hide" : "Show"} details of item ${
              index + 1
            }`}
            onClick={() => setOpen((prev) => !prev)}
          >
            {open ? "▾" : "▸"}
          </Button>
        </Table.Cell>
        {itemColumns
          ? itemColumns.map((column) => (
              <Table.Cell key={column.label}>{column.value(item)}</Table.Cell>
            ))
          : keys.map((key) => (
              <Table.Cell key={key}>
                {formatters[key] && !isEmptyValue(item?.[key])
                  ? formatters[key](item?.[key])
                  : textOf(item?.[key])}
              </Table.Cell>
            ))}
      </Table.Row>
      {open && (
        <Table.Row className="mbdb-details">
          <Table.Cell colSpan={cellCount}>
            {groups?.length ? (
              <MiniDetails
                fieldPath={basePath}
                groups={groups}
                exclude={exclude}
              />
            ) : (
              <Rows rows={collectRows(item, basePath)} />
            )}
          </Table.Cell>
        </Table.Row>
      )}
    </>
  );
};
MiniRow.propTypes = {
  basePath: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  item: PropTypes.object.isRequired,
  keys: PropTypes.array.isRequired,
  itemColumns: PropTypes.array,
  itemGroups: PropTypes.oneOfType([PropTypes.array, PropTypes.func]),
};

// A mini summary table for an array of complex objects (design §4). Columns are
// the array's declared `itemColumns` (the same columns as its edit table) when
// given, else the union of keys with data in first-seen order, with header
// labels from the model (F4e). Read-only; the positional key is meaning.
const MiniTable = ({ basePath, items, itemColumns, itemGroups }) => {
  const keys = itemColumns
    ? itemColumns.map((column) => column.label)
    : [...new Set(items.flatMap((item) => Object.keys(item ?? {})))].filter(
        (key) => items.some((item) => hasData(item?.[key]))
      );
  return (
    <Table compact="very" size="small">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell />
          {keys.map((key) => (
            <Table.HeaderCell key={key}>
              {itemColumns ? (
                key
              ) : (
                <DetailLabel path={`${basePath}.0.${key}`} fallback={key} />
              )}
            </Table.HeaderCell>
          ))}
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {items.map((item, i) => (
          <MiniRow
            key={i}
            basePath={`${basePath}.${i}`}
            index={i}
            item={item}
            keys={keys}
            itemColumns={itemColumns}
            itemGroups={itemGroups}
          />
        ))}
      </Table.Body>
    </Table>
  );
};
MiniTable.propTypes = {
  basePath: PropTypes.string.isRequired,
  items: PropTypes.array.isRequired,
  itemColumns: PropTypes.array,
  itemGroups: PropTypes.oneOfType([PropTypes.array, PropTypes.func]),
};

// Rows of one object. Wrap each row in <Table.Row key={i}>.
export const Rows = ({ rows, onEdit }) => (
  <>
    {rows.map((row, i) => {
      if (row.kind === "heading")
        return (
          <Table.Row key={i}>
            <Heading row={row} />
          </Table.Row>
        );
      if (row.kind === "mini")
        return (
          <Table.Row key={i}>
            <Table.Cell
              colSpan="2"
              className={row.indent ? "mbdb-details-indent" : undefined}
            >
              <MiniTable
                basePath={row.path}
                items={row.items}
                itemColumns={row.itemColumns}
                itemGroups={row.itemGroups}
              />
            </Table.Cell>
          </Table.Row>
        );
      return (
        <Table.Row key={i}>
          <FieldRow row={row} onEdit={onEdit} />
        </Table.Row>
      );
    })}
  </>
);
Rows.propTypes = {
  rows: PropTypes.array.isRequired,
  onEdit: PropTypes.func,
};
