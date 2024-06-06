import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import RawMeasurementFile from "../rawMeasurementFiles/RawMeasurementFile";
import UseDefault from "../../buildingBlocks/UseDefault";
import { useFormikContext, getIn } from "formik";
import { Button } from "semantic-ui-react";

// There are completely separate end points for submitting record's metadata and for submitting files
// therefore it will not be possible to just send file related things as part of record's metadata
// my advice is to treat the files section as a separate form, with its own formik provider, that will
// hold the information about the files and their metadata. Then when you wish to save
// (both record's metadata and its files), you can call save() (note that save must be taken from top formik provider)
// and you can also call submitFiles function right after that will save the files

async function SubmitFile(file, recordMetadata) {
  if (!file) return { code: 400, errors: ["No file selected."] };

  const fileName = file.name;

  // Submit the file name
  let resp = await fetch(recordMetadata?.links?.files, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify([{ key: file.key, metadata: file.metadata }]),
  });

  if (!resp.ok) {
    return {
      code: resp.status,
      errors: [`Failed to submit file "${fileName}": ${resp.statusText}`],
    };
  }

  const response = await resp.json();
  const fileObject = response.entries.find((f) => f.key === file.key);
  // Upload the file content
  resp = await fetch(fileObject.links.content, {
    method: "PUT",
    headers: {
      "Content-Type": "application/octet-stream",
    },
    body: file,
  });

  if (!resp.ok) {
    return {
      code: resp.status,
      errors: [
        `Failed to upload content of file "${fileName}": ${resp.statusText}`,
      ],
    };
  }

  // Commit the result
  resp = await fetch(fileObject.links.commit, {
    method: "POST",
  });

  if (!resp.ok) {
    return {
      code: resp.status,
      errors: [
        `Failed to commit uploaded file "${fileName}": ${resp.statusText}`,
      ],
    };
  }

  return void 0;
}

function RawMeasurementFilesTab({ name, save, recordMetadata }) {
  const fieldName = "raw_measurement_files";

  UseDefault(name, [{}]);
  const { values } = useFormikContext();
  const files = getIn(values, files);
  const submitFiles = async () => {
    console.log(files);
    const filesList = files.files;
    filesList.forEach(async (file, index) => {
      const response = await SubmitFile(file, recordMetadata);
    });
  };

  return (
    <>
      {/* just for testing purposes */}
      <Button primary onClick={() => submitFiles()}>
        Submit files
      </Button>
      <div className="-mt-3">
        <ArrayField
          name={name}
          label="Raw measurement file"
          required={true}
          //   fieldName={fieldName}
          tooltip="List of file(s) containing the raw measurements"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Raw measurement file ${index + 1}`}
              tooltip="List of file(s) containing the raw measurements"
            >
              <div>
                <RawMeasurementFile
                  name={`${arrayName}.${index}`}
                  index={index}
                  save={save}
                />
              </div>
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}

export default RawMeasurementFilesTab;
