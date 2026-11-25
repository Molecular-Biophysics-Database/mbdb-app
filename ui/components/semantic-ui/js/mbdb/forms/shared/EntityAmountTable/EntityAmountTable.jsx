import React from "react";
import PropTypes from "prop-types";
import { ReferenceField, ReferenceNames } from "@js/mbdb/forms/building-blocks/ReferenceField";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { ENTITIES_OF_INTEREST_PATH } from "@js/mbdb/forms/sections/EntitiesOfInterest/path";
import { CONCENTRATION_UNITS } from "@js/mbdb/forms/shared/units";
import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";

const entityColumn = (fieldPath) => ({
  field: "entity",
  label: "Entity",
  required: true,
  // eslint-disable-next-line react/display-name
  render: (row, index) => (
    <ReferenceField
      fieldPath={`${fieldPath}.${index}.entity`}
      targetPath={ENTITIES_OF_INTEREST_PATH}
      label=""
      help=""
      required
      placeholder="Select an entity of interest"
      aria-label="Entity"
    />
  ),
});

// Rows of an entity of interest and its concentration (a sample's targets and
// ligands).
export const EntityConcentrationTable = ({ fieldPath, addButtonLabel }) => (
  <TableArrayField
    fieldPath={fieldPath}
    minItems={1}
    addButtonLabel={addButtonLabel}
    columns={[
      entityColumn(fieldPath),
      {
        field: "concentration",
        label: "Concentration",
        required: true,
        // eslint-disable-next-line react/display-name
        render: (row, index) => (
          <ValueUnitField
            fieldPath={`${fieldPath}.${index}.concentration`}
            units={CONCENTRATION_UNITS}
            label=""
            help=""
            aria-label="Concentration"
          />
        ),
      },
    ]}
  />
);
EntityConcentrationTable.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  addButtonLabel: PropTypes.string.isRequired,
};

// Rows of an entity of interest and how many copies of it are involved.
export const EntityCopiesTable = ({ fieldPath }) => (
  <TableArrayField
    fieldPath={fieldPath}
    minItems={1}
    addButtonLabel="Add entity"
    columns={[
      entityColumn(fieldPath),
      { field: "copy_number", type: "number", width: 4 },
    ]}
  />
);
EntityCopiesTable.propTypes = { fieldPath: PropTypes.string.isRequired };

// The same two lists as read-only mini tables in the details
const ENTITY_ITEM_COLUMN = {
  field: "entity",
  label: "Entity",
  // eslint-disable-next-line react/display-name
  value: (v) => (
    <ReferenceNames value={v?.entity} targetPath={ENTITIES_OF_INTEREST_PATH} />
  ),
};
export const ENTITY_CONCENTRATION_ITEM_SPEC = {
  itemColumns: [
    ENTITY_ITEM_COLUMN,
    {
      field: "concentration",
      label: "Concentration",
      value: (v) => valueUnitText(v?.concentration),
    },
  ],
};
export const ENTITY_COPIES_ITEM_SPEC = {
  itemColumns: [
    ENTITY_ITEM_COLUMN,
    {
      field: "copy_number",
      label: "Copy number",
      value: (v) =>
        v?.copy_number === -1 ? "unknown" : v?.copy_number ?? "",
    },
  ],
};
