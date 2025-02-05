import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import Concentration from "../../../sharedComponents/Concentration";
import BasicInformationField from "../../../buildingBlocks/BasicInformationField";

export default function Chemical({ name }) {
  const tooltips = {
    additionalSpecification:
      "Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)",
  };

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          label="Name"
          fieldName="name"
          required
          tooltip="Name of the chemical"
          width="w-full"
        />
      </div>
      <div className="mb-3">
        <Concentration
          name={`${name}.concentration`}
          tooltip="Concentration of the constituent including its relative concentration related to the collected sample or absolute concentration of the constituent"
        />
      </div>

      <BasicInformationField name={`${name}.basic_information`} />

      <ArrayField
        name={name}
        label="Additional specification"
        fieldName="additional_specifications"
        tooltip={tooltips.additionalSpecification}
        renderChild={({ arrayName, index }) => (
          <CustomField
            name={`${arrayName}.${index}`}
            label={`Additional specification ${index + 1}`}
            width="w-[15rem]"
            tooltip={tooltips.additionalSpecification}
          />
        )}
      />
    </>
  );
}
