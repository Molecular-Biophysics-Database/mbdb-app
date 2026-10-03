import React from "react";
import { MolecularAssemblyFields } from "@js/mbdb/forms/entities/MolecularAssembly";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <MolecularAssemblyFields fieldPath={ENTITY_PATH} />;

const story = {
  title: "MolecularAssembly",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Molecular assembly"),
      render: Fields,
    },
    {
      name: "Filled",
      // sample record, "human Hemoglobin", shortened to the fields this block
      // shows (the design's fixture)
      initialValues: entityValues("Molecular assembly", {
        name: "human Hemoglobin",
        molecular_weight: { value: 64.5, unit: "kDa" },
        external_databases: ["pdb:2HCO"],
        components: [
          {
            type: "Polymer",
            name: "Hemoglobin subunit alpha",
            polymer_type: "polypeptide(L)",
            molecular_weight: { value: 16.0, unit: "kDa" },
            expression_source_type: "Natively",
            copy_number: 2.0,
          },
          {
            type: "Polymer",
            name: "Hemoglobin subunit beta",
            polymer_type: "polypeptide(L)",
            molecular_weight: { value: 16.0, unit: "kDa" },
            expression_source_type: "Recombinantly",
            copy_number: 2.0,
          },
        ],
        quality_controls: {
          purity: {
            assessed: "Yes",
            method: "SDS-PAGE",
            purity_percentage: ">99 %",
          },
          homogeneity: { assessed: "No" },
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Molecular assembly", {
        name: "human Hemoglobin",
      }),
      // components is required with minItems 1: an empty list is an error
      initialErrors: entityErrors(
        "components",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
