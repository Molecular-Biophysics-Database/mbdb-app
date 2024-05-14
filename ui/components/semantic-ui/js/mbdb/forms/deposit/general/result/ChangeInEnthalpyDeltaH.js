import CustomField from "../../buildingBlocks/CustomField";
import ValueUnit from "../../buildingBlocks/ValueUnit";
import ValueError from "../../buildingBlocks/ValueError";
import ArrayField from "../../buildingBlocks/ArrayField";
import EntityInvolved from "./EntityInvolved";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import UseDefault from "../../buildingBlocks/UseDefault";
import OptionalField from "../../buildingBlocks/OptionalField";

function ChangeInEnthalpyDeltaH( { name } ) {

    const unitOptions = [
        { value: 'kcal/mol', label: 'kcal/mol' },
        { value: 'kJ/mol', label: 'kJ/mol' },
    ];

    const fieldNameEntityInvolved = 'entities_involved';
    UseDefault(`${name}.${fieldNameEntityInvolved}`, [{}] );

  return (
    <>
        <div className='flex mb-3'>
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='name'
                    label='Name'
                    tooltip='Descriptive name (id) of the result (e.g. Kd of Lysozyme and VHH2). Must be unique within a record'
                />
            </div>
            <div>
                <ValueUnit
                    options={unitOptions}
                    name={name}
                    tooltipValue='Numerical value of the result'
                    tooltipUnit='Unit of the change in enthalpy rate constant'
                />
            </div>
        </div>
        <div>
            <OptionalField
                name={name}
                label='Value error'
                fieldName='value_error'
                tooltip='The expected error of the result in terms of a 95 % confidence interval'
                renderChild={({ optionalFieldName }) => (
                    <div>
                        <ValueError
                            name={optionalFieldName}
                            colorSchema='light'
                        />
                    </div>
                )}
            />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Entity involved'
                fieldName={fieldNameEntityInvolved}
                required={true}
                tooltip='List of chemical or molecular assemblies the result describes and how many copies of each are involved'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`Entity involved ${index + 1}`}
                        tooltip='List of chemical or molecular assemblies the result describes and how many copies of each are involved'
                    >
                        <EntityInvolved
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default ChangeInEnthalpyDeltaH;