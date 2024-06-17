import React from "react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import { useFormikContext, useField } from "formik";

function FileField({
  name,
  fieldName,
  tooltip,
  required,
  index,
  save,
  onDeleteFile,
  file,
}) {
  const nameCustomField =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [meta] = useField(nameCustomField);
  const { values, setFieldValue } = useFormikContext();
  //console.log(index);
  const handleOnClick = () => {
    if (!values.id) {
      save(true);
    }
  };

  const handleChange = (e) => {
    let file = e.target.files[0];
    if (file) {
      setFieldValue(`${name}.metadata.size`, file.size);
      setFieldValue(`${name}.metadata.name`, file.name);
      setFieldValue(`${name}.${fieldName}`, file.name);
      handleFileContent(file);
    }
  };

  const handleFileContent = async (file) => {
    // Use FileReader API to read the file content
    const reader = new FileReader();

    reader.onload = (e) => {
      const fileContent = e.target.result;

      // Now you can save or process `fileContent` as needed
      console.log(fileContent); // Example: log file content to console
      // You can save `fileContent` in Formik state, pass it to another function, or use it directly

      // Example: Setting file content in Formik state
      setFieldValue(`${name}.fileContent`, fileContent);
    };

    reader.readAsDataURL(file); // Use readAsArrayBuffer or other methods as per your requirement
  };

  const handleClear = async () => {
    if (file.file_id) {
      try {
        await onDeleteFile(file);
      } catch (error) {
        console.error("Error deleting file:", error);
      }
    } else {
      const newFiles = values.files.filter((f) => f.key !== file.key);
      if (newFiles.length === 0) {
        setFieldValue("files", [{}]);
      } else {
        setFieldValue("files", newFiles);
      }
    }
  };

  return (
    <div className="flex">
      <div>
        {file?.key ? (
          <div className="flex items-center">
            <span className="rounded-normal font-JostMedium bg-dark text-white p-3 text-16px">
              {file?.key}
            </span>
            <button
              type="button"
              className="ml-2 p-3 bg-accent font-JostMedium text-white rounded-normal"
              onClick={handleClear}
            >
              Remove file
            </button>
          </div>
        ) : (
          <div className="flex">
            <label
              htmlFor={`${name}.file-upload`}
              className="rounded-normal font-JostMedium bg-dark text-white p-3 text-16px"
            >
              Choose file
            </label>
            <input
              // very important must not hard code an id for element in an array. There must
              // not be duplicate ids in the DOM, it causes weird bugs
              id={`${name}.file-upload`}
              type="file"
              className="hidden"
              onChange={(e) => handleChange(e, index)}
              onClick={handleOnClick}
              size="small"
              error={meta.touched && !!meta.error}
            />
          </div>
        )}
      </div>
      {required && (
        <div className="text-accent ml-1">
          <Tooltip
            title={
              <Typography fontSize={13}>
                This field is required and cannot be left blank or unset
              </Typography>
            }
            arrow
          >
            <span>*</span>
          </Tooltip>
        </div>
      )}
      {tooltip && (
        <div className="ml-1 -mt-1">
          <Tooltip
            title={<Typography fontSize={13}>{tooltip}</Typography>}
            arrow
          >
            <span>?</span>
          </Tooltip>
        </div>
      )}
    </div>
  );
}

export default FileField;
