import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import ChemicalEnvironment from "../chemicalEnvironment/ChemicalEnvironment";
import UseDefault from "../../buildingBlocks/UseDefault";

function ChemicalEnvironmentTab({ name }) {
  const fieldName = "chemical_environments";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the chemical composition of the environments
          (buffers) the entities of interest were exposed to
        </FormWrapper>
      </div>

      <ArrayField
        name={name}
        label="Chemical environment"
        required
        fieldName={fieldName}
        tooltip="Composition of the chemical environment (colloquially known as the buffer)"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Chemical environment ${index + 1}`}
            tooltip="Composition of the chemical environment (colloquially known as the buffer)"
          >
            <ChemicalEnvironment name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ChemicalEnvironmentTab;
