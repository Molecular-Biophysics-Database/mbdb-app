import React from "react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { Divider, Message } from "mbdb-semantic-ui-react";

const BASE = "metadata.general_parameters.entities_of_interest.0";

const ENTITY_TYPES = [
  "Polymer",
  "Chemical",
  "Molecular assembly",
  "Complex substance of biological origin",
  "Complex substance of environmental origin",
  "Complex substance of chemical origin",
  "Complex substance of industrial origin",
];

const Fields = () => (
  <>
    <Message
      info
      size="small"
      content="Change the type after filling the sequence: a confirmation asks first, then only `id` is kept. Change it on an empty entity: no confirmation."
    />
    <DiscriminatorField
      objectPath={BASE}
      field="type"
      options={ENTITY_TYPES}
      variant="dropdown"
    />
    <Divider />
    <DiscriminatorField
      objectPath={`${BASE}.quality_controls.purity`}
      field="assessed"
      label="Purity"
      options={["Yes", "No"]}
      variant="buttons"
      allowUnset
      unsetLabel="Not specified"
      helpText="Not specified means the whole object is absent."
    />
  </>
);

const story = {
  title: "DiscriminatorField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "With data",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                id: "e-1",
                type: "Polymer",
                name: "Lysozyme",
                sequence: "MKALIV",
                quality_controls: {
                  purity: { assessed: "Yes", method: "SDS-PAGE" },
                },
              },
            ],
          },
        },
      },
      render: Fields,
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
              { type: "Missing data for required field." },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
