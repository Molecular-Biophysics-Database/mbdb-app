import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import BasicInformationField from "../../buildingBlocks/BasicInformationField";

export default function Chemical({ name }) {
  CreateUuid(name);

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

      <BasicInformationField
        name={`${name}.basic_information`}
        colorSchema="light"
      />

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
