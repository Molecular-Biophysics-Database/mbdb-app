import React from "react";
import TextField from "@material-ui/core/TextField";
import { useField } from "formik";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function CustomField({
  label,
  name,
  fieldName,
  type,
  tooltip,
  width,
  multiline,
  required,
  disabled,
}) {
  const nameCustomField =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta] = useField(nameCustomField);

  return (
    <>
      <div className="flex">
        <div className={`${width}`}>
          <TextField
            {...field}
            className={`rounded-lg p-2 text-16px ${width}`}
            sx={{
              "& .MuiInputLabel-root": { color: "#034459" }, //styles the label
              "& .MuiOutlinedInput-root": {
                "& > fieldset": { color: "#034459" },
              },
              borderColor: "#666666",
              color: "#034459",
              "&:hover": {
                borderColor: "#666666",
              },
            }}
            label={label}
            type={type}
            value={field.value !== undefined ? field.value : ""}
            disabled={disabled}
            variant="outlined"
            {...(multiline && { multiline: true })}
            size="small"
            error={meta.touched && !!meta.error}
          />
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
    </>
  );
}

export default CustomField;
