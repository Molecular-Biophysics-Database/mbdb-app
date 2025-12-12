import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";

export default function RecordInformation({ name }) {
  return (
    <>
      <FormWrapper>
        <CustomField
          name={name}
          fieldName="title"
          label="Title"
          required
          width="w-full"
          tooltip="Short descriptive title of the record"
        />
      </FormWrapper>
    </>
  );
}
