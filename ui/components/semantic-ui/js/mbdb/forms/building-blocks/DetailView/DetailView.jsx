/* Row and section lists are positional and never reorder, so the index is a
   legitimate key (carries meaning, not identity). See collect.js/Rows.jsx. */
/* eslint-disable react/no-array-index-key */
import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button, Label, Table } from "mbdb-semantic-ui-react";
import { errorMessages, hasError } from "@js/mbdb/forms/building-blocks/errors";
import isEqual from "lodash/isEqual";
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
const Section = ({ fieldPath, section, titles, onEdit }) => (
  <>
    <Table.Row>
      <Table.HeaderCell colSpan="2">{section.title}</Table.HeaderCell>
    </Table.Row>
    <Rows rows={section.rows} titles={titles} onEdit={onEdit} />
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
  titles: PropTypes.object,
  onEdit: PropTypes.func,
};

export const DetailView = ({
  fieldPath,
  groups = [],
  exclude = [],
  requiredPaths = [],
  vocabularyTitles = {},
  onEdit,
  itemName,
}) => {
  const { values, errors, initialErrors, initialValues } = useFormikContext();
  const obj = getIn(values, fieldPath);
  const required = useMergedRequired(fieldPath, groups, requiredPaths);
  // F1: rows read errors ∪ initialErrors. The same merge useFieldErrors
  // performs, inlined here because collect is pure (no hooks): the live
  // `errors` node wins; otherwise `initialErrors` applies while the value at
  // the path is unchanged. Each leaf row re-checks via useFieldErrors (§5).
  const hasErr = (path) => {
    if (errorMessages(errors, path).length > 0) return true;
    const unchanged = isEqual(getIn(values, path), getIn(initialValues, path));
    return unchanged && hasError(initialErrors, path);
  };
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
        <span className="ui grey text">Nothing filled in yet</span>
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
              titles={vocabularyTitles}
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
      fields: PropTypes.arrayOf(PropTypes.string).isRequired,
    })
  ),
  exclude: PropTypes.arrayOf(PropTypes.string),
  requiredPaths: PropTypes.arrayOf(PropTypes.string),
  vocabularyTitles: PropTypes.object,
  onEdit: PropTypes.func,
  itemName: PropTypes.string,
};
