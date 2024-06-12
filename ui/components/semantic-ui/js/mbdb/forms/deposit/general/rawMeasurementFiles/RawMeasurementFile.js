import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import OptionField from "../../buildingBlocks/OptionField";
import ArrayField from "../../buildingBlocks/ArrayField";
import DataProcessingStep from "../../sharedComponents/DataProcessingStep";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionalField from "../../buildingBlocks/OptionalField";
import FileField from "../../buildingBlocks/FileField";
import { useState } from "react";

function RawMeasurementFile({ name, index, save, onDeleteFile, file }) {
  const [isFileEditable, setIsFileEditable] = useState(() => {
    if (file?.file_id === undefined) {
      return false;
    } else {
      return file.file_id === undefined ? true : !!file.file_id;
    }
  });

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
          name={name}
          fieldName="key"
          index={index}
          width="w-[25rem]"
          save={save}
          required={true}
          file={file}
          setIsFileEditable={setIsFileEditable}
          isFileEditable={isFileEditable}
          onDeleteFile={onDeleteFile}
        />
      </div>
      <div className="mb-3">
        <OptionField
          name={name}
          options={originatesFromOptions}
          label="Originates from"
          fieldName="metadata.originates_from"
          width="w-[25rem]"
          tooltip="What is the source of the file"
          required={true}
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
          required={true}
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
          required={true}
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Description"
          fieldName="metadata.description"
          tooltip="Short description of what the file contains"
          renderChild={({ optionalFieldName }) => (
            <CustomField
              name={`${optionalFieldName}`}
              label="description"
              width="w-[25rem]"
              tooltip="Short description of what the file contains"
            />
          )}
        />
      </div>
      <div>
        <OptionalField
          name={name}
          label="Recommended software"
          fieldName="metadata.recommended_software"
          tooltip="The name of the software recommended for opening and working with the file"
          renderChild={({ optionalFieldName }) => (
            <CustomField
              name={optionalFieldName}
              label="Recommended software"
              width="w-[25rem]"
              tooltip="The name of the software recommended for opening and working with the file"
            />
          )}
        />
      </div>
      <ArrayField
        name={name}
        label="processing step"
        fieldName="metadata.processing_step"
        tooltip="List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            colorSchema="light"
            headline={`Processing step ${index + 1}`}
            tooltip="List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)"
          >
            <DataProcessingStep name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default RawMeasurementFile;
