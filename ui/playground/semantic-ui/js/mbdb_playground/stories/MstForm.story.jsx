import React from "react";
import { EntitiesOfInterestSection } from "@js/mbdb/forms/sections/EntitiesOfInterest";
import mstRecord from "./data/mst.json";

const Section = EntitiesOfInterestSection.component;
const Fields = () => (
  <Section formConfig={{ overridableIdPrefix: "mbdb.playground" }} />
);

// A sneak peek of the MST deposit form (ui/mst/semantic-ui/js/mst/forms):
// the same section the real form renders, with the record from
// sample_data/mst/MST.json loaded as initial values, so the entities the MST
// measurement studies (human serum and hemoglobin) fill the form.

const story = {
  title: "MST form",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "MST record (serum + hemoglobin)",
      initialValues: mstRecord,
      render: Fields,
    },
  ],
};

export default story;
