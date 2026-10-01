import React from "react";
import { ExternalDatabases } from "@js/mbdb/forms/shared/ExternalDatabases";

const FIELD =
  "metadata.general_parameters.entities_of_interest.0.external_databases";

const Content = () => <ExternalDatabases fieldPath={FIELD} />;

const story = {
  title: "ExternalDatabases",
  scenarios: [
    {
      name: "Empty",
      initialValues: {},
      render: Content,
    },
    {
      // mixed case ("Uniprot") and an unknown prefix ("chembl") on purpose —
      // real stored data contains both (design fixture)
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                external_databases: [
                  "pdb:2HCO",
                  "Uniprot:P69905",
                  "chembl:CHEMBL25",
                ],
              },
            ],
          },
        },
      },
      render: Content,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ external_databases: ["pdb:"] }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                external_databases: {
                  0: "Invalid external database reference.",
                },
              },
            ],
          },
        },
      },
      render: Content,
    },
  ],
};

export default story;
