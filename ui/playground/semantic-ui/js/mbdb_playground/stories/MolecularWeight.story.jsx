import React from "react";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";

const BASE = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${BASE}.molecular_weight`;

const Fields = () => <MolecularWeight fieldPath={PATH} />;

const story = {
  title: "MolecularWeight",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      // 64.5 kDa: human Hemoglobin (sample record)
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { molecular_weight: { value: 64.5, unit: "kDa" } },
            ],
          },
        },
      },
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: {},
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { molecular_weight: "Missing data for required field." },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
