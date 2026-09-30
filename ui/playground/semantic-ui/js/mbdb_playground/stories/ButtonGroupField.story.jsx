import React from "react";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { Divider } from "mbdb-semantic-ui-react";

const BASE = "metadata.general_parameters.entities_of_interest.0";

const Fields = () => (
  <>
    <ButtonGroupField
      fieldPath={`${BASE}.expression_source_type`}
      label="Expression source type"
      options={["Natively", "Recombinantly", "Synthetically"]}
      helpText="The way the polymer was produced."
    />
    <Divider />
    <ButtonGroupField
      fieldPath={`${BASE}.homogenized`}
      label="Homogenized"
      options={[
        { value: true, text: "Yes" },
        { value: false, text: "No" },
      ]}
      helpText="Booleans are stored as booleans."
    />
  </>
);

const story = {
  title: "ButtonGroupField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { expression_source_type: "Recombinantly", homogenized: false },
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
              { expression_source_type: "Missing data for required field." },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
