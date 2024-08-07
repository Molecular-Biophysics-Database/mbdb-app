import React from "react";
import { useField } from "formik";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function DynamicOptionField({
  label,
  name,
  fieldName,
  options,
  width,
  tooltip,
  required,
  disabled,
}) {
  const [field, meta, helpers] = useField(name);

  const currentObject = field.value.type;

  const currentValue =
    field.value && typeof field.value === "object"
      ? field.value[fieldName]
      : "";

  //console.log(currentValue, "Current value");
  return (
    <div className="flex">
      <div className={`${width} rounded-lg relative border min-w-[178px]`}>
        <FormControl fullWidth>
          <InputLabel>{label}</InputLabel>
          <Select
            {...field}
            value={currentValue || field.value}
            onChange={(event) => {
              const selectedValue = event.target.value;
              const selectedOption = options.find(
                (option) => option.value === selectedValue
              );

              if (selectedValue) {
                if (fieldName === "type") {
                  if (selectedOption.value !== currentValue) {
                    helpers.setValue({
                      [fieldName]: selectedOption.value,
                      id: selectedOption.id,
                    });
                  }
                } else {
                  if (selectedOption.value !== currentValue) {
                    helpers.setValue({
                      [fieldName]: selectedOption.value,
                      id: selectedOption.id,
                      type: currentObject,
                    });
                  }
                }
              }
            }}
            label={label}
            size="small"
            disabled={disabled}
            error={meta.touched && !!meta.error}
          >
            {options.map((option, index) => (
              <MenuItem key={index} value={option.value} id={option.id}>
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

export default DynamicOptionField;
