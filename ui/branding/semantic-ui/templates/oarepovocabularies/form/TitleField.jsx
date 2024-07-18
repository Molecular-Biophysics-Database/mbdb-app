import React from "react";
import { useField } from "formik";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import { useFormikContext } from "formik";

function TitleField({
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
    const { values } = useFormikContext();
  const nameCustomField =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta] = useField(nameCustomField);

  console.log(values, 'Valueesssssss');

  return (
    <>
      <div className="flex">
        <div className="w-full">
            <label htmlFor={label}>{label} </label>
          <input
            {...field}
            id={label}
            className={`rounded-lg p-2 text-16px ${width}`}
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

export default TitleField;
