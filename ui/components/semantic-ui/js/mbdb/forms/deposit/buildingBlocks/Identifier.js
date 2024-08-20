import React, { useEffect } from "react";
import { useField } from "formik";
import { useFormikContext } from "formik";
import TextField from "@material-ui/core/TextField";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function Identifier({ name, label, disabled, required }) {
  const prefix = "orcid";
  const { setFieldValue } = useFormikContext();
  const nameCustomField = name;
  const [field, meta] = useField(nameCustomField);

  useEffect(() => {
    if (!field.value){
      setFieldValue(nameCustomField, `${prefix}:`)
    }

    if (field.value && !field.value.startsWith(`${prefix}:`)) {
      setFieldValue(nameCustomField, `${prefix}:${field.value}`);
    }
  }, [field.value, setFieldValue, nameCustomField, prefix]);

  return (
    <>
      <div className="flex">
        <div className="mr-3">
          <TextField
            className={`rounded-lg p-2 text-16px w-[17rem]`}
            label={label}
            value={field.value || ""}
            onChange={(e) => setFieldValue(nameCustomField, e.target.value)}
            disabled={disabled}
            variant="outlined"
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
        <div className="-ml-2 mr-1 -mt-1">
          <Tooltip
            title={
              <Typography style={{ color: "white", fontSize: 13 }}>
                Persistent personal identifiers, currently only ORCIDs are
                allowed
              </Typography>
            }
            arrow
          >
            <span>?</span>
          </Tooltip>
        </div>
      </div>
    </>
  );
}

export default Identifier;
