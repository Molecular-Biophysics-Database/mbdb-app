import CustomField from "../../buildingBlocks/CustomField";
import ValueUnit from "../../buildingBlocks/ValueUnit";
import ValueError from "../../buildingBlocks/ValueError";
import ArrayField from "../../buildingBlocks/ArrayField";
import EntityInvolved from "./EntityInvolved";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import UseDefault from "../../buildingBlocks/UseDefault";
import OptionalField from "../../buildingBlocks/OptionalField";

function ConstantOfDissociationKD( { name } ) {

    const unitOptions = [
        { value: 'M', label: 'M' },
        { value: 'M^2', label: 'M^2' },
        { value: 'mM', label: 'mM' },
        { value: 'mM^2', label: 'mM^2' },
        { value: 'µM', label: 'µM' },
        { value: 'µM^2', label: 'µM^2' },
        { value: 'nM', label: 'nM' },
        { value: 'nM^2', label: 'nM^2' },
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
                    tooltipUnit='Unit of the constant of dissociation'
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

export default ConstantOfDissociationKD;