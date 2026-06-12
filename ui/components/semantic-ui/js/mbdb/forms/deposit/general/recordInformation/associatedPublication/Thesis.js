import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";
import OptionField from "../../../buildingBlocks/OptionField";

export default function Thesis({ name }) {
  const degreeTypeOptions = [
    { value: "PhD", label: "PhD" },
    { value: "Habilitation", label: "Habilitation" },
    { value: "Master", label: "Master" },
    { value: "Bachelor", label: "Bachelor" },
  ];

  return (
    <>
      <div className="flex">
        <CustomField
          name={name}
          fieldName="pid"
          label="Pid"
          required
          tooltip="Persistent identifier associated with the publication (e.g. DOI, ISBN, URN)"
          width="w-[8rem]"
        />

        <div className="mx-3">
          <CustomField
            name={name}
            fieldName="title"
            label="Title"
            tooltip="The title of the publication"
            width="w-[22.82rem]"
          />
        </div>

        <OptionField
          name={name}
          options={degreeTypeOptions}
          label="Degree type"
          required
          fieldName="degree_type"
          tooltip="The type of degree (equivalent) the thesis was submitted to attain"
        />
      </div>
    </>
  );
}
