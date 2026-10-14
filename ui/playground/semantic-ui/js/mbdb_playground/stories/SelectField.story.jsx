import React from "react";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ENTITY_PATH, entityValues, entityErrors } from "../fixtures";

// Polymer type enum from models/general_parameters-definitions-rdm.yaml
// (polymer_type at e.g. line 3040; keep in sync).
const POLYMER_TYPES = [
  "cyclic-pseudo-peptide",
  "peptide nucleic acid",
  "polydeoxyribonucleotide",
  "polydeoxyribonucleotide/polyribonucleotide hybrid",
  "polypeptide(D)",
  "polypeptide(L)",
  "polyribonucleotide",
];

const BASE = ENTITY_PATH;

// Explicit label/help until the ui_model has entity children (polymorphic
// Entity): without them the raw model path shows as the label.
const Fields = () => (
  <SelectField
    fieldPath={`${BASE}.polymer_type`}
    label="Polymer type"
    options={POLYMER_TYPES}
    help="The type of polymer (e.g. polypeptide(L))."
  />
);

const story = {
  title: "SelectField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        polymer_type: "polypeptide(L)",
      }),
      render: Fields,
    },
    {
      name: "Unknown value",
      initialValues: entityValues("Polymer", {
        polymer_type: "from old data",
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors(
        "polymer_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
