import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import RawMeasurementFile from "../rawMeasurementFiles/RawMeasurementFile";
import { useFormikContext, getIn } from "formik";
import { Button } from "semantic-ui-react";
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

async function fetchMetadata(file) {
  const response = await fetch(file.links.self, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error(`Failed to replace file: ${response.statusText}`);
  }
  const res = await response.json();

  return res;
}

function RawMeasurementFilesTab({ name, save, recordMetadata }) {
  const { values, setFieldValue } = useFormikContext();

  const files = getIn(values, files);

  const submitFiles = async () => {
    console.log(files, "Files");
    const filesList = files.files;
    const filesStatus = [];
    filesList.forEach(async (file, index) => {
      if (!file.file_id) {
        const response = await SubmitFile(file, recordMetadata);
        filesStatus.push(response);
        setFieldValue("files", filesStatus);
      } else {
        const metadataObject = await fetchMetadata(file);
        const initialMetadata = metadataObject.metadata;
        console.log(initialMetadata, "Initial metadata");
        console.log(file.metadata, "File metasatjfdklsjfkldsjklfs");
        //const initialValue = initialValues.files.find(f => (f.key === file.key));
        if (!_isEqual(initialMetadata, file.metadata)) {
          const modifiedFile = await replaceMetadata(file);
          filesStatus.push(modifiedFile);
          console.log(filesStatus, "Fileejksjfkdlsjfkldsjk");
          setFieldValue("files", filesStatus);
        } else {
          filesStatus.push(file);
          setFieldValue("files", filesStatus);
        }
      }
      console.log(filesStatus, "Files status");
    });
  };

  const handleDeleteFile = async (file) => {
    console.log(file, "Filee");
    try {
      const response = await deleteFile(file);
      console.log(response, "Response deleted file");
      if (response.status === 204) {
        const newFiles = values.files.filter((f) => f.key !== file.key);
        console.log(newFiles, "NewFiles");
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
      {/* just for testing purposes */}
      <Button
        primary
        style={{ backgroundColor: "grey", color: "white" }}
        onClick={() => submitFiles()}
      >
        Submit files
      </Button>
      <div className="-mt-3">
        <ArrayField
          name={name}
          label="Raw measurement file"
          required={true}
          //  fieldName={fieldName}
          tooltip="List of file(s) containing the raw measurements"
          renderChild={({ arrayName, index, item: file }) => (
            <FormWrapper
              headline={`Raw measurement file ${index + 1}`}
              tooltip="List of file(s) containing the raw measurements"
            >
              <div>
                <RawMeasurementFile
                  file={file}
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

export default RawMeasurementFilesTab;
