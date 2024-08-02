import React from "react";
import { useField } from "formik";
import { useFormikContext } from "formik";
import { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function ExternalDatabaseField({
  name,
  fieldName,
  prefixTooltip,
  dbTooltip,
  disabled,
}) {
  const nameCustomField =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta] = useField(nameCustomField);
  const { setFieldValue } = useFormikContext();

  const [prefixValue, setPrefixValue] = useState("");
  const [externalDbValue, setExternalDbValue] = useState(field.value || "");

  const updateCombinedValue = (newPrefixValue, newExternalDbValue) => {
    const combinedValue = `${newPrefixValue}:${newExternalDbValue}`;
    console.log(combinedValue, "Combined value");
    setFieldValue(nameCustomField, combinedValue);
  };

  const handlePrefixChange = (e) => {
    const valuePrefix = e.target.value;
    setPrefixValue(valuePrefix);
    updateCombinedValue(valuePrefix, externalDbValue);
  };

  const handleExternalDbChange = (e) => {
    const valueExternalDb = e.target.value;
    setExternalDbValue(valueExternalDb);
    updateCombinedValue(prefixValue, valueExternalDb);
  };

  const setPrefix = (prefix) => {
    setPrefixValue(prefix);
    updateCombinedValue(prefix, externalDbValue);
  };

  return (
    <>
      <div className="flex mb-3 mt-2">
        <button
          onClick={() => setPrefix("pdb")}
          className="uppercase flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
        >
          Pdb
        </button>

        <button
          onClick={() => setPrefix("uniprot")}
          class="uppercase flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
        >
          Uniprot
        </button>
      </div>
      <div className="flex">
        <div className="w-[30%] mr-3">
          <TextField
            {...field}
            id="prefix"
            className={`rounded-lg p-2 text-16px w-full`}
            label="Prefix"
            value={prefixValue}
            onChange={handlePrefixChange}
            disabled={disabled}
            variant="outlined"
            size="small"
            error={meta.touched && !!meta.error}
          />
        </div>
        {prefixTooltip && (
          <div className="-ml-2 mr-1 -mt-1">
            <Tooltip
              title={
                <Typography style={{ color: "white", fontSize: 13 }}>
                  {prefixTooltip}
                </Typography>
              }
              arrow
            >
              <span>?</span>
            </Tooltip>
          </div>
        )}
        <div className="w-[70%]">
          <TextField
            {...field}
            id="external_database"
            className={`rounded-lg p-2 text-16px w-full`}
            label="External database"
            value={externalDbValue}
            onChange={handleExternalDbChange}
            disabled={disabled}
            variant="outlined"
            size="small"
            error={meta.touched && !!meta.error}
          />
        </div>
        {dbTooltip && (
          <div className="ml-1 -mt-1">
            <Tooltip
              title={
                <Typography style={{ color: "white", fontSize: 13 }}>
                  {dbTooltip}
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

export default ExternalDatabaseField;
