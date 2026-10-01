import React from "react";
import { BasicInformation } from "@js/mbdb/forms/shared/BasicInformation";

// The dropdown queries the live chemicals vocabulary (P2). The search index
// there is currently empty, so typing finds nothing until the instance is
// reindexed; the "Enter manually:" addition still appears and opens the
// manual form. The Picked scenario demos the full state once P2 is fixed.

const PATH =
  "metadata.general_parameters.entities_of_interest.0.basic_information";

const seed = (basicInformation) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Chemical",
          ...(basicInformation && { basic_information: basicInformation }),
        },
      ],
    },
  },
});

const Fields = () => <BasicInformation fieldPath={PATH} />;

const story = {
  title: "BasicInformation",
  scenarios: [
    { name: "Empty", initialValues: seed(undefined), render: Fields },
    {
      name: "Picked",
      // inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N = Water (sample draft)
      initialValues: seed({ id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" }),
      render: Fields,
    },
    {
      name: "Manual",
      initialValues: seed({
        title: { en: "my custom lipid mix" },
        chemical_formula: "C42H82NO8P",
        molecular_weight: { value: 760.1, unit: "g/mol" },
        additional_identifiers: ["cid:5497103"],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: seed(undefined),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { basic_information: "Missing data for required field." },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
