import CustomField from '../buildingBlocks/CustomField';
import OptionalField from '../buildingBlocks/OptionalField';

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
            <div className='-mt-3 mr-3'>
                <OptionalField
                    name={name}
                    label='Software name'
                    fieldName='software_name'
                    tooltip='The name of the software that was used for the step (e.g. Excel)'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <CustomField
                                name={optionalFieldName}
                                label='Software name'
                                tooltip='The name of the software that was used for the step (e.g. Excel)'
                            />
                        </div>
                    )}
                />
            </div>
            <div className='-mt-3 mr-3'>
                <OptionalField
                    name={name}
                    label='Software version'
                    fieldName='software_version'
                    tooltip='The version of the software that was used for the step'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <CustomField
                                name={optionalFieldName}
                                label='Software version'
                                tooltip='The version of the software that was used for the step'
                            />
                        </div>
                    )}
                />
            </div>
            <div className='-mt-3'>
                <OptionalField
                    name={name}
                    label='Link to source code'
                    fieldName='link_to_source_code'
                    tooltip='If processing was performed with software where the source code is legally available a link can be specified here (e.g. self-written python script in a GitHub repository'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <CustomField
                                name={optionalFieldName}
                                label='Link to source code'
                                tooltip='If processing was performed with software where the source code is legally available a link can be specified here (e.g. self-written python script in a GitHub repository'
                            />
                        </div>
                    )}
                />
            </div>
        </div>
    </>
  );
}

export default DataProcessingStep;
