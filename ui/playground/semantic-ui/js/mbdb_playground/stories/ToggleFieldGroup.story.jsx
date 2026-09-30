import React from "react";
import { ToggleFieldGroup } from "@js/mbdb/forms/building-blocks/ToggleFieldGroup";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";

const BASE = "metadata.general_parameters.entities_of_interest.0.identity";

const METHODS = ["Mass spectrometry", "SDS-PAGE", "Western blot"];

const Identity = () => (
  <>
    <ToggleFieldGroup
      fieldPath={`${BASE}.by_intact_mass`}
      label="By intact mass"
      help="How identity was determined by intact mass, if applicable."
      initialValue={{}}
    >
      <SelectField
        fieldPath={`${BASE}.by_intact_mass.method`}
        label="Method"
        options={METHODS}
      />
      <ValueUnitField
        fieldPath={`${BASE}.by_intact_mass.deviation_from_expected_mass`}
        label="Deviation from expected mass"
        units={["Da", "kDa"]}
        defaultUnit="Da"
      />
    </ToggleFieldGroup>
    <ToggleFieldGroup
      fieldPath={`${BASE}.by_sequencing`}
      label="By sequencing"
      initialValue={{}}
    >
      <SelectField
        fieldPath={`${BASE}.by_sequencing.method`}
        label="Method"
        options={["Sanger", "NGS"]}
      />
    </ToggleFieldGroup>
  </>
);

const story = {
  title: "ToggleFieldGroup",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Identity },
    {
      name: "Checked",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                identity: {
                  by_intact_mass: {
                    method: "Mass spectrometry",
                    deviation_from_expected_mass: { value: 0.5, unit: "Da" },
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
            entities_of_interest: [{ identity: { by_intact_mass: {} } }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                identity: {
                  by_intact_mass: {
                    method: "Missing data for required field.",
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
