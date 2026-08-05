import React, { forwardRef, useImperativeHandle, useEffect, useState } from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "../../buildingBlocks/ArrayFieldCopyPaste";
import RawMeasurementFile from "../rawMeasurementFiles/RawMeasurementFile";
import { useFormikContext, getIn } from "formik";
import _isEqual from "lodash/isEqual";
import Spinner from "../../buildingBlocks/Spinner";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

// There are completely separate end points for submitting record's metadata and for submitting files
// therefore it will not be possible to just send file related things as part of record's metadata
// my advice is to treat the files section as a separate form, with its own formik provider, that will
// hold the information about the files and their metadata. Then when you wish to save
// (both record's metadata and its files), you can call save() (note that save must be taken from top formik provider)
// and you can also call submitFiles function right after that will save the files

function remapFileErrors(errors, index) {
  return errors.map((error) => ({
    ...error,
    field: error.field?.startsWith("0.")
      ? error.field.replace(/^0\./, `${index}.`)
      : error.field,
  }));
}

const MULTIPART_LIMIT = 20 * 1024 * 1024;
const PART_SIZE = 10 * 1024 * 1024;
const PART_UPLOAD_CONCURRENCY = 4;

async function uploadPart(partLink, browserFile, fileName) {
  const partNumber = partLink.part;
  const start = (partNumber - 1) * PART_SIZE;
  const end = Math.min(start + PART_SIZE, browserFile.size);
  const blobPart = browserFile.slice(start, end);

  const partResp = await fetch(partLink.url, {
    method: "PUT",
    headers: {
      "Content-Type": "application/octet-stream",
    },
    body: blobPart,
  });

  if (!partResp.ok) {
    const error = new Error(
      `Failed to upload part ${partNumber} of file "${fileName}": ${partResp.statusText}`
    );
    error.status = partResp.status;
    throw error;
  }
}

// Uploads parts of a single file concurrently (bounded pool), instead of one at a time,
// since sequential PUTs left most of the upload time waiting on round-trips rather than transferring data.
async function uploadPartsConcurrently(partLinks, browserFile, fileName) {
  const queue = [...partLinks];
  let firstError = null;

  async function worker() {
    while (queue.length && !firstError) {
      const partLink = queue.shift();
      try {
        await uploadPart(partLink, browserFile, fileName);
      } catch (error) {
        if (!firstError) firstError = error;
      }
    }
  }

  const workerCount = Math.min(PART_UPLOAD_CONCURRENCY, partLinks.length);
  await Promise.all(Array.from({ length: workerCount }, worker));

  return firstError;
}

