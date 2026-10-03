import React from "react";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { Divider } from "mbdb-semantic-ui-react";
import { ENTITY_PATH, entityValues } from "../fixtures";

// MW and temperature units from models/general_parameters-definitions-rdm.yaml
const MW_UNITS = ["g/mol", "Da", "kDa", "MDa"];
const TEMPERATURE_UNITS = ["K", "°C", "°F"];

const BASE = ENTITY_PATH;

const Fields = () => (
  <>
    <ValueUnitField
      fieldPath={`${BASE}.molecular_weight`}
      label="Molecular weight"
      units={MW_UNITS}
      defaultUnit="kDa"
      help="kDa is pre-selected but written only together with a value."
    />
    <Divider />
    <ValueUnitField
      fieldPath={`${BASE}.storage.temperature`}
      label="Temperature"
      units={TEMPERATURE_UNITS}
      required
      help="Required variant without a default unit."
    />
  </>
);

const story = {
  title: "ValueUnitField",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        molecular_weight: { value: 14.3, unit: "kDa" },
        storage: { temperature: { value: 4, unit: "°C" } },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        molecular_weight: { value: -5, unit: "kDa" },
      }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                molecular_weight: "Missing data for required field.",
                storage: {
                  temperature: { unit: "Missing data for required field." },
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
