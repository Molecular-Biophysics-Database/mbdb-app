import FormWrapper from '../../../../buildingBlocks/FormWrapper';
import OptionField from '../../../../buildingBlocks/OptionField';
import { getIn, useFormikContext } from 'formik';
import HomogeneityYes from './HomogeneityYes';
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
            label="Homogeneity"
            fieldName='homogeneity'
            tooltip='Information about if, and how homogeneity was assessed'
            initialValue={{ type: 'Yes'}}
            renderChild={({ optionalFieldName }) => {
                const actualValue = getIn(values, optionalFieldName)
                if (!actualValue) {return null}        
                return(
                <FormWrapper
                    headline='Homogeneity'
                    colorSchema={colorSchema}
                    tooltip='Information about if, and how homogeneity was assessed'
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
                                <HomogeneityYes
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
