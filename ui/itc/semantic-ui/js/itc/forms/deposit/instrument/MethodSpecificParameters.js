import React from 'react';
import FormWrapper from '@mbdb_deposit/buildingBlocks/FormWrapper';
import OptionField from '@mbdb_deposit/buildingBlocks/OptionField';
import CellTemperature from './methodSpecificParameters/CellTemperature';
import CellVolume from './methodSpecificParameters/CellVolume';
import ExperimentType from './methodSpecificParameters/experimentType/ExperimentType';
import ReferencePower from './methodSpecificParameters/ReferencePower';
import StirringSpeed from './methodSpecificParameters/StirringSpeed';

function MethodSpecificParameters( { name } ) {

    const feedbackModeOptions = [
        { value: 'Low', label: 'Low' },
        { value: 'High', label: 'High' }
    ];

  return (
    <>
        <FormWrapper
            headline='Method specific parameters'
            tooltip='The parameters of the experiment that is specific to ITC'
        >
            <div className='mb-3'>
                <OptionField
                    name={name}
                    fieldName='feedback_mode'
                    label='Feedback mode'
                    required={true}
                    options={feedbackModeOptions}
                    tooltip='Operating mode where conditions are adjusted automatically to maintain constant temperature during heat measurements'
                />
            </div>
            <div className="flex mb-3">
                <div>
                    <ExperimentType
                        name={`${name}.experiment_type_base`}
                        colorSchema='light'
                    />
                </div>
            </div>
            <div className="flex mb-3">
                <div className="mr-3">
                    <CellTemperature
                        name={`${name}.cell_temperature`}
                        colorSchema='light'
                    />
                </div>
                <div>
                    <CellVolume
                        name={`${name}.cell_volume`}
                        colorSchema='light'
                    />
                </div>
            </div>
            <div className="flex">
                <div className="mr-3">
                    <ReferencePower
                        name={`${name}.reference_power`}
                        colorSchema='light'
                    />
                </div>
                <div>
                    <StirringSpeed
                        name={`${name}.stirring_speed`}
                        colorSchema='light'
                    />
                </div>
            </div>
        </FormWrapper>
    </>
  );
}

export default MethodSpecificParameters;