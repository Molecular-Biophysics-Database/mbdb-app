import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import InjectionParameter from "./InjectionParameter";

export default function Titration({ name }) {
  const tooltips = {
    injectionParameter:
      "Characteristics of each injection (i. e. number of injections at a specific volume of 0.2 ml)",
  };

  return (
    <>
      <div className="flex flex-col">
        <CustomField
          name={name}
          fieldName="number_injections"
          label="Number of injections"
          required
          tooltip="Number of injections performed in the measurement"
          type="number"
        />

        <ArrayField
          name={name}
          label="Injection parameter"
          fieldName="injection_parameters"
          tooltip={tooltips.injectionParameter}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Injection parameter ${index + 1}`}
              tooltip={tooltips.injectionParameter}
            >
              <InjectionParameter name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}
