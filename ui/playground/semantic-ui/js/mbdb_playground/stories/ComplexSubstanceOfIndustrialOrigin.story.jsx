import React from "react";
import { ComplexSubstanceOfIndustrialOriginFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfIndustrialOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => (
  <ComplexSubstanceOfIndustrialOriginFields fieldPath={ENTITY_PATH} />
);

const story = {
  review: "entity",
  title: "ComplexSubstanceOfIndustrialOrigin",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Complex substance of industrial origin"),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues("Complex substance of industrial origin", {
        name: "Whey sample",
        product: { id: "prod:2" },
        preparation_protocol: [
          { name: "Filtration", description: "0.22 µm filter" },
        ],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Complex substance of industrial origin", {
        name: "Whey sample",
      }),
      initialErrors: entityErrors(
        "product",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
