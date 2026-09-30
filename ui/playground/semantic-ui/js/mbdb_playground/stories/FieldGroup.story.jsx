import React from "react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import {
  TextField,
  NumberField,
} from "@js/mbdb/forms/building-blocks/TextField";

const BASE = "metadata.general_parameters.entities_of_interest.0";

const Groups = () => (
  <>
    {/* Title override on purpose: the group header is shorter than the model label of `name`. */}
    <FieldGroup title="Identification" required fieldPath={`${BASE}.name`}>
      <TextField
        fieldPath={`${BASE}.name`}
        helpText="Short descriptive name (id) of the entity; must be unique within a record."
      />
    </FieldGroup>
    <FieldGroup
      title="Details (inline)"
      help="Laid out in one Form.Group row"
      inline
    >
      <TextField fieldPath={`${BASE}.name`} label="Again" width={10} />
      <NumberField
        fieldPath={`${BASE}.copy_number`}
        label="Copy number (not in ui_model yet)"
        width={6}
      />
    </FieldGroup>
  </>
);

const story = {
  title: "FieldGroup",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Groups },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ name: "Lysozyme", copy_number: 2 }],
          },
        },
      },
      render: Groups,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: { general_parameters: { entities_of_interest: [{}] } },
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
      render: Groups,
    },
  ],
};

export default story;
