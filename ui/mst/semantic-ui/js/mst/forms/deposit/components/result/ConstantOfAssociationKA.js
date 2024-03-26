import React from "react";
import CustomField from "../buildingBlocks/CustomField";
import ValueUnit from "../buildingBlocks/ValueUnit";
import ValueError from "../buildingBlocks/ValueError";
import EntityInvolved from "../buildingBlocks/EntityInvolved";
import FormWrapper from "../buildingBlocks/FormWrapper";
import UseDefault from "../buildingBlocks/UseDefault";
import ArrayField from "../buildingBlocks/ArrayField";
import { useFormikContext } from "formik";

function ConstantOfAssociationKA( { name } ) {

    const { values } = useFormikContext()

    const unitOptions = [
        { value: 'M^-1', label: 'M^-1' },
        { value: 'M^-2', label: 'M^-2' },
        { value: 'mM^-1', label: 'mM^-1' },
        { value: 'mM^-2', label: 'mM^-2' },
        { value: 'µM^-1', label: 'µM^-1' },
        { value: 'µM^-2', label: 'µM^-2' },
        { value: 'nM^-1', label: 'nM^-1' },
        { value: 'nM^-2', label: 'nM^-2' },
    ];

    const fieldNameEntityInvolved = 'entities_involved'
    UseDefault(values, `${name}.${fieldNameEntityInvolved}`, [{}] );

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
                    tooltipUnit='Unit of the constant of association'
                />
            </div>
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
                        tooltipHeader='List of chemical or molecular assemblies the result describes and how many copies of each are involved'
                    >
                        <EntityInvolved
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Value error'
                fieldName='value_error'
                maxItems={1}
                tooltip='The expected error of the result in terms of a 95 % confidence interval'
                renderChild={({ arrayName, index }) => (
                    <div>
                        <ValueError
                            name={`${arrayName}.${index}`}
                            colorSchema='light'
                        />
                    </div>
                )}
            />
        </div>
    </>
  );
}

export default ConstantOfAssociationKA;