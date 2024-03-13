import React from "react";
import CustomField from "../buildingBlocks/CustomField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import OptionField from "../buildingBlocks/OptionField";

function RawDataFiles( { name } ) {

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

  return (
    <>
      <FormWrapper headline='Raw data files'>
        <div className="mb-3">
          <CustomField
            name={name}
            type='file'
            fieldName='file'
            width='w-[25rem]'
          />
        </div>
        <div className="mb-3">
          <CustomField
            name={name}
            fieldName='name'
            label='Name'
            width='w-[25rem]'
            tooltip='Name of the file'
          />
        </div>
        <div className="mb-3">
          <OptionField
            name={name}
            fieldName='context'
            options={contextOptions}
            label='Context'
            width='w-[25rem]'
            tooltip='The context the file should be understood within (e.g. raw measurement data)'
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
          <CustomField
            name={name}
            fieldName='description'
            label='description'
            width='w-[25rem]'
            tooltip='Short description of what the file contains'
          />
        </div>
        <div className="mb-3">
          <CustomField
            name={name}
            fieldName='recommended_software'
            label='Recommended software'
            width='w-[25rem]'
            tooltip='The name of the software recommended for opening and working with the file'
          />
        </div>
        <div className="mb-3">
          <CustomField
            name={name}
            fieldName='processing_steps'
            label='Processing steps'
            width='w-[25rem]'
            tooltip='List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)'
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default RawDataFiles;