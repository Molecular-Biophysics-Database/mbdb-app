import React from 'react';
import CustomField from '../buildingBlocks/CustomField';
import OptionField from '../buildingBlocks/OptionField';

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
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='software_name'
                    label='Software name'
                    tooltip='The name of the software that was used for doing the data fitting (e.g. Excel)'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='software_version'
                    label='Software version'
                    tooltip='The version of the software that was used for the step'
                />
            </div>
        </div>
        <div className='flex'>
            <div className='mr-3'>
                <CustomField
                    name={name}
                    fieldName='quality'
                    label='Quality'
                    type='number'
                    tooltip='Numerical value representing the quality estimate of the result'
                />
            </div>
            <div>
                <OptionField
                    name={name}
                    options={qualityOptions}
                    fieldName='quality_type'
                    label='Quality type'
                    tooltip='Type of the quality estimate'
                />
            </div>
        </div>
    </>
  );
}

export default DataFitting;
