import React from "react";
import { Size } from "@js/mbdb/forms/shared/Size";
import { entityPath, entityValues } from "../fixtures";

const PATH = entityPath("size");

// The polymorphic entity variants are merged into the entity item in the new
// model (no `details` level), so size sits directly on the entity. The seed
// marks the entity as a Lipid assembly, the only place size appears.
const seed = (fields = {}) =>
  entityValues("Complex substance of chemical origin", fields, {
    class: "Lipid assembly",
  });

const Fields = () => <Size fieldPath={PATH} />;

const story = {
  title: "Size",
  scenarios: [
    {
      name: "Empty",
      initialValues: seed(),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: seed({
        size: {
          type: "diameter",
          unit: "nm",
          mean: 120,
          lower: 90,
          upper: 150,
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: seed({ size: { mean: 45 } }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                size: {
                  type: "Missing data for required field.",
                  unit: "Missing data for required field.",
                },
              },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
