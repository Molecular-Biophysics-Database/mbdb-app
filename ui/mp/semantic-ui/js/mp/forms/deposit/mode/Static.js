import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import Supplier from "@mbdb_deposit/sharedComponents/Supplier";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import Protocol from "@mbdb_deposit/sharedComponents/Protocol";

export default function Static({ name, colorSchema }) {
  const tooltips = {
    material: "The material the sample carrier (slide) is composed of",
    supplier: "Information about the supplier of the coverslip",
    cleaningProtocol: "List of steps taken to clean the coverslip",
  };

  return (
    <FormWrapper
      headline="Sample carrier"
      colorSchema={colorSchema}
      tooltip="Properties and preparation of the sample carrier"
      required
      name={name}
    >
      <div className="flex">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="surface_modification"
            label="Surface modification"
            tooltip={`Information about coating or other types of surface modification of the coverslip, ("None" if not modified)`}
            required
            width="w-[25rem]"
          />
        </div>
        <div className="-mt-3">
          <OptionalField
            name={name}
            label="Material"
            fieldName="material"
            tooltip={tooltips.material}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Material"
                tooltip={tooltips.material}
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Supplier"
          fieldName="supplier"
          tooltip={tooltips.supplier}
          renderChild={({ optionalFieldName }) => (
            <Supplier name={optionalFieldName} tooltip={tooltips.supplier} />
          )}
        />
      </div>
      <FormWrapper
        headline="Cleaning protocol"
        tooltip={tooltips.cleaningProtocol}
      >
        <ArrayField
          name={name}
          label="Step"
          fieldName="cleaning_protocol"
          tooltip={tooltips.cleaningProtocol}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Step ${index + 1}`}
              colorSchema="light"
              tooltip={tooltips.cleaningProtocol}
            >
              <Protocol name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </FormWrapper>
    </FormWrapper>
  );
}
