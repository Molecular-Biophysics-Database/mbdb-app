import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import ArrayField from "../../buildingBlocks/ArrayField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Protocol from "../../buildingBlocks/Protocol";
import Storage from "../../buildingBlocks/Storage";
import Details from "../../components/Details";
import Concentration from "../../components/Concentration";
import OptionField from "../../buildingBlocks/OptionField";
import { useFormikContext } from "formik";
import UseDefault from "../../buildingBlocks/UseDefault";

function ComplexSubstanceOfChemicalOrigin( { name } ) {

    const classOptions = [
        { value: 'lipid_assembly', label: 'Lipid assembly' },
      ];

      const { values } = useFormikContext();

      const fieldName = 'preparation_protocol'

      UseDefault(values, `${name}.${fieldName}`, [{}] );

  return (
    <>
        <div className="flex mb-3">
            <div className='mr-3'>
                <CustomField
                    name={name}
                    label='Name'
                    fieldName='name'
                    width='w-[45rem]'
                    tooltip='Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample'
                />
            </div>
            <div>
                <OptionField
                    name={name}
                    options={classOptions}
                    label='Class'
                    fieldName='class'
                    tooltip='The chemical origin where the complex substance was derived from'
                />
            </div>
        </div>
        <div className="mb-3">
            <Concentration
                name={`${name}.concentration`}
            />
        </div>
        <div className="flex -mt-3 mb-3">
            <div>
                <ArrayField
                    name={name}
                    label='Preparation protocol'
                    fieldName={fieldName}
                    required={true}
                    tooltip='List of the steps performed during the preparation of the complex substance'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper
                            headline={`Preparation protocol ${index + 1}`}
                            tooltipHeader='List of the steps performed during the preparation of the complex substance'
                        >
                            <Protocol
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
            <div>
                <ArrayField
                    name={name}
                    label='Additional specification'
                    fieldName='additional_specifications'
                    tooltip='Additional information about the lipid assembly, if applicable'
                    renderChild={({ arrayName, index }) => (
                        <CustomField
                            name={`${arrayName}.${index}`}
                            label={`Additional specification ${index + 1}`}
                            width='w-[15rem]'
                            tooltip='Additional information about the lipid assembly, if applicable'
                        />
                    )}
                />
            </div>
        </div>
        <div className="mb-3">
            <ArrayField
                name={name}
                label='Storage'
                fieldName='storage'
                maxItems={1}
                tooltip='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Storage ${index + 1}`}
                        tooltipHeader='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                    >
                        <Storage
                            name={`${arrayName}.${index}`}
                            colorSchema='light'
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <Details name={`${name}.details`} sizeColorSchema='light' colorSchemaProtocol='light' />
        </div>
    </>
  );
}

export default ComplexSubstanceOfChemicalOrigin;