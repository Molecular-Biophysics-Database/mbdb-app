import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import Overridable from "react-overridable";
import { buildUID } from "react-searchkit";
import { Label } from "mbdb-semantic-ui-react";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { ENTITY_SEEDS } from "@js/mbdb/forms/entities/seeds";
import { ENTITY_TYPES, ENTITY_TYPE_ORDER } from "./entityTypes";
import { EntityForm } from "./EntityForm";
import { duplicateNames } from "./duplicateNames";
import { ENTITIES_OF_INTEREST_PATH } from "./path";

// The Name cell plus a "Duplicate name" hint. Trimmed, case-sensitive; a hint
// only, never a client-side error (guide §8).
const NameCell = ({ value, duplicates }) => {
  const name = value?.name ?? "";
  return (
    <>
      {name}
      {duplicates.has(name.trim()) && (
        <Label basic color="yellow" size="mini" content="Duplicate name" />
      )}
    </>
  );
};
NameCell.propTypes = {
  value: PropTypes.object,
  duplicates: PropTypes.instanceOf(Set).isRequired,
};

// The section: a summary table of entities with "Add entity" by type, each row
// edited in a modal that holds the type-specific form (design
// EntitiesOfInterest.md). `detailGroups` and the "Details" column dispatch on
// the entity's type through ENTITY_TYPES.
export const EntitiesOfInterestSectionComponent = ({ formConfig }) => {
  const { values } = useFormikContext();
  const entities = getIn(values, ENTITIES_OF_INTEREST_PATH) ?? [];
  const duplicates = duplicateNames(entities);
  return (
    <Overridable
      id={buildUID(formConfig?.overridableIdPrefix, "EntitiesOfInterest")}
    >
      <ModalArrayField
        fieldPath={ENTITIES_OF_INTEREST_PATH}
        minItems={1}
        withIds
        itemLabel={(v) => `${v?.type ?? "Entity"}: ${v?.name || "new"}`}
        newItemOptions={ENTITY_TYPE_ORDER.map((type) => ({
          label: type,
          value: { type, ...ENTITY_SEEDS[type] },
        }))}
        columns={[
          {
            label: "Name",
            value: (v) => <NameCell value={v} duplicates={duplicates} />,
          },
          { label: "Type", value: (v) => v?.type ?? "" },
          {
            label: "Details",
            value: (v) => ENTITY_TYPES[v?.type]?.summary(v) ?? "",
          },
        ]}
        detailGroups={(v) => ENTITY_TYPES[v?.type]?.groups(v) ?? []}
        // Type and Name are already columns of the row: do not repeat them
        // under "Other" (design DetailView §2)
        detailProps={{ exclude: ["id", "type", "name"] }}
        // a component's nested modal shows the entity as "name (type) ›" and
        // its Done reads "Done, back to <the entity type's noun>"
        crumbLabel={(v) => `${v?.name ?? ""} (${v?.type ?? ""})`}
        crumbNoun={(v) => ENTITY_TYPES[v?.type]?.noun}
        renderForm={(itemPath) => <EntityForm fieldPath={itemPath} />}
      />
    </Overridable>
  );
};

EntitiesOfInterestSectionComponent.propTypes = {
  formConfig: PropTypes.object.isRequired,
};

export const EntitiesOfInterestSection = {
  key: "entities-of-interest",
  label: "Entities of interest",
  component: EntitiesOfInterestSectionComponent,
  includesPaths: [ENTITIES_OF_INTEREST_PATH],
};

export { ENTITIES_OF_INTEREST_PATH } from "./path";
