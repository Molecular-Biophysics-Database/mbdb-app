import FormWrapper from '../../../../buildingBlocks/FormWrapper';
import OptionField from '../../../../buildingBlocks/OptionField';
import { getIn, useFormikContext } from 'formik';
import PurityYes from './PurityYes';
import OptionalField from '../../../../buildingBlocks/OptionalField';

function Purity( { name, colorSchema } ) {

    const { values } = useFormikContext();

    const typeOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
    ];

  return (
    <>
        <OptionalField
            name={name}
            label="Purity"
            fieldName='purity'
            initialValue={{ type: 'Yes'}}
            tooltip='Information about if and how the purity was obtained'
            renderChild={({ optionalFieldName }) => {
                const actualValue = getIn(values, optionalFieldName)
                if (!actualValue) {return null}        
                return(
                <FormWrapper
                    headline='Purity'
                    colorSchema={colorSchema}
                    tooltip='Information about if and how the purity was obtained'
                >
                    <div className="flex">
                        <div className="mr-3">
                            <OptionField
                                name={optionalFieldName}
                                options={typeOptions}
                                label='type'
                                fieldName='type'
                                width='w-full'
                            />
                        </div>
                        <div>
                            {actualValue.type === 'Yes' && (
                                <PurityYes
                                    name={optionalFieldName}
                                />
                            )}
                            {actualValue.type === 'No' && (
                                <></>
                            )}
                        </div>
                    </div>
                </FormWrapper>
            )}}
        />
    </>
  );
}

export default Purity;
