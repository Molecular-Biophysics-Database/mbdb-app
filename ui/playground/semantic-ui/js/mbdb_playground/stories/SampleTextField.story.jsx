import React from "react";
import { TextField } from "mbdb-react-invenio-forms";
import { useFieldData } from "@js/oarepo_ui/forms";

// Proves the frame: a plain RIF TextField on a real model path, with the model's
// label and help. The mbdb field wrappers (plan step 1) will read them themselves.
const NAME_PATH = "metadata.general_parameters.entities_of_interest.0.name";

const NameField = () => {
  const { getFieldData } = useFieldData();
  const { label, helpText, placeholder, required } = getFieldData({
    fieldPath: NAME_PATH,
  });
  return (
    <TextField
      fieldPath={NAME_PATH}
      label={label}
      helpText={helpText}
      placeholder={placeholder}
      required={required}
    />
  );
};

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
