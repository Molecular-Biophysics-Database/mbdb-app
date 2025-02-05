import React from "react";
import CustomField from "../../buildingBlocks/CustomField";

export default function Ph({ name }) {
  return (
    <>
      <div className="bg-primary p-3 rounded-lg text-dark flex">
        <div className="m-auto font-bold mr-10">pH</div>

        <CustomField
          name={name}
          label="Value"
          type="number"
          required
          tooltip="The pH value of the chemical environment"
          width="w-[8.5rem]"
        />
      </div>
    </>
  );
}
