import React from "react";
import { TextField } from "mbdb-react-invenio-forms";
import { entityPath, entityValues, entityErrors } from "../fixtures";

// Proves the frame: a plain RIF TextField on a real model path. The mbdb
// wrappers read label/help/required from the model themselves (explicit
// props win), so this story passes nothing but the path.
const NAME_PATH = entityPath("name");

const NameField = () => <TextField fieldPath={NAME_PATH} />;

const withName = (name) => entityValues("Polymer", { name });

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
      initialErrors: entityErrors("name", "Missing data for required field."),
      render: NameField,
    },
  ],
};

export default story;
