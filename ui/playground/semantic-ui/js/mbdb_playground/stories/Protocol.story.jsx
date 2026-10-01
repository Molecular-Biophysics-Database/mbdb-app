import React from "react";
import { Protocol } from "@js/mbdb/forms/shared/Protocol";

const BASE = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${BASE}.preparation_protocol`;

// required use (complex substances): one virtual row to start with
const Fields = () => <Protocol fieldPath={PATH} minItems={1} />;

// draft gvfzs-t5060, entity "Human serum"
const SAMPLE_PROTOCOL = [
  {
    name: "Centrifugation",
    description:
      "Tubes were centrifuged for 10 min at 1,300g at 4°C within 2 hours of collection",
  },
  {
    name: "Aliquotation",
    description:
      "The supernatant was distributed among 0.5mL cryostorage tubes that were maintained at 4°C",
  },
];

const story = {
  title: "Protocol",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ preparation_protocol: SAMPLE_PROTOCOL }],
          },
        },
      },
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { preparation_protocol: [{ name: "Centrifugation" }] },
            ],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                preparation_protocol: {
                  0: { description: "Missing data for required field." },
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
