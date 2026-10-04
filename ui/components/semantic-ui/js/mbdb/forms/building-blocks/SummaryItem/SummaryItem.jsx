/* Summary cells are positional by design (index is their identity). */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import {
  Button,
  Confirm,
  Icon,
  Label,
  Table,
  useDisclosureDefault,
} from "mbdb-semantic-ui-react";
import { hasData, useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";

// A one-line summary row of a complex object plus, when `detail` is given, a
// second row with the read-only details (design/building-blocks/SummaryItem.md).
// Must be rendered inside a Semantic Table inside Formik.
export const SummaryItem = ({
  fieldPath,
  cells,
  onEdit,
  onRemove,
  detail = null,
  itemName,
}) => {
  const { values } = useFormikContext();
  // Initial only: the playground's one-shot "Expand/Collapse all" default
  // (undefined in the deposit form, so closed as before); a user toggle wins.
  const disclosure = useDisclosureDefault();
  const [open, setOpen] = useState(() => disclosure === "open");
  const [confirming, setConfirming] = useState(false);
  const value = getIn(values, fieldPath);
  // badge reads errors ∪ initialErrors so it survives the first edit
  const { count: errorCount } = useFieldErrors(fieldPath);

  const colSpan = cells.length + 2; // toggle cell + data cells + actions cell

  const requestRemove = () =>
    hasData(value) ? setConfirming(true) : onRemove();

  // Row clicks and Enter toggle the details, except clicks on buttons, and
  // except clicks inside the Confirm portal: React bubbles synthetic events
  // through portals, so a dimmer/text click would otherwise reach the row.
  const onRowClick = (e) => {
    if (!detail || e.target.closest("button")) return;
    if (!e.currentTarget.contains(e.target)) return;
    setOpen((prev) => !prev);
  };
  const onRowKeyDown = (e) => {
    if (!detail || e.key !== "Enter" || e.target.closest("button")) return;
    setOpen((prev) => !prev);
  };

  return (
    <>
      <Table.Row
        className={open ? "mbdb-row-open" : undefined}
        onClick={onRowClick}
        onKeyDown={onRowKeyDown}
        tabIndex={detail ? 0 : undefined}
      >
        <Table.Cell collapsing>
          {detail && (
            <Button
              basic
              icon
              size="mini"
              type="button"
              aria-expanded={open}
              aria-label={`${open ? "Hide" : "Show"} details of ${itemName}`}
              onClick={() => setOpen((prev) => !prev)}
            >
              {open ? "▾" : "▸"}
            </Button>
          )}
        </Table.Cell>
        {cells.map((cell, i) => {
          const text = cell(value) ?? "";
          return (
            <Table.Cell key={i}>
              {text === "" ? <span className="mbdb-muted-text">—</span> : text}
            </Table.Cell>
          );
        })}
        <Table.Cell collapsing textAlign="right">
          {errorCount > 0 && (
            <Label
              color="red"
              as="button"
              type="button"
              size="mini"
              onClick={(e) => {
                e.stopPropagation();
                // the badge opens the editor at the first error (true);
                // the plain Edit button does not scroll (false)
                onEdit(true);
              }}
            >
              {`${errorCount} ${errorCount === 1 ? "error" : "errors"}`}
            </Label>
          )}{" "}
          <Button basic size="mini" type="button" onClick={() => onEdit(false)}>
            Edit
          </Button>{" "}
          {onRemove !== undefined && (
            <>
              <Button
                basic
                icon
                size="mini"
                type="button"
                aria-label={`Remove ${itemName}`}
                onClick={requestRemove}
              >
                <Icon name="close" />
              </Button>
              <Confirm
                open={confirming}
                header={`Remove ${itemName}?`}
                content="This cannot be undone."
                confirmButton="Remove"
                onCancel={() => setConfirming(false)}
                onConfirm={() => {
                  setConfirming(false);
                  onRemove();
                }}
              />
            </>
          )}
        </Table.Cell>
      </Table.Row>
      {detail && open && (
        <Table.Row className="mbdb-details mbdb-row-open">
          <Table.Cell colSpan={colSpan}>{detail}</Table.Cell>
        </Table.Row>
      )}
    </>
  );
};

SummaryItem.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  cells: PropTypes.arrayOf(PropTypes.func).isRequired,
  onEdit: PropTypes.func.isRequired,
  onRemove: PropTypes.func,
  detail: PropTypes.node,
  itemName: PropTypes.string.isRequired,
};
