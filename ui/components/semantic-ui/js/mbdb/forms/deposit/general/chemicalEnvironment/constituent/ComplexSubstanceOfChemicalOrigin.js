import CustomField from "../../../buildingBlocks/CustomField";
import ArrayField from "../../../buildingBlocks/ArrayField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Protocol from "../../../sharedComponents/Protocol";
import Storage from "../../sharedComponents/Storage";
import Details from "../../sharedComponents/Details";
import Concentration from "../../../sharedComponents/Concentration";
import OptionField from "../../../buildingBlocks/OptionField";
import UseDefault from "../../../buildingBlocks/UseDefault";
import OptionalField from "../../../buildingBlocks/OptionalField";

function ComplexSubstanceOfChemicalOrigin( { name } ) {

    const classOptions = [
        { value: 'lipid_assembly', label: 'Lipid assembly' },
    ];

    const fieldName = 'preparation_protocol';

    UseDefault(`${name}.${fieldName}`, [{}] );

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
                            tooltip='List of the steps performed during the preparation of the complex substance'
                        >
                            <Protocol
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
            <div className="mt-3">
                <Concentration
                    name={`${name}.concentration`}
                />
            </div>
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
        <div className="mb-3">
            <OptionalField
                name={name}
                label='Storage'
                fieldName='storage'
                tooltip='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                renderChild={({ optionalFieldName }) => (
                    <FormWrapper
                        headline='Storage'
                        tooltip='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                    >
                        <Storage
                            name={optionalFieldName}
                            colorSchema='light'
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <Details name={`${name}.details`} />
        </div>
    </>
  );
}

export default ComplexSubstanceOfChemicalOrigin;