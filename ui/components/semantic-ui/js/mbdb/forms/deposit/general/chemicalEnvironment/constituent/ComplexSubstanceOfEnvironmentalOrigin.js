import CustomField from "../../../buildingBlocks/CustomField";
import Location from "../../sharedComponents/Location";
import ArrayField from "../../../buildingBlocks/ArrayField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Protocol from "../../../sharedComponents/Protocol";
import Storage from "../../sharedComponents/Storage";
import Concentration from "../../../sharedComponents/Concentration";
import OptionField from "../../../buildingBlocks/OptionField";
import OptionalField from "../../../buildingBlocks/OptionalField";

function ComplexSubstanceOfEnvironmentalOrigin( { name } ) {

    const sourceOptions = [
        { value: 'Fresh water', label: 'Fresh water' },
        { value: 'Marine', label: 'Marine' },
        { value: 'Ice core', label: 'Ice core' },
        { value: 'Sediment', label: 'Sediment' },
        { value: 'Sewage', label: 'Sewage' },
        { value: 'Soil', label: 'Soil' },
      ];

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
                    options={sourceOptions} 
                    label='Source' 
                    fieldName='source'
                    tooltip='The environmental source where the complex substance was derived from'
                />
            </div>
        </div>
        <div className="flex">
            <div className="mr-3">
                <Location
                    name={`${name}.location`}
                    tooltip='The longitude, from west to east, in degrees (decimal notation)'
                />
            </div>
            <div>
                <Concentration
                    name={`${name}.concentration`}
                />
            </div>
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
                        tooltip='List of the steps performed during the preparation of the complex substance'
                    >
                        <Protocol
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <OptionalField
                name={name}
                label='Storage'
                fieldName='storage'
                tooltip='The specific steps that were taken to prepare the samples for storage (e.g. flash freezing in liquid nitrogen), if applicable'
                renderChild={({ optionalFieldName }) => (
                    <FormWrapper
                        headline='Storage'
                        tooltip='The specific steps that were taken to prepare the samples for storage (e.g. flash freezing in liquid nitrogen), if applicable'
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

export default ComplexSubstanceOfEnvironmentalOrigin;