import React from "react";
import { ComplexSubstanceCommonFields } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <ComplexSubstanceCommonFields fieldPath={ENTITY_PATH} />;

const story = {
  title: "ComplexSubstanceCommon",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Complex substance of industrial origin"),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues("Complex substance of industrial origin", {
        preparation_protocol: [
          {
            name: "Centrifugation",
            description: "10 min at 4000 g, supernatant kept",
          },
          { name: "Filtration", description: "0.22 µm filter" },
        ],
        storage: {
          temperature: { value: -80, unit: "°C" },
          duration: { value: 3, unit: "months" },
          storage_preparation: [
            {
              name: "Flash freezing",
              description: "Aliquots frozen in liquid nitrogen",
            },
          ],
        },
        additional_specifications: ["Freshly prepared"],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      // preparation_protocol is required with minItems 1: an empty list is an error
      initialValues: entityValues("Complex substance of industrial origin"),
      initialErrors: entityErrors(
        "preparation_protocol",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
