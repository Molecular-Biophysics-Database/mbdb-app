import React from "react";
import { EntitiesOfInterestSection } from "@js/mbdb/forms/sections/EntitiesOfInterest";

const Section = EntitiesOfInterestSection.component;
const Fields = () => (
  <Section formConfig={{ overridableIdPrefix: "mbdb.playground" }} />
);

const values = (list) => ({
  metadata: { general_parameters: { entities_of_interest: list } },
});

// The two entities of draft gvfzs-t5060 ("Human serum", "human Hemoglobin")
// plus one Chemical (Water) (design EntitiesOfInterest.md).
const FILLED = [
  {
    id: "e-serum",
    type: "Complex substance of biological origin",
    name: "Human serum",
    derived_from: "Body fluid",
    source_organism: { id: "taxid:9606" },
    fluid: { id: "bf:2" },
    health_status: "Healthy",
    preparation_protocol: [
      { name: "Centrifugation", description: "10 min at 1,300g" },
    ],
  },
  {
    id: "e-hemoglobin",
    type: "Molecular assembly",
    name: "human Hemoglobin",
    molecular_weight: { value: 64.5, unit: "kDa" },
    components: [
      {
        type: "Polymer",
        name: "Hemoglobin subunit alpha",
        copy_number: 2,
        polymer_type: "polypeptide(L)",
      },
      {
        type: "Polymer",
        name: "Hemoglobin subunit beta",
        copy_number: 2,
        polymer_type: "polypeptide(L)",
      },
    ],
  },
  {
    id: "e-water",
    type: "Chemical",
    name: "Water",
    basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
  },
];

const story = {
  title: "EntitiesOfInterest",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    { name: "Filled", initialValues: values(FILLED), render: Fields },
    {
      name: "With errors",
      initialValues: values([{ id: "e-siga", type: "Polymer", name: "SigA" }]),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { polymer_type: "Missing data for required field." },
            ],
          },
        },
      },
      render: Fields,
    },
    {
      name: "Duplicates",
      initialValues: values([
        {
          id: "e-1",
          type: "Complex substance of biological origin",
          name: "Serum",
          derived_from: "Body fluid",
        },
        {
          id: "e-2",
          type: "Complex substance of biological origin",
          name: "Serum",
          derived_from: "Body fluid",
        },
      ]),
      render: Fields,
    },
  ],
};

export default story;
