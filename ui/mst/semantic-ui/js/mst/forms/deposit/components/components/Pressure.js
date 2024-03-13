import React from 'react';
import ValueUnit from '../buildingBlocks/ValueUnit';
import ValueError from '../buildingBlocks/ValueError';
import FormWrapper from '../buildingBlocks/FormWrapper';
import OptionField from '../buildingBlocks/OptionField';

function Pressure( {name} ) {

    const unitOptions = [
        { value: 'Pa', label: 'Pa' },
        { value: 'kPa', label: 'kPa' },
        { value: 'MPa', label: 'MPa' },
        { value: 'Bar', label: 'Bar' },
        { value: 'mBar', label: 'mBar' },
        { value: 'atm', label: 'atm' },
        { value: 'Torr', label: 'Torr' },
        { value: 'PSI', label: 'PSI' },
        { value: 'mmHg', label: 'mmHg' },
        { value: 'inchHg', label: 'inchHg' },
    ];

    const obtainedOptions = [
        { value: 'Measurement', label: 'Measurement' },
        { value: 'Calculation', label: 'Calculation' },
        { value: 'Assumption', label: 'Assumption' },
        { value: 'Other', label: 'Other' },
    ];

    const controlledOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
    ];

  return (
    <>
        <FormWrapper headline='Pressure'>
            <div className='flex mb-3'>
                <div>
                    <ValueUnit options={unitOptions} name={name} width='w-[7rem]'/>
                </div>
                <div className='flex'>
                    <div className='mr-3'>
                        <OptionField
                            options={obtainedOptions} 
                            name={name} 
                            label='Obtained by' 
                            fieldName='obtained_by'
                            width='w-[10rem]'
                        />
                    </div>
                    <div>
                        <OptionField
                            options={controlledOptions} 
                            name={name} 
                            label='Controlled' 
                            fieldName='controlled'
                            width='w-[7rem]'
                        />
                    </div>
                </div>
            </div>
            <div>
                <ValueError name={`${name}.value_error`}/>
            </div>
        </FormWrapper>
    </>
  );
}

export default Pressure;
