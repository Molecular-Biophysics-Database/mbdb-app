import React from "react";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { Divider } from "mbdb-semantic-ui-react";
import { ENTITY_PATH, entityValues, entityErrors } from "../fixtures";

const BASE = ENTITY_PATH;

const Fields = () => (
  <>
    <ButtonGroupField
      fieldPath={`${BASE}.expression_source_type`}
      label="Expression source type"
      options={["Natively", "Recombinantly", "Synthetically"]}
      help="The way the polymer was produced."
    />
    <Divider />
    <ButtonGroupField
      fieldPath={`${BASE}.homogenized`}
      label="Homogenized"
      options={[
        { value: true, text: "Yes" },
        { value: false, text: "No" },
      ]}
      help="Booleans are stored as booleans."
    />
  </>
);

const story = {
  title: "ButtonGroupField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        expression_source_type: "Recombinantly",
        homogenized: false,
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors(
        "expression_source_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
