import FormWrapper from '../../../../buildingBlocks/FormWrapper';
import OptionField from '../../../../buildingBlocks/OptionField';

function ByFingerprinting( { name, colorSchema } ) {

    const methodOptions = [
        { value: 'Protease digest + Mass spectrometry', label: 'Protease digest + Mass spectrometry' },
        { value: 'Restriction enzyme digest + Gel electrophoresis', label: 'Restriction enzyme digest + Gel electrophoresis' },
    ];

  return (
    <>
        <FormWrapper
            headline='By fingerprinting'
            colorSchema={colorSchema}
            tooltip='How identity was determined by intact mass, if applicable'
        >
            <div>
                <OptionField
                    name={name}
                    fieldName='method'
                    label='Method'
                    options={methodOptions}
                    tooltip='The method used for fingerprinting'
                />
            </div>
        </FormWrapper>
    </>
  );
}

export default ByFingerprinting;