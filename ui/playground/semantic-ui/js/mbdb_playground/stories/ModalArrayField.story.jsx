import React from "react";
import PropTypes from "prop-types";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";

const PATH = "metadata.general_parameters.entities_of_interest";

const ENTITY_TYPES = ["Polymer", "Chemical"];

// Mini stand-in for the real entity modal (plan steps 4–5 build the full one
// on the same ModalArrayField).
const EntityForm = ({ fieldPath }) => (
  <>
    <DiscriminatorField
      objectPath={fieldPath}
      field="type"
      options={ENTITY_TYPES}
      variant="dropdown"
    />
    <TextField fieldPath={`${fieldPath}.name`} />
  </>
);

EntityForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};

const Entities = () => (
  <ModalArrayField
    fieldPath={PATH}
    label="Entities of interest"
    required
    itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
    columns={[
      { title: "Name", value: (v) => v.name },
      { title: "Type", value: (v) => v.type },
    ]}
    newItemOptions={ENTITY_TYPES.map((t) => ({ label: t, value: { type: t } }))}
    withIds
    renderForm={(itemPath) => <EntityForm fieldPath={itemPath} />}
  />
);

const story = {
  title: "ModalArrayField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Entities },
    {
      name: "Filled",
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
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ id: "e-1", type: "Polymer", name: "" }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { name: "Missing data for required field." },
            ],
          },
        },
      },
      render: Entities,
    },
  ],
};

export default story;
