import React from "react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { Divider } from "mbdb-semantic-ui-react";
import { ENTITY_PATH, entityValues, entityErrors } from "../fixtures";

const BASE = ENTITY_PATH;

// Explicit titles/helps until the ui_model has entity children (polymorphic
// Entity). fieldPath is the *object* path: it is also the element id (F5 of
// the review), so passing a leaf that a child field also uses would duplicate
// ids.
const Groups = () => (
  <>
    {/* fieldPath is the object path the group watches for errors (and its
        element id); it must not duplicate a child field's own path (F5). */}
    <FieldGroup
      title="Identification"
      required
      fieldPath={BASE}
      help="Header turns red for any error under the entity."
    >
      <TextField fieldPath={`${BASE}.name`} label="Name" />
    </FieldGroup>
    <Divider />
    {/* No fieldPath: plain group, no id, no error state. */}
    <FieldGroup title="Quantities" help="Layout in one Form.Group row." inline>
      <ValueUnitField
        fieldPath={`${BASE}.molecular_weight`}
        label="Molecular weight"
        units={["g/mol", "Da", "kDa", "MDa"]}
        defaultUnit="kDa"
      />
      <NumberField
        fieldPath={`${BASE}.copy_number`}
        label="Copy number"
        width={4}
      />
    </FieldGroup>
    <FieldGroup title="Nested example" nested>
      <TextField fieldPath={`${BASE}.variant`} label="Variant" />
    </FieldGroup>
  </>
);

const story = {
  title: "FieldGroup",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Groups },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        name: "Lysozyme",
        molecular_weight: { value: 14.3, unit: "kDa" },
        copy_number: 2,
      }),
      render: Groups,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors("name", "Missing data for required field."),
      render: Groups,
    },
  ],
};

export default story;
