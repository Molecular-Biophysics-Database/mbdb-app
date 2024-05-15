import CustomField from '../buildingBlocks/CustomField';
import OptionField from '../buildingBlocks/OptionField';
import OptionalField from '../buildingBlocks/OptionalField';

function DataFitting( { name } ) {

    const qualityOptions = [
        { value: 'R^2', label: 'R^2' },
        { value: 'SEM', label: 'SEM' },
        { value: 'Red. Chi^2', label: 'Red. Chi^2' },
        { value: '1sigma', label: '1sigma' },
        { value: '2sigma', label: '2sigma' },
        { value: '3sigma', label: '3sigma' },
        { value: '4sigma', label: '4sigma' },
        { value: '5sigma', label: '5sigma' },
        { value: 'Skewness', label: 'Skewness' },
    ];

  return (
    <>
        <div className='flex mb-3'>
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='model'
                    label='Model'
                    tooltip='Description of the model (e.g. 1:1 binding)'
                />
            </div>
            <div className='-mt-3 mr-3'>
                <OptionalField
                    name={name}
                    label='Software name'
                    fieldName='software_name'
                    tooltip='The name of the software that was used for doing the data fitting (e.g. Excel)'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <CustomField
                                name={optionalFieldName}
                                label='Software name'
                                tooltip='The name of the software that was used for doing the data fitting (e.g. Excel)'
                            />
                        </div>
                    )}
                />
            </div>
            <div className='-mt-3'>
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
        </div>
        <div className='flex'>
            <div className='-mt-3 mr-3'>
                <OptionalField
                    name={name}
                    label='Quality'
                    fieldName='quality'
                    tooltip='Numerical value representing the quality estimate of the result'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <CustomField
                                name={optionalFieldName}
                                label='Quality'
                                type='number'
                                tooltip='Numerical value representing the quality estimate of the result'
                            />
                        </div>
                    )}
                />
            </div>
            <div className='-mt-3'>
                <OptionalField
                    name={name}
                    label='Quality type'
                    fieldName='quality_type'
                    tooltip='Type of the quality estimate'
                    renderChild={({ optionalFieldName }) => (
                        <div>
                            <OptionField
                                name={optionalFieldName}
                                options={qualityOptions}
                                label='Quality type'
                                tooltip='Type of the quality estimate'
                            />
                        </div>
                    )}
                />
            </div>
        </div>
    </>
  );
}

export default DataFitting;
