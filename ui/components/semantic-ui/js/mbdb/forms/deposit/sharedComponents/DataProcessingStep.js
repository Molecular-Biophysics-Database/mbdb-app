import React from "react";
import CustomField from "../buildingBlocks/CustomField";
import OptionalField from "../buildingBlocks/OptionalField";

function DataProcessingStep({ name }) {
  const tooltips = {
    softwareName:
      "The name of the software that was used for the step (e.g. Excel)",
    softwareVersion: "The version of the software that was used for the step",
    linkToSourceCode:
      "If processing was performed with software where the source code is legally available a link can be specified here (e.g. self-written python script in a GitHub repository)",
  };

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="name"
            label="Name"
            required
            tooltip="Short descriptive name of the processing step"
          />
        </div>
        <CustomField
          name={name}
          fieldName="description"
          label="Description"
          required
          tooltip="Description of what the processing step was"
        />
      </div>
      <div className="flex">
        <div className="-mt-3 mr-3">
          <OptionalField
            name={name}
            label="Software name"
            fieldName="software_name"
            tooltip={tooltips.softwareName}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Software name"
                tooltip={tooltips.softwareName}
              />
            )}
          />
        </div>
        <div className="-mt-3 mr-3">
          <OptionalField
            name={name}
            label="Software version"
            fieldName="software_version"
            tooltip={tooltips.softwareVersion}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Software version"
                tooltip={tooltips.softwareVersion}
              />
            )}
          />
        </div>
        <div className="-mt-3">
          <OptionalField
            name={name}
            label="Link to source code"
            fieldName="link_to_source_code"
            tooltip={tooltips.linkToSourceCode}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Link to source code"
                tooltip={tooltips.linkToSourceCode}
              />
            )}
          />
        </div>
      </div>
    </>
  );
}

export default DataProcessingStep;
