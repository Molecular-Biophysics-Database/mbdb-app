import React from "react";
import { IdentityFields } from "@js/mbdb/forms/shared/QualityControls";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("quality_controls.identity");

// IdentityFields is the field set shown under the Identity row of
// QualityControls; this standalone story inspects it on its own.
const Fields = () => <IdentityFields fieldPath={PATH} />;

const story = {
  title: "Identity",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        quality_controls: {
          identity: {
            assessed: "Yes",
            by_intact_mass: {
              method: "Mass spectrometry",
              deviation_from_expected_mass: { value: 0.5, unit: "Da" },
            },
            by_sequencing: { method: "Sanger sequencing", coverage: 98 },
          },
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        quality_controls: {
          identity: {
            assessed: "Yes",
            by_sequencing: { coverage: 98 },
          },
        },
      }),
      initialErrors: entityErrors(
        "quality_controls.identity.by_sequencing.method",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
