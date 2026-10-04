/* Rows in the read-only details are positional and never reorder, so the
   index is a legitimate key (carries meaning, not identity). See collect.js. */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import {
  Button,
  Label,
  Table,
  useDisclosureDefault,
} from "mbdb-semantic-ui-react";
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

// "a b", skipping falsy parts; undefined when there is nothing (so a cell
// without a class keeps className undefined, not "").
const cx = (...parts) => parts.filter(Boolean).join(" ") || undefined;

// The indentation class of a cell at `depth` (design §2a rule 1). Depth 0 is the
// table's own edge (group headers): no padding. Deeper than 3 reuses depth-3.
const depthClass = (depth) =>
  depth > 0 ? `mbdb-details-depth-${Math.min(depth, 3)}` : undefined;

// A nested sub-heading: every level resolves its own model label, joined
// with " › " (design §2, §4). The last N path segments of row.path match the
// N joined names, so each level gets its path-aware label. Rule 4/5: it reads as
// a header (not a field label) and must not pick up the definition-table style.
const Heading = ({ row }) => {
  const parts = row.name.split(" › ");
  const pathParts = row.path.split(".");
  const start = pathParts.length - parts.length;
  return (
    <Table.HeaderCell
      colSpan="2"
      className={cx("ignored", "mbdb-detail-group", depthClass(row.depth))}
    >
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

// One not-filled entry: its label chain, e.g. "Storage › Duration" (the model
// labels of each path segment, joined with " › ", design ReviewMode.md rule 4).
const NotFilledLabel = ({ fieldPath, path }) => {
  const segments = path.split(".");
  return (
    <>
      {segments.map((seg, i) => (
        <React.Fragment key={i}>
          {i > 0 ? " › " : ""}
          <DetailLabel
            path={`${fieldPath}.${segments.slice(0, i + 1).join(".")}`}
            fallback={seg}
          />
        </React.Fragment>
      ))}
    </>
  );
};
NotFilledLabel.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  path: PropTypes.string.isRequired,
};

// One group of the form becomes a section: a header row plus its rows and the
// red "Missing" rows for required-but-absent fields (design §5). Used by the
// top-level DetailView and by a mini row's own ▸ (the item's groups). A
// one-field group has no title (§2a rule 3).
export const Section = ({ fieldPath, section, onEdit }) => (
  <>
    {section.title && (
      <Table.Row>
        <Table.HeaderCell colSpan="2" className="ignored mbdb-detail-group">
          {section.title}
        </Table.HeaderCell>
      </Table.Row>
    )}
    <Rows rows={section.rows} onEdit={onEdit} />
    {section.missing.map((name) => (
      <Table.Row key={`miss-${name}`}>
        <Table.Cell width={4}>
          <DetailLabel path={`${fieldPath}.${name}`} fallback={name} />
        </Table.Cell>
        <Table.Cell>
          <Label color="red" size="small">
            Missing
          </Label>
        </Table.Cell>
      </Table.Row>
    ))}
    {/* review mode (rule 4): what this group has not filled */}
    {section.notFilled?.length > 0 && (
      <Table.Row>
        <Table.Cell
          colSpan="2"
          className="ignored mbdb-details-depth-1 mbdb-muted-text"
        >
          Not filled:{" "}
          {section.notFilled.map((path, i) => (
            <React.Fragment key={path}>
              {i > 0 ? ", " : ""}
              <NotFilledLabel fieldPath={fieldPath} path={path} />
            </React.Fragment>
          ))}
        </Table.Cell>
      </Table.Row>
    )}
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
  if (isEmptyValue(row.value) && !hasError && !row.notFilled) return null;
  return (
    <>
      <Table.Cell
        width={4}
        className={cx(
          depthClass(row.depth),
          row.groupGap && "mbdb-detail-group-gap"
        )}
      >
        <DetailLabel path={row.path} fallback={row.name} />
      </Table.Cell>
      <Table.Cell>
        {row.notFilled ? (
          // review mode: a header-less one-field group's empty row (rule 5)
          <span className="mbdb-muted-text">not filled</span>
        ) : (
          <>
            <Value
              name={row.name}
              value={row.value}
              vocabulary={row.vocabulary}
            />
            <ErrorNote path={row.path} onEdit={onEdit} />
          </>
        )}
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
    <Table definition basic="very" compact className="mbdb-detail-table">
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
// columns) when given, else the union of keys (`keys`). §2b rule 4: a row gets a
// ▸ only when the item has data OUTSIDE the columns; `showColumn` is false when
// no row has one, and the toggle column is dropped for the whole table.
const MiniRow = ({
  basePath,
  index,
  item,
  keys,
  itemColumns,
  itemGroups,
  showColumn,
  hasExtra,
  columnCount,
}) => {
  // Initial only: the playground's one-shot "Expand/Collapse all" default
  // (undefined in the deposit form, so closed as before); a user toggle wins.
  const disclosure = useDisclosureDefault();
  const [open, setOpen] = useState(() => disclosure === "open");
  const groups =
    typeof itemGroups === "function" ? itemGroups(item) : itemGroups;
  // the fields already shown as columns are not repeated in the details
  const exclude = itemColumns
    ? itemColumns.filter((column) => column.field).map((column) => column.field)
    : [];
  const canExpand = showColumn && hasExtra;
  return (
    <>
      <Table.Row>
        {showColumn && (
          <Table.Cell collapsing className="ignored">
            {hasExtra ? (
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
            ) : null}
          </Table.Cell>
        )}
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
      {canExpand && open && (
        <Table.Row className="mbdb-details">
          <Table.Cell
            colSpan={columnCount}
            className="ignored mbdb-details-depth-1"
          >
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
  showColumn: PropTypes.bool.isRequired,
  hasExtra: PropTypes.bool.isRequired,
  columnCount: PropTypes.number.isRequired,
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
  // §2b rule 4: a ▸ only when the item has data outside the columns; when no
  // row has one, the toggle column is dropped (no empty first column).
  const columnFields = itemColumns
    ? itemColumns.filter((column) => column.field).map((column) => column.field)
    : keys;
  const hasExtra = (item) =>
    Object.keys(item ?? {}).some(
      (key) => !columnFields.includes(key) && hasData(item?.[key])
    );
  const showColumn = items.some(hasExtra);
  const columnCount = keys.length + (showColumn ? 1 : 0);
  return (
    <Table compact="very" size="small">
      <Table.Header>
        <Table.Row>
          {showColumn && <Table.HeaderCell />}
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
            showColumn={showColumn}
            hasExtra={hasExtra(item)}
            columnCount={columnCount}
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
              className={cx("ignored", depthClass(row.depth))}
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
