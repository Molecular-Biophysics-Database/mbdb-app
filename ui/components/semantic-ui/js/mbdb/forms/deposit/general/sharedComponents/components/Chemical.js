import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import BasicInformationField from "../../../buildingBlocks/BasicInformationField";

function Chemical({ name, colorSchema }) {
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
        colorSchema={colorSchema}
      />

      <ArrayField
        name={name}
        label="Additional specification"
        fieldName="additional_specifications"
        tooltip="Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)"
        renderChild={({ arrayName, index }) => (
          <CustomField
            name={`${arrayName}.${index}`}
            label={`Additional specification ${index + 1}`}
            width="w-[15rem]"
            tooltip="Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)"
          />
        )}
      />
    </>
  );
}

export default Chemical;
