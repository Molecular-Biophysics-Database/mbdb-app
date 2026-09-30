import React from "react";
import { StringArrayField } from "@js/oarepo_ui/forms";

const PATH =
  "metadata.general_parameters.entities_of_interest.0.additional_specifications";

// StringListField is oarepo's StringArrayField used directly (no mbdb wrapper).
const Fields = () => (
  <StringArrayField
    fieldPath={PATH}
    addButtonLabel="Add specification"
    helpText="Additional information about the entity can be specified here."
  />
);

const story = {
  title: "StringListField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { additional_specifications: ["RNase free water", "desalted"] },
            ],
          },
        },
      },
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ additional_specifications: ["ok", ""] }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                additional_specifications: [null, "Shorter than 1 character."],
              },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
