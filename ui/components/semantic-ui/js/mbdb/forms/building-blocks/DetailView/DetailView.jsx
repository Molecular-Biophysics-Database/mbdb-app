/* Row and section lists are positional and never reorder, so the index is a
   legitimate key (carries meaning, not identity). See collect.js/Rows.jsx. */
/* eslint-disable react/no-array-index-key */
import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button, Label, Table } from "mbdb-semantic-ui-react";
import {
  collectMessages,
  mergedErrorNode,
} from "@js/mbdb/forms/building-blocks/errors";
import { isPlainObject } from "./values";
import { DetailLabel } from "./DetailLabel";
import { Rows } from "./Rows";
import { groupSections, useMergedRequired } from "./collect";

// A generic read-only definition table built from a group spec — the
// "Details" (▸) view (design/building-blocks/DetailView.md). It reads Formik
// `values` and `errors` ∪ `initialErrors` (via useFieldErrors, F1); it never
// writes.

// One group of the form becomes a section: a header row plus its rows and the
// red "Missing" rows for required-but-absent fields (design §5).
const Section = ({ fieldPath, section, onEdit }) => (
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

export const DetailView = ({
  fieldPath,
  groups = [],
  exclude = [],
  requiredPaths = [],
  onEdit,
  itemName,
}) => {
  const formik = useFormikContext();
  const { values } = formik;
  const obj = getIn(values, fieldPath);
  const required = useMergedRequired(fieldPath, groups, requiredPaths);
  // Rows with a server error stay visible even when empty (design §5). collect
  // is pure (no hooks), so it cannot call useFieldErrors; mergedErrorNode is
  // the same errors∪initialErrors selection as a plain function, and the row
  // is kept when that node holds any message. Each leaf row still re-checks
  // via useFieldErrors at render.
  const hasErr = (path) =>
    collectMessages(mergedErrorNode(formik, path), []).length > 0;
  if (obj === undefined || obj === null) return null;
  const sections = groupSections(
    isPlainObject(obj) ? obj : {},
    fieldPath,
    groups,
    exclude,
    required,
    hasErr
  );
  const showEdit = typeof onEdit === "function";
  const editButton = showEdit && (
    <Button basic size="small" type="button" onClick={onEdit}>
      {`Edit ${itemName ?? ""}`.trim()}
    </Button>
  );
  if (sections.length === 0)
    return (
      <>
        <span className="mbdb-muted-text">Nothing filled in yet</span>
        {editButton && <div>{editButton}</div>}
      </>
    );
  return (
    <>
      <Table definition basic="very" compact>
        <Table.Body>
          {sections.map((section, si) => (
            <Section
              key={si}
              fieldPath={fieldPath}
              section={section}
              onEdit={onEdit}
            />
          ))}
        </Table.Body>
      </Table>
      {editButton && <div>{editButton}</div>}
    </>
  );
};

DetailView.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  groups: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      // a plain name, or `{ field, vocabulary }` when the field is a
      // vocabulary reference whose title comes from the server cache
      fields: PropTypes.arrayOf(
        PropTypes.oneOfType([
          PropTypes.string,
          PropTypes.shape({
            field: PropTypes.string.isRequired,
            vocabulary: PropTypes.string,
          }),
        ])
      ).isRequired,
    })
  ),
  exclude: PropTypes.arrayOf(PropTypes.string),
  requiredPaths: PropTypes.arrayOf(PropTypes.string),
  onEdit: PropTypes.func,
  itemName: PropTypes.string,
};