async function SubmitFile(file, recordMetadata, setIsPending) {
  if (!file) return { code: 400, errors: ["No file selected."] };
  setIsPending(true);

  const fileName = file.name;

  const browserFile = file.fileContent;
  const useMultipart = browserFile.size > MULTIPART_LIMIT;
  const parts = Math.ceil(browserFile.size / PART_SIZE);

  const payload = {
    key: file.key,
    metadata: file.metadata || {},
  };

  if (useMultipart) {
    payload.size = browserFile.size;
    payload.transfer = {
      type: "M",
      parts: parts,
      part_size: PART_SIZE,
    };
  }

// Submit the file name
  let resp = await fetch(recordMetadata?.links?.files, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify([payload]),
  });

  const data = await resp.json().catch(() => null);

  if (!resp.ok) {
    setIsPending(false);
    return {
      code: resp.status,
      message: data?.message || `Failed to submit file "${file.name}"`,
      errors: data?.errors || [],
      raw: data,
    };
  }

  const fileObject = data.entries.find((f) => f.key === file.key);

  // Upload the file content
  if (useMultipart) {
    const partLinks = fileObject.links?.parts;

    if (!partLinks || !partLinks.length) {
      setIsPending(false);
      return {
        code: 500,
        errors: [
          `Multipart upload was requested, but no part links were returned for "${fileName}".`,
        ],
      };
    }

    const partError = await uploadPartsConcurrently(
      partLinks,
      browserFile,
      fileName
    );

    if (partError) {
      setIsPending(false);
      return {
        code: partError.status || 500,
        errors: [partError.message],
      };
    }
  } else {
    resp = await fetch(fileObject.links.content, {
      method: "PUT",
      headers: {
        "Content-Type": "application/octet-stream",
      },
      body: browserFile,
    });

    if (!resp.ok) {
      setIsPending(false);
      return {
        code: resp.status,
        errors: [
          `Failed to upload content of file "${fileName}": ${resp.statusText}`,
        ],
      };
    }
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

  setIsPending(false);

  // update the page to place values in inside the form case extraction took place
  // also serves signal to let the user know that file uploading has completed
  //setTimeout(() => {
  //  window.location.href = "/";
  //}, 1500); // 1.5 seconds delay
  //window.location.reload();
  return {
    code: resp.status,
    data: res,
  };
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
  ({ name, save, recordMetadata, setFileUploadErrors }, ref) => {
    const { values, setFieldValue } = useFormikContext();
    const [isPending, setIsPending] = useState(false);

    UseDefault(name, [{ key: "" }]);
    const files = getIn(values, name);

    useEffect(() => {
      if (isPending) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "";
      }

      return () => {
        document.body.style.overflow = "";
      };
    }, [isPending]);

    //console.log(ref);
    const submitFiles = async () => {
      setFileUploadErrors([]);
      setIsPending(false);

      const filesList = files;
      const filesStatus = [];
      const allErrors = [];

      // before submitting one fetch to fetch current status of files from the server
      const serverFilesState = await fetch(recordMetadata?.links?.files).then(
        (response) => response.json()
      );
      const uploadedFilesKeys = serverFilesState?.entries.map(
        (file) => file.key
      );
      // forEach was introduced before async await, so async await does not work very well
      // with it. Using for of instead
      for (const [index, file] of filesList.entries()) {
        // If file has no key it cannot be uploaded so pass
        if (!file?.key) {
          continue;
        }
        if (!uploadedFilesKeys.includes(file.key)) {
          // if file with such key does not exist on the server upload it and its metadata
          const response = await SubmitFile(file, recordMetadata, setIsPending);

          if (response?.errors?.length) {
            allErrors.push(...remapFileErrors(response.errors, index));
            filesStatus.push(file);
            continue;
          }

          if (response?.data) {
            filesStatus.push(response.data);
          }
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
  
      setFileUploadErrors(allErrors);
      setFieldValue("files", filesStatus);
    };
    //console.log(ref);
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

        {isPending && (
          <div className="fixed inset-0 flex flex-col items-center justify-center bg-zinc-900 bg-opacity-50 z-[200]">
            <Spinner />
            <h2 className="text-primary mt-4">Saving metadata and files..</h2>
          </div>
        )}

        <div className="mb-3 w-fit">
          <FormWrapper>
            Information about the file(s) containing the raw data. Maximum number of uploaded files is 255.
          </FormWrapper>
        </div>
        <div>
          <ArrayFieldCopyPaste
            name={name}
            label="Raw measurement file"
            required
            method="file"
            initialValue={{ key: "" }}
            tooltip="List of file(s) containing the raw measurements"
            renderChild={({ arrayName, index, item: file }) => (
              <FormWrapper
                headline={`Raw measurement file ${index + 1}`}
                tooltip="List of file(s) containing the raw measurements"
                name={`${name}.enabled`}
              >
                <RawMeasurementFile
                  file={file}
                  key={index}
                  name={`${arrayName}.${index}`}
                  index={index}
                  save={save}
                  onDeleteFile={handleDeleteFile}
                />
              </FormWrapper>
            )}
          />
        </div>
      </>
    );
  }
);

export default RawMeasurementFilesTab;
