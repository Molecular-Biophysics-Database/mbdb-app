import CustomField from "../../buildingBlocks/CustomField";
import OptionField from "../../buildingBlocks/OptionField";
import ArrayField from "../../buildingBlocks/ArrayField";
import DataProcessingStep from "../../sharedComponents/DataProcessingStep";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionalField from "../../buildingBlocks/OptionalField";
import FileField from "../../buildingBlocks/FileField";

function RawDataFile( { name } ) {

  const originatesFromOptions = [
    { value: 'Instrument software', label: 'Instrument software' },
    { value: 'User', label: 'User' },
    { value: 'MBDB', label: 'MBDB' },
  ];

  const contextOptions = [
    { value: 'Raw measurement data', label: 'Raw measurement data' },
    { value: 'Derived measurement data', label: 'Derived measurement data' },
    { value: 'Quality control report', label: 'Quality control report' },
  ];

  const contentTypeOptions = [
    { value: 'Text', label: 'Text' },
    { value: 'Binary', label: 'Binary' },
    { value: 'Text and binary', label: 'Text and binary' },
  ];

  return (
    <>
        <div className="mb-3">
          <FileField
            name={name}
            type='file'
            fieldName='file'
            width='w-[25rem]'
          />
        </div>
        <div className="mb-3">
          <OptionField
            name={name}
            options={originatesFromOptions}
            label='Originates from'
            fieldName='originates_from'
            width='w-[25rem]'
            tooltip='What is the source of the file'
          />
        </div>
        <div className="mb-3">
          <OptionalField
              name={name}
              label='Context'
              fieldName='context'
              tooltip='The context the file should be understood within (e.g. raw measurement data)'
              renderChild={({ optionalFieldName }) => (
                <OptionField
                  name={optionalFieldName}
                  options={contextOptions}
                  label='Context'
                  width='w-[25rem]'
                  tooltip='The context the file should be understood within (e.g. raw measurement data)'
                />
              )}
          />
        </div>
        <div className="mb-3">
          <OptionalField
              name={name}
              label='Content type'
              fieldName='content_type'
              tooltip='Type of the file content in terms of how it can be read (text, binary, etc.)'
              renderChild={({ optionalFieldName }) => (
                <OptionField
                  name={optionalFieldName}
                  options={contentTypeOptions}
                  label='Content type'
                  width='w-[25rem]'
                  tooltip='Type of the file content in terms of how it can be read (text, binary, etc.)'
                />
              )}
          />
        </div>
        <div className="mb-3">
          <OptionalField
              name={name}
              label='Description'
              fieldName='description'
              tooltip='Short description of what the file contains'
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label='description'
                  width='w-[25rem]'
                  tooltip='Short description of what the file contains'
                />
              )}
          />
        </div>
        <div>
          <OptionalField
              name={name}
              label='Recommended software'
              fieldName='recommended_software'
              tooltip='The name of the software recommended for opening and working with the file'
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label='Recommended software'
                  width='w-[25rem]'
                  tooltip='The name of the software recommended for opening and working with the file'
                />
              )}
          />
        </div>
        <ArrayField
          name={name}
          label='processing step'
          fieldName='processing_step'
          tooltip='List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)'
          renderChild={({ arrayName, index }) => (
              <FormWrapper
                  colorSchema='light'
                  headline={`Processing step ${index + 1}`}
                  tooltip='List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)'
              >
                  <DataProcessingStep
                      name={`${arrayName}.${index}`}
                  />
              </FormWrapper>
          )}
        />
    </>
  );
}

export default RawDataFile;