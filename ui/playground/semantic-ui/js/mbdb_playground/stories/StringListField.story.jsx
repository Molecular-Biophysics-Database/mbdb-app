import React from "react";
import { StringArrayField } from "mbdb-react-invenio-forms";

const PATH =
  "metadata.general_parameters.entities_of_interest.0.additional_specifications";

// StringListField is oarepo's StringArrayField behind the mbdb wrapper (help
// goes through HelpLabel/FieldHelp so the global help mode reaches it).
const Fields = () => (
  <StringArrayField
    fieldPath={PATH}
    label="Additional specifications"
    addButtonLabel="Add specification"
    help="Additional information about the entity can be specified here."
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
