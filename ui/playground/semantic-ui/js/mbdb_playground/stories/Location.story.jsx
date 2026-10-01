import React from "react";
import { Location } from "@js/mbdb/forms/shared/Location";

const BASE = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${BASE}.location`;

const Fields = () => <Location fieldPath={PATH} />;

const story = {
  title: "Location",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                location: {
                  latitude: 49.1951,
                  longitude: 16.6068,
                  altitude: 237,
                },
              },
            ],
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
            entities_of_interest: [{ location: { latitude: 95 } }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                location: {
                  latitude:
                    "Must be greater than or equal to -90 and less than or equal to 90.",
                  longitude: "Missing data for required field.",
                  altitude: "Missing data for required field.",
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
