import React, { useState, useEffect } from "react";
import { useField } from "formik";
import { useFormikContext } from "formik";
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

  // Split the initial combined value into prefix and external database values
  const initialCombinedValue = field.value || "";
  const initialPrefix = initialCombinedValue.split(":")[0] || "";
  const initialExternalDb = initialCombinedValue.split(":")[1] || "";

  const [prefixValue, setPrefixValue] = useState(initialPrefix);
  const [externalDbValue, setExternalDbValue] = useState(initialExternalDb);

  useEffect(() => {
    // Update the state when the combined value changes
    const combinedValue = `${prefixValue}:${externalDbValue}`;
    setFieldValue(nameCustomField, combinedValue);
  }, [prefixValue, externalDbValue, setFieldValue, nameCustomField]);

  const handlePrefixChange = (e) => {
    setPrefixValue(e.target.value);
  };

  const handleExternalDbChange = (e) => {
    setExternalDbValue(e.target.value);
  };

  const setPrefix = (prefix) => {
    setPrefixValue(prefix);
  };

  return (
    <>
      <div className="flex mb-3 mt-2">
        <button
          onClick={() => setPrefix("pdb")}
          className="uppercase flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
        >
          PDB
        </button>

        <button
          onClick={() => setPrefix("uniprot")}
          className="uppercase flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
        >
          UniProt
        </button>
      </div>
      <div className="flex">
        <div className="w-[30%] mr-3">
          <TextField
            id="external_database"
            className={`rounded-lg p-2 text-16px w-full`}
            label="External database"
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
            id="ID"
            className={`rounded-lg p-2 text-16px w-full`}
            label="ID"
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
