import React from "react";
import CustomField from "../buildingBlocks/CustomField";
import OptionField from "../buildingBlocks/OptionField";
import OptionalField from "../buildingBlocks/OptionalField";

function DataFitting({ name }) {
  const tooltips = {
    softwareName:
      "The name of the software that was used for doing the data fitting (e.g. Excel)",
    softwareVersion: "The version of the software that was used for the step",
    quality: "Numerical value representing the quality estimate of the result",
    qualityType: "Type of the quality estimate",
  };

  const qualityOptions = [
    { value: "R^2", label: "R^2" },
    { value: "SEM", label: "SEM" },
    { value: "red. Chi^2", label: "red. Chi^2" },
    { value: "1sigma", label: "1sigma" },
    { value: "2sigma", label: "2sigma" },
    { value: "3sigma", label: "3sigma" },
    { value: "4sigma", label: "4sigma" },
    { value: "5sigma", label: "5sigma" },
    { value: "Skewness", label: "Skewness" },
  ];

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="model"
            required
            label="Model"
            tooltip="Description of the model (e.g. 1:1 binding)"
          />
        </div>
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
        <div className="-mt-3">
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
      </div>
      <div className="flex">
        <div className="-mt-3 mr-3">
          <OptionalField
            name={name}
            label="Quality"
            fieldName="quality"
            tooltip={tooltips.quality}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Quality"
                type="number"
                tooltip={tooltips.quality}
              />
            )}
          />
        </div>
        <div className="-mt-3">
          <OptionalField
            name={name}
            label="Quality type"
            fieldName="quality_type"
            tooltip={tooltips.qualityType}
            renderChild={({ optionalFieldName }) => (
              <OptionField
                name={optionalFieldName}
                options={qualityOptions}
                label="Quality type"
                tooltip={tooltips.qualityType}
              />
            )}
          />
        </div>
      </div>
    </>
  );
}

export default DataFitting;
