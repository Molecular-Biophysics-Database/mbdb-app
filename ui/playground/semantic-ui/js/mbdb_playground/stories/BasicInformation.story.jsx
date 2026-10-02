import React from "react";
import { BasicInformation } from "@js/mbdb/forms/shared/BasicInformation";

// The dropdown queries the live chemicals vocabulary, which must be
// loaded and indexed. Manual entry is hidden until the backend keeps
// manual chemicals (chemical.js): the "Manual" scenario below stays as a
// demo of the disabled flow, and "Enter manually:" does not appear in the
// dropdown while the flag is off.

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
      // hidden until the backend keeps manual chemicals (chemical.js);
      // while the flag is off this fixture renders the picker, which is
      // exactly the disabled behaviour the scenario demonstrates
      name: "Manual (disabled: server drops manual chemicals)",
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
