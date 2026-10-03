import React from "react";
import { CellFractionFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import { ENTITY_PATH, entityValues } from "../fixtures";

const Fields = () => <CellFractionFields fieldPath={ENTITY_PATH} />;

const values = (fields) =>
  entityValues("Complex substance of biological origin", fields, {
    derived_from: "Cell fraction",
  });

const story = {
  title: "CellFraction",
  scenarios: [
    { name: "Empty", initialValues: values({}), render: Fields },
    {
      name: "Filled",
      initialValues: values({
        fraction: { id: "cf:1" },
        health_status: "healthy",
        organ: "liver",
        tissue: "muscle",
        cell_type: "macrophage",
      }),
      render: Fields,
    },
  ],
};

export default story;
