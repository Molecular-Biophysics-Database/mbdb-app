import React from "react";
import FormWrapper from '../../../../buildingBlocks/FormWrapper';
import OptionField from '../../../../buildingBlocks/OptionField';
import DeviationFromExpectedMass from './DeviationFromExpectedMass';

function ByIntactMass( { name, colorSchema } ) {

    const methodOptions = [
        { value: 'Mass spectrometry', label: 'Mass spectrometry' },
        { value: 'SDS-PAGE', label: 'SDS-PAGE' },
    ];

  return (
    <>
        <FormWrapper
            headline='By intact mass'
            colorSchema={colorSchema}
            tooltip='How identity was determined by intact mass, if applicable'
        >
            <div className='mb-3'>
                <OptionField
                    name={name}
                    required
                    fieldName='method'
                    label='Method'
                    options={methodOptions}
                    tooltip='The method used to determine the intact mass'
                />
            </div>
            <div>
                <DeviationFromExpectedMass
                    name={`${name}.deviation_from_expected_mass`}
                    required
                    colorSchema={colorSchema === 'light' ? '' : 'light'}
                />
            </div>
        </FormWrapper>
    </>
  );
}

export default ByIntactMass;
