import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import Overridable from "react-overridable";
import { buildUID } from "react-searchkit";
import { useReviewMode } from "mbdb-semantic-ui-react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { FieldRow } from "@js/mbdb/forms/building-blocks/FieldRow";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { StringTableField } from "@js/mbdb/forms/building-blocks/StringTableField";
import {
  NumberField,
  TextField,
} from "@js/mbdb/forms/building-blocks/TextField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { ENTITY_SEEDS } from "@js/mbdb/forms/entities/seeds";
import {
  ENTITY_TYPES,
  ENTITY_TYPE_ORDER,
} from "@js/mbdb/forms/sections/EntitiesOfInterest/entityTypes";
import { CONCENTRATION_UNITS } from "@js/mbdb/forms/shared/units";
import { CHEMICAL_ENVIRONMENTS_PATH } from "./path";

// A constituent is an entity (same types, same fields) with a concentration
// instead of an id, so the entity field sets and groups are reused.
const CONCENTRATION_GROUP = {
  title: "Concentration",
  fields: ["concentration"],
};
const constituentGroups = (v) => [
  CONCENTRATION_GROUP,
  ...(ENTITY_TYPES[v?.type]?.groups(v) ?? []),
];

const CONSTITUENT_COLUMNS = [
  { field: "name", label: "Name", value: (v) => v?.name ?? "" },
  { field: "type", label: "Type", value: (v) => v?.type ?? "" },
  {
    field: "concentration",
    label: "Concentration",
    value: (v) => valueUnitText(v?.concentration),
  },
  { label: "Details", value: (v) => ENTITY_TYPES[v?.type]?.summary(v) ?? "" },
];

const CONSTITUENT_ITEM_SPEC = {
  itemColumns: CONSTITUENT_COLUMNS,
  itemGroups: constituentGroups,
};

const ConstituentForm = ({ fieldPath, types }) => {
  const { values } = useFormikContext();
  const type = getIn(values, `${fieldPath}.type`);
  const Fields = ENTITY_TYPES[type]?.Fields;
  return (
    <>
      {types.length > 1 && (
        <DiscriminatorField
          objectPath={fieldPath}
          field="type"
          options={types}
          variant="dropdown"
          keep={["name", "concentration"]}
          seed={(newType) => ENTITY_SEEDS[newType]}
        />
      )}
      <FieldRow widths="equal">
        <TextField fieldPath={`${fieldPath}.name`} />
        <ValueUnitField
          fieldPath={`${fieldPath}.concentration`}
          units={CONCENTRATION_UNITS}
        />
      </FieldRow>
      {Fields ? <Fields fieldPath={fieldPath} /> : null}
    </>
  );
};
ConstituentForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  types: PropTypes.arrayOf(PropTypes.string).isRequired,
};

const ConstituentList = ({ fieldPath, types, minItems, noun }) => (
  <ModalArrayField
    fieldPath={fieldPath}
    minItems={minItems}
    itemLabel={(v) => v?.name || `New ${noun}`}
    newItemOptions={types.map((type) => ({
      label: types.length > 1 ? type : noun,
      value: { type, ...ENTITY_SEEDS[type] },
    }))}
    columns={CONSTITUENT_COLUMNS}
    detailGroups={constituentGroups}
    detailProps={{ exclude: ["name", "type"] }}
    crumbNoun={noun}
    renderForm={(itemPath) => (
      <ConstituentForm fieldPath={itemPath} types={types} />
    )}
  />
);
ConstituentList.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  types: PropTypes.arrayOf(PropTypes.string).isRequired,
  minItems: PropTypes.number,
  noun: PropTypes.string.isRequired,
};

const EnvironmentForm = ({ fieldPath }) => (
  <>
    <FieldRow widths="equal">
      <TextField fieldPath={`${fieldPath}.name`} />
      <NumberField fieldPath={`${fieldPath}.ph`} label="pH" />
    </FieldRow>
    <ConstituentList
      fieldPath={`${fieldPath}.constituents`}
      types={ENTITY_TYPE_ORDER}
      noun="constituent"
    />
    <ConstituentList
      fieldPath={`${fieldPath}.solvent`}
      types={["Chemical"]}
      minItems={1}
      noun="solvent"
    />
    <StringTableField
      fieldPath={`${fieldPath}.additional_specifications`}
      columnLabel="Specification"
      addButtonLabel="Add specification"
    />
  </>
);
EnvironmentForm.propTypes = { fieldPath: PropTypes.string.isRequired };

export const CHEMICAL_ENVIRONMENT_GROUPS = [
  {
    title: "Constituents",
    fields: [{ field: "constituents", ...CONSTITUENT_ITEM_SPEC }],
  },
  { title: "Solvent", fields: [{ field: "solvent", ...CONSTITUENT_ITEM_SPEC }] },
  { title: "Additional specifications", fields: ["additional_specifications"] },
];

const names = (items) =>
  (items ?? [])
    .map((item) => item?.name)
    .filter(Boolean)
    .join(", ");

export const ChemicalEnvironmentsSectionComponent = ({ formConfig }) => {
  const reviewMode = useReviewMode();
  return (
    <Overridable
      id={buildUID(formConfig?.overridableIdPrefix, "ChemicalEnvironments")}
    >
      <React.Fragment key={reviewMode ? "review" : "edit"}>
        <ModalArrayField
          fieldPath={CHEMICAL_ENVIRONMENTS_PATH}
          minItems={1}
          withIds
          itemLabel={(v) => v?.name || "New chemical environment"}
          newItemOptions={[{ label: "chemical environment", value: {} }]}
          columns={[
            { label: "Name", value: (v) => v?.name ?? "" },
            { label: "pH", value: (v) => v?.ph ?? "" },
            { label: "Constituents", value: (v) => names(v?.constituents) },
            { label: "Solvent", value: (v) => names(v?.solvent) },
          ]}
          detailGroups={CHEMICAL_ENVIRONMENT_GROUPS}
          detailProps={{ exclude: ["id", "name", "ph"] }}
          crumbNoun="environment"
          renderForm={(itemPath) => <EnvironmentForm fieldPath={itemPath} />}
        />
      </React.Fragment>
    </Overridable>
  );
};
ChemicalEnvironmentsSectionComponent.propTypes = {
  formConfig: PropTypes.object.isRequired,
};

export const ChemicalEnvironmentsSection = {
  key: "chemical-environments",
  label: "Chemical environments",
  component: ChemicalEnvironmentsSectionComponent,
  includesPaths: [CHEMICAL_ENVIRONMENTS_PATH],
};

export { CHEMICAL_ENVIRONMENTS_PATH } from "./path";
