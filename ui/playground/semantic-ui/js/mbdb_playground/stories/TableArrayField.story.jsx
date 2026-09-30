import React from "react";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";

const PATH =
  "metadata.general_parameters.entities_of_interest.0.preparation_protocol";

const Protocol = () => (
  <TableArrayField
    fieldPath={PATH}
    label="Preparation protocol"
    required
    minItems={1}
    addButtonLabel="Add step"
    help="List of the steps performed during the preparation of the complex substance."
    columns={[
      { field: "name", label: "Name", required: true, width: 4 },
      {
        field: "description",
        label: "Description",
        required: true,
        type: "textarea",
      },
    ]}
  />
);

const story = {
  title: "TableArrayField",
  scenarios: [
    { name: "Empty (min 1 row)", initialValues: {}, render: Protocol },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                preparation_protocol: [
                  {
                    name: "Centrifugation",
                    description: "10 min at 4000 g, supernatant kept",
                  },
                  { name: "Filtration", description: "0.22 µm filter" },
                ],
              },
            ],
          },
        },
      },
      render: Protocol,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                preparation_protocol: [
                  { name: "Centrifugation", description: "" },
                ],
              },
            ],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                preparation_protocol: [
                  { description: "Missing data for required field." },
                ],
              },
            ],
          },
        },
      },
      render: Protocol,
    },
  ],
};

export default story;
