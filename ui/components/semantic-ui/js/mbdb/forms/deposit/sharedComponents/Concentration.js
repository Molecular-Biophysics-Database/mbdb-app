import CustomField from "../buildingBlocks/CustomField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import OptionField from "../buildingBlocks/OptionField";

function Concentration({ name, tooltip, colorSchema }) {

    const unitOptions = [
        { value: 'M', label: 'M' },
        { value: 'mM', label: 'mM' },
        { value: 'µM', label: 'µM' },
        { value: 'nM', label: 'nM' },
        { value: 'pM', label: 'pM' },
        { value: 'fM', label: 'fM' },
        { value: 'aM', label: 'aM' },
        { value: 'g/L', label: 'g/L' },
        { value: 'mg/mL', label: 'mg/mL' },
        { value: 'µg/mL', label: 'µg/mL' },
        { value: 'ng/mL', label: 'ng/mL' },
        { value: 'mol/kg', label: 'mol/kg' },
        { value: 'mmol/kg', label: 'mmol/kg' },
        { value: 'v/v %', label: 'v/v %' },
        { value: 'w/w %', label: 'w/w %' },
        { value: 'v/w %', label: 'v/w %' },
        { value: 'w/v %', label: 'w/v %' },
        { value: 'U/ml', label: 'U/ml' },
        { value: '% saturated', label: '% saturated' },
      ];

  return (
    <>
      <FormWrapper 
        colorSchema={colorSchema}
        headline='Concentration'
        tooltip={tooltip}
      >
        <div className="flex">
          <div className="mr-3">
              <CustomField 
                  name={name}
                  fieldName='value'
                  label='Value'
                  type='number'
                  tooltip='The numerical value of the concentration, -1 if unknown'
              />
          </div>
          <div>
              <OptionField
                  name={name}
                  options={unitOptions}
                  fieldName='unit'
                  label='Unit'
                  tooltip='The unit of the concentration'
              />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Concentration;