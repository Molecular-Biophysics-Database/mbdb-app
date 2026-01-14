import React from "react";
import CustomField from "../buildingBlocks/CustomField";

export default function Protocol({ name }) {
  return (
    <>
      <div className="flex">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="name"
            label="Name"
            tooltip="Descriptive name of the step"
            required
          />
        </div>
        <CustomField
          name={name}
          fieldName="description"
          label="Description"
          tooltip="Short description of the step"
          required
          width="w-80"
        />
      </div>
    </>
  );
}
