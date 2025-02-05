import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import OptionField from "../../buildingBlocks/OptionField";
import ArrayField from "../../buildingBlocks/ArrayField";
import DataProcessingStep from "../../sharedComponents/DataProcessingStep";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionalField from "../../buildingBlocks/OptionalField";
import FileField from "../../buildingBlocks/FileField";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function RawMeasurementFile({ name, index, save, onDeleteFile, file }) {
  const tooltips = {
    description: "Short description of what the file contains",
    recommendedSoftware:
      "The name of the software recommended for opening and working with the file",
    processingStep:
      "List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)",
  };

  const originatesFromOptions = [
    { value: "Instrument software", label: "Instrument software" },
    { value: "User", label: "User" },
    { value: "MBDB", label: "MBDB" },
  ];

  const contextOptions = [
    { value: "Raw measurement data", label: "Raw measurement data" },
    { value: "Derived measurement data", label: "Derived measurement data" },
    { value: "Quality control report", label: "Quality control report" },
  ];

  const contentTypeOptions = [
    { value: "Text", label: "Text" },
    { value: "Binary", label: "Binary" },
    { value: "Text and binary", label: "Text and binary" },
  ];

  return (
    <>
      <div className="mb-3">
        <FileField
          key={index}
          name={name}
          fieldName="key"
          index={index}
          save={save}
          required
          file={file}
          onDeleteFile={onDeleteFile}
        />
      </div>
      <div className="w-[25rem] mr-7 mb-3">
        <FormWrapper colorSchema="light">
          <div className="flex">
            <div className="flex">
              <div className="mr-3 my-auto text-dark">Creation date</div>
              <div className="-mt-1 -ml-2 mr-3">
                <Tooltip
                  title={
                    <Typography style={{ color: "white", fontSize: 13 }}>
                      Creation date
                    </Typography>
                  }
                  arrow
                >
                  <span>?</span>
                </Tooltip>
              </div>
            </div>

            <CustomField
              name={name}
              type="date"
              fieldName="metadata.creation_date"
              required
            />
          </div>
        </FormWrapper>
      </div>
      <div className="mb-3">
        <OptionField
          name={name}
          options={originatesFromOptions}
          label="Originates from"
          fieldName="metadata.originates_from"
          width="w-[25rem]"
          tooltip="What is the source of the file"
          required
        />
      </div>
      <div className="mb-3">
        <OptionField
          name={name}
          fieldName="metadata.context"
          label="Context"
          tooltip="The context the file should be understood within (e.g. raw measurement data)"
          options={contextOptions}
          width="w-[25rem]"
          required
        />
      </div>
      <div className="mb-3">
        <OptionField
          name={name}
          fieldName="metadata.content_type"
          label="Content type"
          options={contentTypeOptions}
          tooltip="Type of the file content in terms of how it can be read (text, binary, etc.)"
          width="w-[25rem]"
          required
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Description"
          fieldName="metadata.description"
          tooltip={tooltips.description}
          renderChild={({ optionalFieldName }) => (
            <CustomField
              name={`${optionalFieldName}`}
              label="description"
              width="w-[25rem]"
              tooltip={tooltips.description}
            />
          )}
        />
      </div>

      <OptionalField
        name={name}
        label="Recommended software"
        fieldName="metadata.recommended_software"
        tooltip={tooltips.recommendedSoftware}
        renderChild={({ optionalFieldName }) => (
          <CustomField
            name={optionalFieldName}
            label="Recommended software"
            width="w-[25rem]"
            tooltip={tooltips.recommendedSoftware}
          />
        )}
      />

      <ArrayField
        name={name}
        label="processing step"
        fieldName="metadata.processing_step"
        tooltip={tooltips.processingStep}
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            colorSchema="light"
            headline={`Processing step ${index + 1}`}
            tooltip={tooltips.processingStep}
          >
            <DataProcessingStep name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default RawMeasurementFile;
