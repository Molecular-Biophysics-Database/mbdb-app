import CustomField from "./CustomField";
import FormWrapper from "./FormWrapper";
import OptionField from "./OptionField";

function ValueError( {colorSchema, name} ) {

    const ErrorOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
    ];

  return (
    <>    
        <div className='flex'>
            <FormWrapper 
                headline='Value error'
                tooltip='The expected error of the result in terms of a 95 % confidence interval'
                colorSchema={colorSchema}
            >
                <div className="flex">
                    <div className="mr-3">
                        <CustomField
                            name={name}
                            fieldName='lower_error'
                            type='Lower'
                            label='Lower'
                            tooltip='The lower error, i.e. the number that should be subtracted from the value to get the lower bound of the 95 % confidence interval. The same unit as the value being described is assumed. If relative errors are provided, please provide it in fractional form (e.g.  0.01 for 1 %)'
                            width='w-[8rem]'
                        />
                    </div>
                    <div className="mr-3">
                        <CustomField
                            name={name}
                            fieldName='upper_error'
                            type='number'
                            label='Upper'
                            tooltip='The upper error, i.e. the number that should be added to the value to get the upper bound of the 95 % confidence interval. The same unit as the value being described is assumed. If relative errors are provided, please provide it in fractional form (e.g.  0.01 for 1 %)'
                            width='w-[8rem]'
                        />
                    </div>
                    <div>
                        <OptionField
                            name={name}
                            fieldName='errors_are_relative'
                            options={ErrorOptions}
                            label='Errors are relative'
                            tooltip='True if the error values should be interpreted as relative errors (fractional uncertainty)'
                        />
                    </div>
                </div>
            </FormWrapper>

        </div>
    </>
  );
}

export default ValueError;