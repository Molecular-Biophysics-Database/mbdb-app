import React from "react";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";
import { entityPath, entityValues, entityErrors } from "../fixtures";

const PATH = entityPath("molecular_weight");

const Fields = () => <MolecularWeight fieldPath={PATH} />;

const story = {
  title: "MolecularWeight",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      // 64.5 kDa: human Hemoglobin (sample record)
      initialValues: entityValues("Polymer", {
        molecular_weight: { value: 64.5, unit: "kDa" },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors(
        "molecular_weight",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
