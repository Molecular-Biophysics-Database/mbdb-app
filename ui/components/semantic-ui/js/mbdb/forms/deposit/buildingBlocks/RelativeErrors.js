import React from "react";
import { useField, useFormikContext } from "formik";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function RelativeErrors({ name, required, disabled }) {
  const nameRelativeField = `${name}.is_relative`;
  const [field, meta] = useField(nameRelativeField);
  const { setFieldValue } = useFormikContext();

  const ErrorOptions = [
    { value: true, label: "Yes" },
    { value: false, label: "No" },
  ];

  const currentValue = field.value;

  const handleOnChange = (e) => {
    const selectedValue = e.target.value === "Yes";
    setFieldValue(nameRelativeField, selectedValue);
  };

  return (
    <div className="flex">
      <div className="rounded-lg relative border w-[12rem]">
        <FormControl fullWidth>
          <InputLabel>Errors are relative</InputLabel>
          <Select
            value={
              currentValue === true ? "Yes" : currentValue === false ? "No" : ""
            }
            label="Errors are relative"
            size="small"
            onChange={handleOnChange}
            disabled={disabled}
            error={meta.touched && !!meta.error}
            displayEmpty
          >
            {ErrorOptions.map((option, index) => (
              <MenuItem key={index} value={option.label}>
                {option.label}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </div>
      {required && (
        <div className="ml-1 text-accent">
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
      <div className="ml-1 -mt-1">
        <Tooltip
          title={
            <Typography style={{ color: "white", fontSize: 13 }}>
              True if the error values should be interpreted as relative errors
              (fractional uncertainty)
            </Typography>
          }
          arrow
        >
          <span>?</span>
        </Tooltip>
      </div>
    </div>
  );
}

export default RelativeErrors;
