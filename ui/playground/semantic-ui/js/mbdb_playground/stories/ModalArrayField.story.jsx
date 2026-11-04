import React from "react";
import PropTypes from "prop-types";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { entityValues, entityErrors } from "../fixtures";

const PATH = "metadata.general_parameters.entities_of_interest";

const ENTITY_TYPES = ["Polymer", "Chemical"];

// Mini stand-in for the real entity modal (the section builds the full one
// on the same ModalArrayField).
const EntityForm = ({ fieldPath }) => (
  <>
    {/* Explicit label until the ui_model has entity children (polymorphic) */}
    <DiscriminatorField
      objectPath={fieldPath}
      field="type"
      label="Type"
      options={ENTITY_TYPES}
      variant="dropdown"
    />
    <TextField fieldPath={`${fieldPath}.name`} label="Name" />
  </>
);

EntityForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};

// Depth-2 stand-in: the entity modal's form contains another
// ModalArrayField (mini Components — no ids, optional list).
const NestedEntityForm = ({ fieldPath }) => (
  <>
    <TextField fieldPath={`${fieldPath}.name`} label="Name" />
    <ModalArrayField
      fieldPath={`${fieldPath}.components`}
      label="Components"
      minItems={0}
      itemLabel={(v) => `component: ${v?.name ?? "new"}`}
      columns={[
        { label: "Type", value: (v) => v.type },
        { label: "Name", value: (v) => v.name },
      ]}
      initialValue={{ type: "Polymer" }}
      withIds={false}
      renderForm={(p) => <TextField fieldPath={`${p}.name`} label="Name" />}
    />
  </>
);

NestedEntityForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};

const NestedEntities = () => (
  <ModalArrayField
    fieldPath={PATH}
    label="Entities of interest"
    itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
    columns={[{ label: "Name", value: (v) => v.name }]}
    initialValue={{ type: "Polymer" }}
    withIds
    renderForm={(itemPath) => <NestedEntityForm fieldPath={itemPath} />}
  />
);

const Entities = () => (
  <ModalArrayField
    fieldPath={PATH}
    label="Entities of interest"
    required
    minItems={1}
    itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
    columns={[
      { label: "Name", value: (v) => v.name },
      { label: "Type", value: (v) => v.type },
    ]}
    newItemOptions={ENTITY_TYPES.map((t) => ({ label: t, value: { type: t } }))}
    withIds
    detailGroups={[{ title: "Identification", fields: ["type", "name"] }]}
    renderForm={(itemPath) => <EntityForm fieldPath={itemPath} />}
  />
);

const story = {
  title: "ModalArrayField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Entities },
    {
      name: "Filled",
      // two entities: entityValues seeds one, so this array is written out
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { id: "e-1", type: "Polymer", name: "Lysozyme" },
              { id: "e-2", type: "Chemical", name: "NaCl" },
            ],
          },
        },
      },
      render: Entities,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", { id: "e-1", name: "" }),
      initialErrors: entityErrors("name", "Missing data for required field."),
      render: Entities,
    },
    {
      name: "Nested (depth 2)",
      // open an entity and add a component: the inner modal stacks on top;
      // Cancel on the inner keeps the outer edits, Cancel on the outer
      // drops the whole entity
      initialValues: entityValues("Polymer", {
        id: "e-1",
        name: "Lysozyme",
        components: [{ type: "Polymer", name: "chain A" }],
      }),
      render: NestedEntities,
    },
  ],
};

export default story;
