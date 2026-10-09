import React from "react";
import { PurityFields } from "@js/mbdb/forms/shared/QualityControls";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("quality_controls.purity");

// PurityFields is the field set shown under the Purity row of QualityControls;
// this standalone story inspects it on its own (the QualityControls story also
// shows it in context).
const Fields = () => <PurityFields fieldPath={PATH} />;

const story = {
  title: "Purity",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        quality_controls: {
          purity: {
            assessed: "Yes",
            method: "SDS-PAGE",
            purity_percentage: ">99 %",
          },
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
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
  ],
};

export default story;
