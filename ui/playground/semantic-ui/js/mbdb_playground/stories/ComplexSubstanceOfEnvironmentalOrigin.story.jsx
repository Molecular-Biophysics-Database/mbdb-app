import React from "react";
import { ComplexSubstanceOfEnvironmentalOriginFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfEnvironmentalOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => (
  <ComplexSubstanceOfEnvironmentalOriginFields fieldPath={ENTITY_PATH} />
);

const story = {
  review: "entity",
  title: "ComplexSubstanceOfEnvironmentalOrigin",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Complex substance of environmental origin"),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues("Complex substance of environmental origin", {
        name: "Brno pond water",
        environment_type: { id: "env:1" },
        location: { latitude: 49.1951, longitude: 16.6068, altitude: 237 },
        preparation_protocol: [
          { name: "Filtration", description: "0.22 µm filter" },
        ],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Complex substance of environmental origin", {
        name: "Brno pond water",
      }),
      initialErrors: entityErrors(
        "location",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
