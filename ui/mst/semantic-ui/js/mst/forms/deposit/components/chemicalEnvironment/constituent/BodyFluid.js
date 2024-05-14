import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import OptionField from "../../buildingBlocks/OptionField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Protocol from "../../buildingBlocks/Protocol";
import Storage from "../../buildingBlocks/Storage";
import Concentration from "../../components/Concentration";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function BodyFluid( { name } ) {

    const fluidOptions = [
        { value: 'Blood', label: 'Blood' },
        { value: 'Fecal matter', label: 'Fecal matter' },
        { value: 'Milk', label: 'Milk' },
        { value: 'Plasma', label: 'Plasma' },
        { value: 'Saliva', label: 'Saliva' },
        { value: 'Serum', label: 'Serum' },
        { value: 'Urine', label: 'Urine' },
        { value: 'Plant extract', label: 'Plant extract' },
    ];

  return (
    <>
        <div className='flex mb-3'>
          <div className='mr-3'>
            <CustomField
                name={name}
                label='Name'
                fieldName='name'
                tooltip='Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample'
            />
          </div>
          <div className="mr-3">
            <OptionField
                name={name}
                options={fluidOptions}
                label='Fluid'
                fieldName='fluid'
                tooltip='The body fluid the complex substance is derived from'
            />
          </div>
          <div className="mr-3">
            <CustomField
                name={name}
                label='Health status'
                fieldName='health_status'
                tooltip='Health status of the donor organism where the body fluid was derived from (e.g. healthy, sick, patient with Diabetes type 2)'
            />
          </div>
          <div>
            <VocabularySelectField
                search={(options) => options}
                type="organisms/authoritative"
                label={
                    <FieldLabel
                    htmlFor={`${name}.source_organism`}
                    icon=""
                    />
                }
                fieldPath={`${name}.source_organism`}
                placeholder='Source organism'
            />
          </div>
        </div>
        <div className="mb-3">
            <Concentration
                name={`${name}.concentration`}
            />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Preparation protocol'
                fieldName='preparation_protocol'
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
            <ArrayField
                name={name}
                label='Additional specification'
                fieldName='additional_specifications'
                tooltip='Additional information about the complex substance can be specified here'
                renderChild={({ arrayName, index }) => (
                    <CustomField
                        name={`${arrayName}.${index}`}
                        label={`Additional specification ${index + 1}`}
                        width='w-[15rem]'
                        tooltip='Additional information about the complex substance can be specified here'
                    />
                )}
            />
        </div>
    </>
  );
}

export default BodyFluid;