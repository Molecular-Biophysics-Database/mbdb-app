import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";

function Article({ name }) {
  return (
    <>
      <div className="flex">
        <div>
          <CustomField
            name={name}
            fieldName="pid"
            label="Pid"
            required
            tooltip="Persistent identifier associated with the publication (e.g. DOI, ISBN, URN)"
            width="w-[8rem]"
          />
        </div>
        <div className="mx-3">
          <CustomField
            name={name}
            fieldName="title"
            label="Title"
            tooltip="The title of the publication"
            width="w-[17.5rem]"
          />
        </div>
        <div>
          <CustomField
            name={name}
            fieldName="journal"
            label="Journal"
            required
            tooltip="The full name of the journal the article appears in"
            width="w-[17.5rem]"
          />
        </div>
      </div>
    </>
  );
}

export default Article;
