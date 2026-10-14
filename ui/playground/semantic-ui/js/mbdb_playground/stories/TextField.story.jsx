import React from "react";
import {
  TextField,
  NumberField,
  TextAreaField,
} from "@js/mbdb/forms/building-blocks/TextField";
import { ENTITY_PATH, entityValues } from "../fixtures";

const BASE = ENTITY_PATH;

// Explicit labels/helps until the ui_model has entity children (polymorphic
// Entity): without them labels fall back to the readable leaf of the path.
const Fields = () => (
  <>
    <TextField
      fieldPath={`${BASE}.name`}
      help="Short descriptive name (id) of the entity; must be unique within a record."
    />
    <NumberField
      fieldPath={`${BASE}.molecular_weight.value`}
      label="Molecular weight value"
      help="A number; empty removes the value."
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
      help="Primary sequence of the polymer."
    />
  </>
);

const story = {
  title: "TextField / NumberField / TextAreaField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        name: "Lysozyme",
        molecular_weight: { value: 14305.0, unit: "Da" },
        sequence:
          "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV",
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer"),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                name: "Missing data for required field.",
                molecular_weight: { value: "Must be a number." },
                sequence: "Unknown residue at position 7.",
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
