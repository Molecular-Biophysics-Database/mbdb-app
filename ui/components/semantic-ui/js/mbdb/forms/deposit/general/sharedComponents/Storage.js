import React from "react";
import Temperature from "../../sharedComponents/Temperature";
import Duration from "../../sharedComponents/Duration";
import ArrayField from "../../buildingBlocks/ArrayField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import StoragePreparation from "./StoragePreparation";
import OptionalField from "../../buildingBlocks/OptionalField";

export default function Storage({ name, colorSchema }) {
  const tooltips = {
    duration: "Length of time the sample was stored before being measured",
    storagePreparation:
      "The specific steps that were taken to prepare the samples for storage (e.g. flash freezing in liquid nitrogen), if applicable",
  };

  return (
    <>
      <Temperature
        name={`${name}.temperature`}
        tooltip="The temperature the sample was stored at"
        colorSchema={colorSchema}
      />

      <OptionalField
        name={name}
        label="Duration"
        fieldName="duration"
        tooltip={tooltips.duration}
        renderChild={({ optionalFieldName }) => (
          <Duration
            name={optionalFieldName}
            colorSchema={colorSchema}
            tooltip={tooltips.duration}
          />
        )}
      />

      <ArrayField
        name={name}
        label="Storage preparation"
        fieldName="storage_preparation"
        tooltip={tooltips.storagePreparation}
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Storage preparation ${index + 1}`}
            colorSchema={colorSchema}
            tooltip={tooltips.storagePreparation}
          >
            <StoragePreparation name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
