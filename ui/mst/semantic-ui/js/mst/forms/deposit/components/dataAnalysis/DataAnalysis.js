import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import DataFitting from "./DataFitting";
import FColdAndHot from "./FColdAndHot";
import ArrayField from "../buildingBlocks/ArrayField";
import DataProcessingStep from "./DataProcessingStep";
import OptionField from "../buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import UseDefault from "../buildingBlocks/UseDefault";

function DataAnalysis( { name } ) {

    const { values } = useFormikContext();

    const fieldNameResults = 'results'
    UseDefault(values, `${name}.${fieldNameResults}`, [{}] );
      
    const resultsValue = getIn(values, `metadata.general_parameters.results`)

    let resultOptions = [];

    if (resultsValue && resultsValue.length > 0) {
        resultOptions = resultsValue.map(result => ({
            value: result.name,
            label: result.name,
        }));
    } else {
        resultOptions = [{ label: 'Select Result, if applicable' }];
    }

    const measurementsValue = getIn(values, `metadata.method_specific_parameters.measurements`)

    let measurementOptions = [];

    if (measurementsValue && measurementsValue.length > 0) {
        measurementOptions = measurementsValue.map(result => ({
            value: result.name,
            label: result.name,
        }));
    } else {
        measurementOptions = [{ label: 'Select Measurement, if applicable' }];
    }

  return (
    <>
        <div className='flex mb-3'>
            <div className="-mt-3">
                <ArrayField
                    name={name}
                    label='Result'
                    fieldName={fieldNameResults}
                    required={true}
                    tooltip='Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters'
                    renderChild={({ arrayName, index }) => (
                        <OptionField
                            name={`${arrayName}.${index}`}
                            options={resultOptions}
                            label={`Result ${index + 1}`}
                            tooltip='Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters'
                        />
                    )}
                />
            </div>
          <div>
            <OptionField
                name={name}
                options={measurementOptions}
                label='Measurement'
                fieldName='measurement'
                tooltip='List of the measurements that was analyzed together for a specific parameter'
            />
          </div>
        </div>
        <div className="mb-3">
            <ArrayField
                name={name}
                label='F cold and hot'
                fieldName='f_cold_and_hot'
                maxItems={1}
                tooltip='If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`F cold and hot`}
                        tooltipHeader='If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here'
                    >
                        <FColdAndHot
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div className="mb-3">
            <ArrayField
                name={name}
                label='Data fitting'
                fieldName='data_fitting'
                maxItems={1}
                tooltip='If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`Data fitting`}
                        tooltipHeader='If the data was analyzed with time windows corresponding to fluorescence before and after an IR laser was heating the sample the edges of the time windows can be specified here'
                    >
                        <DataFitting
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Data processing step'
                fieldName='data_processing_step'
                tooltip='Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying smoothing filters, etc.)'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`Data processing step ${index + 1}`}
                        tooltipHeader='Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying smoothing filters, etc.)'
                    >
                        <DataProcessingStep
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default DataAnalysis;