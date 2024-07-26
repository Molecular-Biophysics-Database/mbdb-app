import React from "react";
import TextField from "@material-ui/core/TextField";
import { useField } from "formik";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import FormWrapper from "./FormWrapper";

function SequenceField({
  label,
  name,
  fieldName,
  tooltip,
  width,
  required,
  disabled,
  colorSchema,
}) {
  const nameCustomField =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta] = useField(nameCustomField);

  return (
    <>
      <FormWrapper colorSchema={colorSchema}>
        <div className="flex mb-3">
          <div>
            <a
              class="flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
              href="https://www.uniprot.org/"
              target="_blank"
              rel="noreferrer"
            >
              Uniprot
            </a>
          </div>
          <div>
            <a
              class="flex justify-center py-1 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
              href="https://blast.ncbi.nlm.nih.gov/Blast.cgi"
              target="_blank"
              rel="noreferrer"
            >
              Blast
            </a>
          </div>
        </div>
        <div className="flex">
          <div className={`${width}`}>
            <TextField
              {...field}
              className={`rounded-lg p-2 text-16px ${width}`}
              label={label}
              value={field.value !== undefined ? field.value : ""}
              disabled={disabled}
              variant="outlined"
              multiline={true}
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
            <div className="ml-[2.5rem]">
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
      </FormWrapper>
    </>
  );
}

export default SequenceField;
