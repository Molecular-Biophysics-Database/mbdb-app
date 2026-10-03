import React from "react";
import { HomogeneityFields } from "@js/mbdb/forms/shared/QualityControls";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("quality_controls.homogeneity");

// HomogeneityFields is the field set shown under the Homogeneity row of
// QualityControls; this standalone story inspects it on its own (including the
// "more species observed than expected" note).
const Fields = () => <HomogeneityFields fieldPath={PATH} />;

const story = {
  title: "Homogeneity",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    {
      name: "Filled",
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
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        quality_controls: {
          homogeneity: {
            assessed: "Yes",
            expected_number_of_species: 1,
            number_of_species_observed: 2,
          },
        },
      }),
      initialErrors: entityErrors(
        "quality_controls.homogeneity.method",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
