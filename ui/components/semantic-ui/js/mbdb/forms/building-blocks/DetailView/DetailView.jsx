/* Row and section lists are positional and never reorder, so the index is a
   legitimate key (carries meaning, not identity). See collect.js/Rows.jsx. */
/* eslint-disable react/no-array-index-key */
import React from "react";
import PropTypes from "prop-types";
import { Button, Table } from "mbdb-semantic-ui-react";
import { Section } from "./Rows";
import { useSections } from "./collect";

// A generic read-only definition table built from a group spec — the
// "Details" (▸) view (design/building-blocks/DetailView.md). It reads Formik
// `values` and `errors` ∪ `initialErrors` (via useSections); it never writes.

export const DetailView = ({
  fieldPath,
  groups = [],
  exclude = [],
  requiredPaths = [],
  onEdit,
  itemName,
}) => {
  const sections = useSections(fieldPath, groups, exclude, requiredPaths);
  if (!sections) return null;
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
      // vocabulary reference whose title comes from the server cache; an
      // array-of-complex field may also declare `itemColumns` (its mini-table
      // columns) and `itemGroups` (its items' details groups)
      fields: PropTypes.arrayOf(
        PropTypes.oneOfType([
          PropTypes.string,
          PropTypes.shape({
            field: PropTypes.string.isRequired,
            vocabulary: PropTypes.string,
            itemColumns: PropTypes.array,
            itemGroups: PropTypes.oneOfType([PropTypes.array, PropTypes.func]),
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
