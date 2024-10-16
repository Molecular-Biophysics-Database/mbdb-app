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
      setFieldValue(`${name}.fileContent`, file);
      setFieldValue(`${name}.${fieldName}`, file.name);
    }
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
              <Typography style={{ color: "white", fontSize: 13 }}>
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
            title={
              <Typography style={{ color: "white", fontSize: 13 }}>
                {tooltip}
              </Typography>
            }
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
