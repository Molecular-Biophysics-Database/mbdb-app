import React from "react";
import { StringArrayField } from "mbdb-react-invenio-forms";
import { entityPath, entityValues, entityErrors } from "../fixtures";

const PATH = entityPath("basic_information.additional_identifiers");

// StringListField is oarepo's StringArrayField behind the mbdb wrapper (help
// goes through HelpLabel/FieldHelp so the global help mode reaches it). Its
// remaining use is `additional_identifiers`; `additional_specifications` is a
// one-column table now (see StringTableField.story.jsx). The label/help are set
// explicitly because the model has none for this keyword array (guide §6).
const Fields = () => (
  <StringArrayField
    fieldPath={PATH}
    label="Additional identifiers"
    addButtonLabel="Add identifier"
    help="Additional identifiers of the chemical"
  />
);

const story = {
  title: "StringListField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Chemical", {
        basic_information: {
          additional_identifiers: ["cid:5497103", "smiles:O"],
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Chemical", {
        basic_information: { additional_identifiers: ["ok", ""] },
      }),
      initialErrors: entityErrors(
        "basic_information.additional_identifiers.1",
        "Shorter than 1 character."
      ),
      render: Fields,
    },
  ],
};

export default story;
