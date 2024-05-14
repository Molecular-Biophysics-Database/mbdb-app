import ArrayField from "../buildingBlocks/ArrayField";
import OptionField from "../buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import DataFitting from "./DataFitting";
import FormWrapper from "../buildingBlocks/FormWrapper";
import DataProcessingStep from "./DataProcessingStep";
import OptionalField from "../buildingBlocks/OptionalField";
import CreateOptions from "../buildingBlocks/CreateOptions";

function DataAnalysis( { name } ) {

    const { values } = useFormikContext();

    const resultValue = getIn(values, 'metadata.general_parameters.results');
    const resultOptions = CreateOptions(resultValue, 'Select Result, if applicable');
    
    const measurementValue = getIn(values, 'metadata.method_specific_parameters.measurements');
    const measurementOptions = CreateOptions(measurementValue, 'Select Measurement, if applicable');

  return (
    <>
        <div className="flex">
            <div className="mr-3 -mt-3">
                <ArrayField
                    name={name}
                    label='Measurement'
                    fieldName='measurements'
                    tooltip='List of measurement links that was analyzed together'
                    renderChild={({ arrayName, index }) => (
                        <div>
                            <OptionField
                                name={`${arrayName}.${index}`}
                                label={`Measurement ${index + 1}`}
                                options={measurementOptions}
                                tooltip='List of measurement links that was analyzed together'
                            />
                        </div>
                    )}
                />
            </div>
            <div className="-mt-3">
                <OptionalField
                    name={name}
                    label='Result'
                    fieldName='result'
                    tooltip='Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <OptionField
                                name={optionalFieldName}
                                label='Result'
                                options={resultOptions}
                                tooltip='Link to the result(s) that was obtained by the data analysis. The link is to the results defined in the general parameters'
                            />
                        </div>
                    )}
                />
            </div>
        </div>
        <div className="mb-3">
            <OptionalField
                name={name}
                label='Data fitting'
                fieldName='data_fitting'
                tooltip='The details of how data fitting of the data to obtain the result was performed'
                renderChild={({ optionalFieldName }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline='Data fitting'
                        tooltip='The details of how data fitting of the data to obtain the result was performed'
                    >
                        <DataFitting
                            name={optionalFieldName}
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
                tooltip='Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying data filter, placing data at same start time etc. )'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`Data processing step ${index + 1}`}
                        tooltip='Describe the steps in the data analysis prior to fitting (removing outliers in the raw data, applying data filter, placing data at same start time etc. )'
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