/* Rows in the read-only details are positional and never reorder, so the
   index is a legitimate key (carries meaning, not identity). See collect.js. */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import { Button, Table } from "mbdb-semantic-ui-react";
import {
  hasData,
  isEmptyValue,
  useFieldErrors,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorNote, Value, textOf, vocabularyLookup } from "./values";
import { DetailLabel } from "./DetailLabel";
import { collectRows } from "./collect";

// The shared renderer for the collected rows — used for the top-level table
// and inside an expanded mini row. Details are read-only and never reordered,
// so the positional key carries meaning (not identity).

// A nested sub-heading through the model label (design §2); multi-level
// headings ("storage › temperature") keep their raw join.
const Heading = ({ row }) => (
  <Table.HeaderCell colSpan="2">
    {row.name.indexOf(" › ") === -1 ? (
      <DetailLabel path={row.path} fallback={row.name} />
    ) : (
      row.name
    )}
  </Table.HeaderCell>
);
Heading.propTypes = {
  row: PropTypes.object.isRequired,
};

// One field row; kept visible even when empty while it has a server error
// (design §5). The error comes through useFieldErrors so it survives edits (F1).
const FieldRow = ({ row, titles, onEdit }) => {
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
        <Value name={row.name} value={row.value} titles={titles} />
        <ErrorNote path={row.path} onEdit={onEdit} />
      </Table.Cell>
    </>
  );
};
FieldRow.propTypes = {
  row: PropTypes.object.isRequired,
  titles: PropTypes.object,
  onEdit: PropTypes.func,
};

// A mini-table row with its own ▸; expansion renders the item's rows inline.
const MiniRow = ({ basePath, index, item, keys, titles }) => {
  const [open, setOpen] = useState(false);
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
        {keys.map((key) => (
          <Table.Cell key={key}>
            {textOf(item?.[key], vocabularyLookup(titles, key))}
          </Table.Cell>
        ))}
      </Table.Row>
      {open && (
        <Table.Row className="mbdb-details">
          <Table.Cell colSpan={keys.length + 1}>
            <Rows rows={collectRows(item, basePath)} titles={titles} />
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
  titles: PropTypes.object,
};

// A mini summary table for an array of complex objects (design §4). Columns
// are the union of keys with data in first-seen order, with a header row whose
// labels come from the model (F4e). Read-only; the positional key is meaning.
const MiniTable = ({ basePath, items, titles }) => {
  const keys = [
    ...new Set(items.flatMap((item) => Object.keys(item ?? {}))),
  ].filter((key) => items.some((item) => hasData(item?.[key])));
  return (
    <Table compact="very" size="small">
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell />
          {keys.map((key) => (
            <Table.HeaderCell key={key}>
              <DetailLabel path={`${basePath}.0.${key}`} fallback={key} />
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
            titles={titles}
          />
        ))}
      </Table.Body>
    </Table>
  );
};
MiniTable.propTypes = {
  basePath: PropTypes.string.isRequired,
  items: PropTypes.array.isRequired,
  titles: PropTypes.object,
};

// Rows of one object. Wrap each row in <Table.Row key={i}>.
export const Rows = ({ rows, titles, onEdit }) => (
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
                titles={titles}
              />
            </Table.Cell>
          </Table.Row>
        );
      return (
        <Table.Row key={i}>
          <FieldRow row={row} titles={titles} onEdit={onEdit} />
        </Table.Row>
      );
    })}
  </>
);
Rows.propTypes = {
  rows: PropTypes.array.isRequired,
  titles: PropTypes.object,
  onEdit: PropTypes.func,
};
