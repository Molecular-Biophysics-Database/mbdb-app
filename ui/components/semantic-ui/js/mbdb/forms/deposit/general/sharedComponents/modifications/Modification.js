import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";
import Protocol from "../../../sharedComponents/Protocol";
import ArrayField from "../../../buildingBlocks/ArrayField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import OptionalField from "../../../buildingBlocks/OptionalField";

function Modification( { name, colorSchema } ) {

  return (
    <>
        <div className="flex mb-3">
            <div>
                <CustomField
                    name={name}
                    required
                    fieldName='type'
                    label='Type'
                    tooltip='The common name/type of the modification'
                />
            </div>
            <div className="mr-3">
                <OptionalField
                    name={name}
                    fieldName='position'
                    label='Position'
                    tooltip='The position where the modification occurs'
                />
            </div>
        </div>
        <div>
            <ArrayField
                name={name}
                label='Protocol'
                fieldName='protocol'
                tooltip='List of steps that led to the modification taking place'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Protocol ${index + 1}`}
                        colorSchema={colorSchema}
                        tooltip='List of steps that led to the modification taking place'
                    >
                        <Protocol
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default Modification;