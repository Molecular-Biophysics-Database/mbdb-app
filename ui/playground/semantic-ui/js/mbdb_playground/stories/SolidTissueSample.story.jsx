import React from "react";
import { SolidTissueSampleFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import { ENTITY_PATH, entityValues } from "../fixtures";

const Fields = () => <SolidTissueSampleFields fieldPath={ENTITY_PATH} />;

const values = (fields) =>
  entityValues("Complex substance of biological origin", fields, {
    derived_from: "Solid tissue sample",
  });

const story = {
  title: "SolidTissueSample",
  scenarios: [
    { name: "Empty", initialValues: values({}), render: Fields },
    {
      name: "Filled",
      // homogenized: false on purpose: it checks that `false` shows as "No",
      // not as unset
      initialValues: values({
        organ: "liver",
        health_status: "healthy",
        homogenized: false,
      }),
      render: Fields,
    },
  ],
};

export default story;
