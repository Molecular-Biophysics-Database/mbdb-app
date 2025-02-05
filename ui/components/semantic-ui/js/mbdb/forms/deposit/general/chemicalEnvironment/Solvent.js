import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionField from "../../buildingBlocks/OptionField";
import UseDefault from "../../buildingBlocks/UseDefault";
import ArrayField from "../../buildingBlocks/ArrayField";
import Chemical from "./constituent/Chemical";
import { getIn, useFormikContext } from "formik";

function Solvent({ name }) {
  const { values } = useFormikContext();

  const tooltip =
    "Information about the solvent component(s) of the chemical environment (e.g. water, D2O, DMSO, EtOH) can be specified here";

  const componentName = `${name}.solvent[0].type`;

  UseDefault(componentName, "Chemical");

  const entitiesOfInterestTabOptions = [
    { value: "Chemical", label: "Chemical" },
  ];

  return (
    <>
      <ArrayField
        name={name}
        label="Solvent"
        fieldName="solvent"
        initialValue={{ type: "Chemical" }}
        required
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => {
          const actualValue = getIn(values, `${arrayName}.${index}`);
          if (!actualValue) {
            return null;
          }
          return (
            <div>
              <FormWrapper
                headline={`Solvent ${index + 1}`}
                colorSchema="light"
                tooltip={tooltip}
              >
                <div className="mb-3">
                  <OptionField
                    name={`${arrayName}.${index}`}
                    options={entitiesOfInterestTabOptions}
                    label="type"
                    fieldName="type"
                    required
                    tooltip="The type of the constituent, options are Chemical"
                    width="w-full"
                  />
                </div>
                <div>
                  {actualValue.type === "Chemical" && (
                    <Chemical name={`${arrayName}.${index}`} />
                  )}
                </div>
              </FormWrapper>
            </div>
          );
        }}
      />
    </>
  );
}

export default Solvent;
