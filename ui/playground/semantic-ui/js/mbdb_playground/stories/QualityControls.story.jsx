import React from "react";
import { QualityControls } from "@js/mbdb/forms/shared/QualityControls";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("quality_controls");

const Fields = () => <QualityControls fieldPath={PATH} />;

// constructed (the sample records have no quality controls)
const FILLED = entityValues("Polymer", {
  name: "Hemoglobin subunit beta",
  quality_controls: {
    purity: { assessed: "Yes", method: "SDS-PAGE", purity_percentage: ">99 %" },
    identity: {
      assessed: "Yes",
      by_intact_mass: {
        method: "Mass spectrometry",
        deviation_from_expected_mass: { value: 0.5, unit: "Da" },
      },
      by_sequencing: { method: "Sanger sequencing", coverage: 98 },
    },
    homogeneity: { assessed: "No" },
  },
});

const story = {
  title: "Quality controls",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    { name: "Filled", initialValues: FILLED, render: Fields },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        name: "Hemoglobin subunit beta",
        quality_controls: {
          purity: { assessed: "Yes", method: "SDS-PAGE" },
        },
      }),
      initialErrors: entityErrors(
        "quality_controls.purity.purity_percentage",
        "Missing data for required field."
      ),
      render: Fields,
    },
    {
      name: "Identity: Yes, no method",
      initialValues: entityValues("Polymer", {
        quality_controls: { identity: { assessed: "Yes" } },
      }),
      render: Fields,
    },
    {
      name: "Homogeneity: more observed",
      initialValues: entityValues("Polymer", {
        quality_controls: {
          homogeneity: {
            assessed: "Yes",
            method: "Mass photometry",
            expected_number_of_species: 1,
            number_of_species_observed: 2,
          },
        },
      }),
      render: Fields,
    },
  ],
};

export default story;
