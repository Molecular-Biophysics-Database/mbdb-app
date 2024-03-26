import React from 'react';
import CustomField from '../buildingBlocks/CustomField';

function DataProcessingStep( { name } ) {

  return (
    <>
        <div className='flex mb-3'>
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='name'
                    label='Name'
                    tooltip='Short descriptive name of the processing step'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='description'
                    label='Description'
                    tooltip='Description of what the processing step was'
                />
            </div>
        </div>
        <div className='flex'>
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='software_name'
                    label='Software name'
                    tooltip='The name of the software that was used for the step (e.g. Excel)'
                    />
            </div>
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='software_version'
                    label='Software version'
                    tooltip='The version of the software that was used for the step'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='link_to_source_code'
                    label='Link to source code'
                    tooltip='If processing was performed with software where the source code is legally available a link can be specified here (e.g. self-written python script in a GitHub repository'
                />
            </div>
        </div>
    </>
  );
}

export default DataProcessingStep;
