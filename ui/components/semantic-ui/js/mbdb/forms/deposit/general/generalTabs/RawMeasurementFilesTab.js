import React, { forwardRef, useImperativeHandle } from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import RawMeasurementFile from "../rawMeasurementFiles/RawMeasurementFile";
import { useFormikContext, getIn } from "formik";
import _isEqual from "lodash/isEqual";

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
    body: file.fileContent,
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

  const res = await resp.json();

  return res;
}

async function deleteFile(file) {
  const response = await fetch(file.links.self, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`Failed to delete file: ${response.statusText}`);
  }

  return response;
}

async function replaceMetadata(file) {
  const response = await fetch(file.links.self, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      metadata: file.metadata,
    }),
  });

  if (!response.ok) {
    throw new Error(`Failed to replace file: ${response.statusText}`);
  }
  const res = await response.json();

  return res;
}

const RawMeasurementFilesTab = forwardRef(
  ({ name, save, recordMetadata }, ref) => {
    const { values, setFieldValue } = useFormikContext();
    const files = getIn(values, name);
    console.log(ref);
    const submitFiles = async () => {
      const filesList = files;
      const filesStatus = [];
      // before submitting one fetch to fetch current status of files from the server
      const serverFilesState = await fetch(recordMetadata?.links?.files).then(
        (response) => response.json()
      );
      const uploadedFilesKeys = serverFilesState?.entries.map(
        (file) => file.key
      );
      // forEach was introduced before async await, so async await does not work very well
      // with it. Using for of instead
      for (const file of filesList) {
        // If file has no key it cannot be uploaded so pass
        if (!file?.key) {
          continue;
        }
        if (!uploadedFilesKeys.includes(file.key)) {
          // if file with such key does not exist on the server upload it and its metadata
          const response = await SubmitFile(file, recordMetadata);
          filesStatus.push(response);
        } else if (
          // if file with such key exits, but it has different metadata than the one
          // on the server make put to replace the metadata
          uploadedFilesKeys.includes(file.key) &&
          !_isEqual(
            file.metadata,
            serverFilesState.entries.find((f) => f.key === file.key).metadata
          )
        ) {
          const modifiedFile = await replaceMetadata(file);
          filesStatus.push(modifiedFile);
        } else {
          // else just put the file object into the array
          filesStatus.push(file);
        }
      }

      setFieldValue("files", filesStatus);
    };
    console.log(ref);
    useImperativeHandle(ref, () => ({
      submitFiles,
    }));

    const handleDeleteFile = async (file) => {
      try {
        const response = await deleteFile(file);
        if (response.status === 204) {
          const newFiles = values.files.filter((f) => f.key !== file.key);
          if (newFiles.length === 0) {
            setFieldValue("files", [{}]);
          } else {
            setFieldValue("files", newFiles);
          }
        }
      } catch (error) {
        console.error("Error deleting file:", error);
      }
    };

    return (
      <>
        {/* just for testing purposes 
          <Button
            primary
            style={{ backgroundColor: "#023850", color: "white" }}
            onClick={() => submitFiles()}
          >
            Submit files
          </Button>
        */}
        <div className="-mt-3">
          <ArrayField
            name={name}
            label="Raw measurement file"
            required
            initialValue={{ key: "" }}
            tooltip="List of file(s) containing the raw measurements"
            renderChild={({ arrayName, index, item: file }) => (
              <FormWrapper
                headline={`Raw measurement file ${index + 1}`}
                tooltip="List of file(s) containing the raw measurements"
              >
                <div>
                  <RawMeasurementFile
                    file={file}
                    key={index}
                    name={`${arrayName}.${index}`}
                    index={index}
                    save={save}
                    onDeleteFile={handleDeleteFile}
                  />
                </div>
              </FormWrapper>
            )}
          />
        </div>
      </>
    );
  }
);

export default RawMeasurementFilesTab;
