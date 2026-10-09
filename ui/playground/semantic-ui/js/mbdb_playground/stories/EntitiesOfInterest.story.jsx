import React from "react";
import { EntitiesOfInterestSection } from "@js/mbdb/forms/sections/EntitiesOfInterest";
import complete from "./data/complete.json";

const Section = EntitiesOfInterestSection.component;
const Fields = () => (
  <Section formConfig={{ overridableIdPrefix: "mbdb.playground" }} />
);

const values = (list) => ({
  metadata: { general_parameters: { entities_of_interest: list } },
});

// The "Filled" scenario shows every alternative the entity table can hold: one
// entity per `Entity_base.type`, and for the biological origin one per
// `derived_from` sub-type (a sub-type renders different fields). It loads the
// whole `./data/complete.json` record (not just the entities slice), so the
// scenario mirrors the running deposit form, whose initial values are a full
// record; its `entities_of_interest` fill every optional array /
// array-of-object so the form renders filled complex structures.

const story = {
  title: "EntitiesOfInterest",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    { name: "Filled", initialValues: complete, render: Fields },
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
