import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Chemical from "./constituent/Chemical";
import Polymer from "./constituent/Polymer";
import ComplexSubstanceOfBiologicalOrigin from "./constituent/ComplexSubstanceOfBiologicalOrigin";
import ComplexSubstanceOfEnvironmentalOrigin from "./constituent/ComplexSubstanceOfEnvironmentalOrigin";
import MolecularAssembly from "./constituent/MolecularAssembly";
import ComplexSubstanceOfChemicalOrigin from "./constituent/ComplexSubstanceOfChemicalOrigin";
import ArrayField from "../../buildingBlocks/ArrayField";
import ComplexSubstanceOfIndustrialOrigin from "./constituent/ComplexSubstanceOfIndustrialOrigin";
import { getIn, useFormikContext } from "formik";
import DynamicOptionField from "../../buildingBlocks/DynamicOptionField";

function Constituent({ name }) {
  const { values } = useFormikContext();

  const tooltip =
    "List of the constituents, excluding solvent components, that made up the chemical environment (i.e. buffer system, salts, surfactants, crowding agents, serum, etc.)";

  const ChemicalEnvironmentTabOptions = [
    { value: "Polymer", label: "Polymer" },
    { value: "Chemical", label: "Chemical" },
    { value: "Molecular assembly", label: "Molecular assembly" },
    {
      value: "Complex substance of biological origin",
      label: "Complex substance of biological origin",
    },
    {
      value: "Complex substance of environmental origin",
      label: "Complex substance of environmental origin",
    },
    {
      value: "Complex substance of chemical origin",
      label: "Complex substance of chemical origin",
    },
    {
      value: "Complex substance of industrial origin",
      label: "Complex substance of industrial origin",
    },
  ];

  return (
    <>
      <div>
        <div>
          <ArrayField
            name={name}
            label="Constituent"
            fieldName="constituents"
            initialValue={{ type: "Chemical" }}
            tooltip={tooltip}
            renderChild={({ arrayName, index }) => {
              const actualValue = getIn(values, `${arrayName}.${index}`);
              if (!actualValue) {
                return null;
              }
              return (
                <FormWrapper
                  colorSchema="light"
                  headline={`Constituent ${index + 1}`}
                  tooltip={tooltip}
                >
                  <div className="mb-3">
                    <DynamicOptionField
                      name={`${arrayName}.${index}`}
                      options={ChemicalEnvironmentTabOptions}
                      label="type"
                      fieldName="type"
                      width="w-full"
                    />
                  </div>
                  <div>
                    {actualValue.type === "Polymer" && (
                      <Polymer name={`${arrayName}.${index}`} />
                    )}
                    {actualValue.type === "Chemical" && (
                      <Chemical name={`${arrayName}.${index}`} />
                    )}
                    {actualValue.type === "Molecular assembly" && (
                      <MolecularAssembly name={`${arrayName}.${index}`} />
                    )}
                    {actualValue.type ===
                      "Complex substance of biological origin" && (
                      <ComplexSubstanceOfBiologicalOrigin
                        name={`${arrayName}.${index}`}
                      />
                    )}
                    {actualValue.type ===
                      "Complex substance of environmental origin" && (
                      <ComplexSubstanceOfEnvironmentalOrigin
                        name={`${arrayName}.${index}`}
                      />
                    )}
                    {actualValue.type ===
                      "Complex substance of chemical origin" && (
                      <ComplexSubstanceOfChemicalOrigin
                        name={`${arrayName}.${index}`}
                      />
                    )}
                    {actualValue.type ===
                      "Complex substance of industrial origin" && (
                      <ComplexSubstanceOfIndustrialOrigin
                        name={`${arrayName}.${index}`}
                      />
                    )}
                  </div>
                </FormWrapper>
              );
            }}
          />
        </div>
      </div>
    </>
  );
}

export default Constituent;
