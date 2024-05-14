import FormWrapper from '../../../../buildingBlocks/FormWrapper';
import OptionField from '../../../../buildingBlocks/OptionField';
import ByIntactMass from './ByIntactMass';
import BySequencing from './BySequencing';
import ByFingerprinting from './ByFingerprinting';
import OptionalField from '../../../../buildingBlocks/OptionalField';

function Identity( { name, colorSchema } ) {

    const checkedOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
    ];

  return (
    <>
        <OptionalField
            name={name}
            label='Identity'
            fieldName='identity'
            tooltip='Information about if, and how identity was assessed'
            renderChild={({ optionalFieldName }) => (
                <FormWrapper
                    headline='Identity'
                    colorSchema={colorSchema}
                    tooltip='Information about if, and how identity was assessed'
                >
                    <div>
                        <OptionField
                            name={optionalFieldName}
                            fieldName='checked'
                            label='Checked'
                            options={checkedOptions}
                            tooltip='Whether the identity was confirmed experimentally'
                        />
                    </div>
                    <div>
                        <OptionalField
                            name={optionalFieldName}
                            label='By intact mass'
                            fieldName='by_intact_mass'
                            tooltip='How identity was determined by intact mass, if applicable'
                            renderChild={({ optionalFieldName }) => (
                                <ByIntactMass
                                    name={optionalFieldName}
                                    colorSchema={colorSchema === 'light' ? '' : 'light'}
                                />
                            )}
                        />
                    </div>
                    <div>
                        <OptionalField
                            name={optionalFieldName}
                            label='By sequencing'
                            fieldName='by_sequencing'
                            tooltip='How identity was determined by intact mass, if applicable'
                            renderChild={({ optionalFieldName }) => (
                                <BySequencing
                                    name={optionalFieldName}
                                    colorSchema={colorSchema === 'light' ? '' : 'light'}
                                />
                            )}
                        />
                    </div>
                    <div>
                        <OptionalField
                            name={optionalFieldName}
                            label='By fingerprinting'
                            fieldName='by_fingerprinting'
                            tooltip='How identity was determined by fingerprinting, if applicable'
                            renderChild={({ optionalFieldName }) => (
                                <ByFingerprinting
                                    name={optionalFieldName}
                                    colorSchema={colorSchema === 'light' ? '' : 'light'}
                                />
                            )}
                        />
                    </div>
                </FormWrapper>
            )}
        />
    </>
  );
}

export default Identity;
