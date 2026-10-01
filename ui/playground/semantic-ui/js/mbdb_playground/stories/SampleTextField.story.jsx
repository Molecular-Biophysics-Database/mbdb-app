import React from "react";
import { TextField } from "mbdb-react-invenio-forms";

// Proves the frame: a plain RIF TextField on a real model path. The mbdb
// wrappers read label/help/required from the model themselves (explicit
// props win), so this story passes nothing but the path.
const NAME_PATH = "metadata.general_parameters.entities_of_interest.0.name";

const NameField = () => <TextField fieldPath={NAME_PATH} />;

const withName = (name) => ({
  metadata: { general_parameters: { entities_of_interest: [{ name }] } },
});

const story = {
  title: "Sample: plain TextField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: NameField },
    {
      name: "Filled",
      initialValues: withName("Human serum"),
      render: NameField,
    },
    {
      name: "With errors",
      initialValues: withName(""),
      initialErrors: withName("Missing data for required field."),
      render: NameField,
    },
  ],
};

export default story;
