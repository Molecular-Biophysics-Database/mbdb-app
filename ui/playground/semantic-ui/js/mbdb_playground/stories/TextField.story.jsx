import React from "react";
import {
  TextField,
  NumberField,
  TextAreaField,
} from "@js/mbdb/forms/building-blocks/TextField";

const BASE = "metadata.general_parameters.entities_of_interest.0";

const Fields = () => (
  <>
    <TextField
      fieldPath={`${BASE}.name`}
      helpText="Short descriptive name (id) of the entity; must be unique within a record."
    />
    <NumberField
      fieldPath={`${BASE}.molecular_weight.value`}
      label="Molecular weight value"
      helpText="A number; empty removes the value."
    />
    <TextAreaField
      fieldPath={`${BASE}.sequence`}
      label="Sequence"
      monospace
      autoHeight
      rows={2}
      links={[
        { label: "UniProt", href: "https://www.uniprot.org" },
        { label: "BLAST", href: "https://blast.ncbi.nlm.nih.gov" },
      ]}
      helpText="Primary sequence of the polymer."
    />
  </>
);

const story = {
  title: "TextField / NumberField / TextAreaField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                name: "Lysozyme",
                molecular_weight: { value: 14305.0, unit: "Da" },
                sequence:
                  "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV",
              },
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
              {
                name: "Missing data for required field.",
                molecular_weight: { value: "Must be a number." },
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
