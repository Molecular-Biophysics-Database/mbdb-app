import React from "react";
import { ToggleFieldGroup } from "@js/mbdb/forms/building-blocks/ToggleFieldGroup";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";

// Identity lives under quality_controls; by_* fields exist when assessed: "Yes"
// (models/general_parameters-definitions-rdm.yaml:2188, 2287).
const BASE =
  "metadata.general_parameters.entities_of_interest.0.quality_controls.identity";

// Method enums from the model (Keep in sync with By_intact_mass.method /
// By_sequencing.method). MOLECULAR_WEIGHT_UNITS per the model.
const INTACT_MASS_METHODS = ["Mass spectrometry", "SDS-PAGE"];
const SEQUENCING_METHODS = ["Sanger sequencing", "Next-generation sequencing"];
const MOLECULAR_WEIGHT_UNITS = ["g/mol", "Da", "kDa", "MDa"];

// Explicit labels/helps until the ui_model has children for polymorphic types.
const Identity = () => (
  <>
    <ToggleFieldGroup
      fieldPath={`${BASE}.by_intact_mass`}
      label="By intact mass"
      help="How identity was assessed by intact mass, if applicable."
    >
      <SelectField
        fieldPath={`${BASE}.by_intact_mass.method`}
        label="Method"
        options={INTACT_MASS_METHODS}
      />
      <ValueUnitField
        fieldPath={`${BASE}.by_intact_mass.deviation_from_expected_mass`}
        label="Deviation from expected mass"
        units={MOLECULAR_WEIGHT_UNITS}
        defaultUnit="Da"
      />
    </ToggleFieldGroup>
    <ToggleFieldGroup
      fieldPath={`${BASE}.by_sequencing`}
      label="By sequencing"
      help="How identity was assessed by sequencing, if applicable."
    >
      <SelectField
        fieldPath={`${BASE}.by_sequencing.method`}
        label="Method"
        options={SEQUENCING_METHODS}
      />
    </ToggleFieldGroup>
  </>
);

const story = {
  title: "ToggleFieldGroup",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Identity },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                quality_controls: {
                  identity: {
                    assessed: "Yes",
                    by_intact_mass: {
                      method: "Mass spectrometry",
                      deviation_from_expected_mass: { value: 0.5, unit: "Da" },
                    },
                  },
                },
              },
            ],
          },
        },
      },
      render: Identity,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                quality_controls: {
                  identity: { assessed: "Yes", by_intact_mass: {} },
                },
              },
            ],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                quality_controls: {
                  identity: {
                    by_intact_mass: {
                      method: "Missing data for required field.",
                    },
                  },
                },
              },
            ],
          },
        },
      },
      render: Identity,
    },
  ],
};

export default story;
