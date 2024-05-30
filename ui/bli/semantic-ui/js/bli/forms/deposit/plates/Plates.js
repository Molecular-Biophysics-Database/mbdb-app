import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Supplier from "../sharedComponents/Supplier";
import SurfaceModification from "./SurfaceModification";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

function Plates( { name } ) {

    CreateUuid(name);

    const wellsOptions = [
        { value: '96', label: '96' },
        { value: '384', label: '384' },
    ];

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='name'
                label='Name'
                required={true}
                tooltip='Name (id) of the plate which must be unique within a record'
                width='w-full'
            />
        </div>
        <div className="flex mb-3">
            <div className="mr-3">
                <OptionField
                    name={name}
                    label='Wells'
                    fieldName='wells'
                    options={wellsOptions}
                    required={true}
                    tooltip='Number of wells in the plate'
                />
            </div>
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='type'
                    label='Type'
                    required={true}
                    tooltip='The type of the plate (e.g. half-area black polystyrene)'
                />
            </div>
            <div className="-mt-3">
                <OptionalField
                    name={name}
                    label='Sealing'
                    fieldName='sealing'
                    tooltip='The type of sealing used to seal the top of the plate'
                    renderChild={({ optionalFieldName }) => (
                        <CustomField
                            name={optionalFieldName}
                            label='Sealing'
                            tooltip='The type of sealing used to seal the top of the plate'
                        />
                    )}
                />
            </div>
        </div>
        <div>
            <Supplier
                name={`${name}.supplier`}
                colorSchema='light'
                tooltip='Information about the supplier of the plate'
            />
        </div>
        <div>
            <OptionalField
                name={name}
                label='Surface modification'
                fieldName='surface_modification'
                tooltip='If the plate had a modified surface, the modification can specified here (e.g. Non-binding surface)'
                renderChild={({ optionalFieldName }) => (
                    <SurfaceModification
                        name={optionalFieldName}
                        colorSchema='light'
                    />
                )}
            />
        </div>
    </>
  );
}

export default Plates;