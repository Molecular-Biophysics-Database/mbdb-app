import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import Protocol from "@mbdb_deposit/sharedComponents/Protocol";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

function SurfaceModification( { name, colorSchema } ) {

    const fieldName = 'protocol';

    UseDefault(`${name}.${fieldName}`, [{}] );

  return (
    <>
        <FormWrapper
            headline='Surface modification'
            colorSchema={colorSchema}
            tooltip='If the plate had a modified surface, the modification can specified here (e.g. Non-binding surface)'
        >
            <div>
                <CustomField
                    name={name}
                    label='Type'
                    fieldName='type'
                    tooltip='The expected type of surface of the wells after the modification (e.g. BSA coated)'
                />
            </div>
            <div className="mr-3">
                <ArrayField
                    name={name}
                    required={true}
                    label='Protocol'
                    fieldName={fieldName}
                    tooltip='List of protocol steps used to modify the surface of the wells'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper
                            headline={`Protocol ${index + 1}`}
                            tooltip='List of protocol steps used to modify the surface of the wells'
                        >
                            <Protocol
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
        </FormWrapper>
    </>
  );
}

export default SurfaceModification;