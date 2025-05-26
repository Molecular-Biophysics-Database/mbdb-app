import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import DataFitting from "@mbdb_deposit/sharedComponents/DataFitting";
import FColdAndHot from "./FColdAndHot";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import DataProcessingStep from "@mbdb_deposit/sharedComponents/DataProcessingStep";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

function DataAnalysis({ name }) {
  const { values } = useFormikContext();

  const tooltips = {
    measurements:
      "List of the measurements that were analyzed together for a specific parameter",
    results:
      "Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters",
    fColdAndHot:
      "If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here",
    dataFitting:
      "If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here",
    dataProcessing:
      "Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying smoothing filters, etc.)",
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
      <div className="flex mb-3">
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
                options={resultOptions}
                label={`Result ${index + 1}`}
                tooltip={tooltips.results}
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="F cold and hot"
          fieldName="f_cold_and_hot"
          tooltip={tooltips.fColdAndHot}
          renderChild={({ optionalFieldName }) => (
            <FormWrapper
              colorSchema="light"
              headline="F cold and hot"
              tooltip={tooltips.fColdAndHot}
            >
              <FColdAndHot name={optionalFieldName} />
            </FormWrapper>
          )}
        />
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
