import React from "react";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";

// Polymer type enum from models/general_parameters-definitions-rdm.yaml
const POLYMER_TYPES = [
  "cyclic-pseudo-peptide",
  "peptide nucleic acid",
  "polydeoxyribonucleotide",
  "polydeoxyribonucleotide/polyribonucleotide hybrid",
  "polypeptide(D)",
  "polypeptide(L)",
  "polyribonucleotide",
  "polysaccharide",
  "other",
];

const BASE = "metadata.general_parameters.entities_of_interest.0";

const Fields = () => (
  <SelectField
    fieldPath={`${BASE}.polymer_type`}
    options={POLYMER_TYPES}
    helpText="The type of polymer (e.g. polypeptide(L))."
  />
);

const story = {
  title: "SelectField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ polymer_type: "polypeptide(L)" }],
          },
        },
      },
      render: Fields,
    },
    {
      name: "Unknown value",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ polymer_type: "from old data" }],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
