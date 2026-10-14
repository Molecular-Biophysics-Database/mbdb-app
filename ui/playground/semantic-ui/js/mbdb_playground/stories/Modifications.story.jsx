import React from "react";
import {
  Modifications,
  ModificationTable,
} from "@js/mbdb/forms/shared/Modifications";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const MODIFICATIONS_PATH = entityPath("modifications");
const ASSEMBLY_PATH = entityPath("chemical_modifications");

// two blocks in one story (design): the polymer's Modifications group, and
// the molecular assembly's standalone chemical_modifications table
const Fields = () => <Modifications fieldPath={MODIFICATIONS_PATH} />;
const AssemblyFields = () => <ModificationTable fieldPath={ASSEMBLY_PATH} />;

// constructed (the sample records have no modifications)
const FILLED = entityValues("Polymer", {
  name: "Hemoglobin subunit beta",
  modifications: {
    biological_postprocessing: [{ type: "Phosphorylation", position: "S10" }],
    chemical: [
      {
        type: "Deglycosylation",
        position: "N45",
        protocol: [
          { name: "PNGase F", description: "37 °C overnight" },
          { name: "Desalting", description: "Zeba spin column" },
        ],
      },
    ],
  },
});

// "With errors" = the Filled fixture minus protocol step 2's description, so
// both tables stay populated and only that one cell is missing data.
const WITH_ERRORS = JSON.parse(JSON.stringify(FILLED));
delete WITH_ERRORS.metadata.general_parameters.entities_of_interest[0]
  .modifications.chemical[0].protocol[1].description;

const story = {
  title: "Modifications",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    { name: "Filled", initialValues: FILLED, render: Fields },
    {
      name: "With errors",
      initialValues: WITH_ERRORS,
      initialErrors: entityErrors(
        "modifications.chemical.0.protocol.1.description",
        "Missing data for required field."
      ),
      render: Fields,
    },
    {
      name: "Assembly",
      initialValues: entityValues("Molecular assembly", {
        chemical_modifications: [{ type: "Biotinylation" }],
      }),
      render: AssemblyFields,
    },
  ],
};

export default story;
