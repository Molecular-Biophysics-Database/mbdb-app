import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Chemical from "../entitiesOfInterest/Chemical";
import Polymer from "../entitiesOfInterest/Polymer";
import UseDefault from "../../buildingBlocks/UseDefault";
import ComplexSubstanceOfBiologicalOrigin from "../entitiesOfInterest/ComplexSubstanceOfBiologicalOrigin";
import MolecularAssembly from "../entitiesOfInterest/MolecularAssembly";
import ComplexSubstanceOfIndustrialOrigin from "../entitiesOfInterest/ComplexSubstanceOfIndustrialOrigin";
import ComplexSubstanceOfEnvironmentalOrigin from "../entitiesOfInterest/ComplexSubstanceOfEnvironmentalOrigin";
import ComplexSubstanceOfChemicalOrigin from "../entitiesOfInterest/ComplexSubstanceOfChemicalOrigin";
import ArrayField from "../../buildingBlocks/ArrayField";
import { getIn, useFormikContext } from "formik";
import DynamicOptionField from "../../buildingBlocks/DynamicOptionField";

function EntitiesOfInterestTab({ name }) {
  const { values } = useFormikContext();

  const componentName = `${name}.entities_of_interest[0].type`;

  UseDefault(componentName, "Polymer");

  const entitiesOfInterestTabOptions = [
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
      <div className="mb-3 w-fit">
        <FormWrapper>
          Identification of the measured molecules and the molecules/complex
          substances used to affect them
        </FormWrapper>
      </div>
      <div>
        <ArrayField
          name={name}
          label="Entity of interest"
          fieldName="entities_of_interest"
          initialValue={{ type: "Polymer" }}
          required
          tooltip="List of the entities that are being directly measured, as well as the entities that are being used as a variable to influence the behavior of the directly measured entities (e.g. lysozyme, NAG3, NaCl). IMPORTANT! If the pH was varied by individually prepared chemical environments these should be specified individually in chemical environments"
          renderChild={({ arrayName, index }) => {
            const actualValue = getIn(values, `${arrayName}.${index}`);
            if (!actualValue) {
              return null;
            }
            return (
              <FormWrapper
                headline={`Entity of interest ${index + 1}`}
                tooltip="List of the entities that are being directly measured, as well as the entities that are being used as a variable to influence the behavior of the directly measured entities (e.g. lysozyme, NAG3,NaCl). IMPORTANT! If the pH was varied by individually prepared chemical environments these should be specified individually in chemical environments"
              >
                <div className="mb-3">
                  <DynamicOptionField
                    name={`${arrayName}.${index}`}
                    options={entitiesOfInterestTabOptions}
                    label="type"
                    fieldName="type"
                    required
                    width="w-full"
                    tooltip="The type of the entity, where the options are (biological) Polymer, Chemical, Molecular assembly (also includes all proteins composed of more than one polypeptide chain) or Complex substance. Chemical polymers such as PEG 5000 should be described as being a Chemical. Complex substance refers to substances which are not exactly specified by their exact chemical composition by the time measurements were performed, e.g. blood, serum, plant extract"
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
    </>
  );
}

export default EntitiesOfInterestTab;
