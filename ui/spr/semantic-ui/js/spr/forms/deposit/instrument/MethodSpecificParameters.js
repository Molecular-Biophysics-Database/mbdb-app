import React from 'react';
import FormWrapper from '@mbdb_deposit/buildingBlocks/FormWrapper';
import OptionField from '@mbdb_deposit/buildingBlocks/OptionField';

function MethodSpecificParameters( { name } ) {

    const experimentTypeOptions = [
        { value: 'Affinity', label: 'Affinity' },
        { value: 'Quantification', label: 'Quantification' },
        { value: 'Other', label: 'Other' },
    ];

  return (
    <>
        <FormWrapper
            headline='Method specific parameters'
            tooltip='The parameters of the experiment that is specific to BLI'
        >
            <OptionField
                name={name}
                options={experimentTypeOptions}
                label='Experiment type'
                fieldName='experiment_type'
                required={true}
                tooltip='Which type of parameter is sought with the measurements'
            />
        </FormWrapper>
    </>
  );
}

export default MethodSpecificParameters;