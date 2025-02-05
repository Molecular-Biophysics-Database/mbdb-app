import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";

export default function Book({ name }) {
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
            width="w-[17.5rem]"
          />
        </div>

        <CustomField
          name={name}
          fieldName="publisher"
          label="Publisher"
          required
          tooltip="The full name of the publisher of the book"
          width="w-[17.5rem]"
        />
      </div>
    </>
  );
}
