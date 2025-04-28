import React from "react";
import ArrayField from "../buildingBlocks/ArrayField";
import OptionField from "../buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import DataFitting from "./DataFitting";
import FormWrapper from "../buildingBlocks/FormWrapper";
import DataProcessingStep from "./DataProcessingStep";
import OptionalField from "../buildingBlocks/OptionalField";
import CreateOptions from "../buildingBlocks/CreateOptions";

function DataAnalysis({ name }) {
  const { values } = useFormikContext();

  const tooltips = {
    measurements: "Measurements that were analyzed together",
    results:
      "Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters",
    dataFitting:
      "The details of how data fitting of the data to obtain the result was performed",
    dataProcessing:
      "Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying data filter, placing data at same start time etc. )",
  };

  const resultOptions = CreateOptions(
    getIn(values, "metadata.general_parameters.results"),
    "Select Result, if applicable"
  );

  const measurementOptions = CreateOptions(
    getIn(values, "metadata.method_specific_parameters.measurements"),
    "Select Measurement, if applicable"
  );

  return (
    <>
      <div className="flex">
        <div className="mr-3 -mt-3">
          <ArrayField
            name={name}
            label="Measurement"
            fieldName="measurements"
            tooltip={tooltips.measurements}
            renderChild={({ arrayName, index }) => (
              <OptionField
                name={`${arrayName}.${index}`}
                label={`Measurement ${index + 1}`}
                options={measurementOptions}
                tooltip={tooltips.measurements}
              />
            )}
          />
        </div>
        <div className="-mt-3">
          <ArrayField
            name={name}
            label="Result"
            fieldName="results"
            tooltip={tooltips.results}
            renderChild={({ arrayName, index }) => (
              <OptionField
                name={`${arrayName}.${index}`}
                label={`Result ${index + 1}`}
                options={resultOptions}
                tooltip={tooltips.results}
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Data fitting"
          fieldName="data_fitting"
          tooltip={tooltips.dataFitting}
          renderChild={({ optionalFieldName }) => (
            <FormWrapper
              colorSchema="light"
              headline="Data fitting"
              tooltip={tooltips.dataFitting}
            >
              <DataFitting name={optionalFieldName} />
            </FormWrapper>
          )}
        />
      </div>
      <ArrayField
        name={name}
        label="Data processing"
        fieldName="data_processing"
        tooltip={tooltips.dataProcessing}
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            colorSchema="light"
            headline={`Data processing step ${index + 1}`}
            tooltip={tooltips.dataProcessing}
          >
            <DataProcessingStep name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default DataAnalysis;
