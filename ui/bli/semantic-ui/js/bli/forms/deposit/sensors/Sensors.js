import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Supplier from "../sharedComponents/Supplier";
import HydrationTime from "./HydrationTime";
import LigandInformation from "@mbdb_deposit/sharedComponents/LigandInformation";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

function Sensors( { name } ) {

    CreateUuid(name);

    const previouslyUsedOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
      ];

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='name'
                label='Name'
                required={true}
                tooltip='Descriptive name of the sensor'
                width='w-full'
            />
        </div>
        <div className="flex -mt-3 mb-3">
            <div className="mr-3">
                <OptionalField
                    name={name}
                    label='Surface properties'
                    fieldName='surface_properties'
                    tooltip='The type of surface properties the sensor has, e.g. Protein A'
                    renderChild={({ optionalFieldName }) => (
                        <CustomField
                            name={optionalFieldName}
                            label='Surface properties'
                            tooltip='The type of surface properties the sensor has, e.g. Protein A'
                        />
                    )}
                />
            </div>
            <div className="mr-3">
                <OptionalField
                    name={name}
                    label='Sensor id'
                    fieldName='sensor_id'
                    tooltip='The id of the sensor as given by the supplier'
                    renderChild={({ optionalFieldName }) => (
                        <CustomField
                            name={optionalFieldName}
                            label='Sensor id'
                            tooltip='The id of the sensor as given by the supplier'
                        />
                    )}
                />
            </div>
            <div>
                <OptionalField
                    name={name}
                    label='Previously used'
                    fieldName='previously_used'
                    tooltip='Whether or not the sensor was used for previous measurements'
                    renderChild={({ optionalFieldName }) => (
                        <OptionField
                            name={optionalFieldName}
                            label='Previously used'
                            options={previouslyUsedOptions}
                            tooltip='Whether or not the sensor was used for previous measurements'
                        />
                    )}
                />
            </div>
        </div>
        <div className="mb-3">
            <OptionalField
                name={name}
                label='Hydration time'
                fieldName='hydration_time'
                tooltip='How long the sensor was hydrated before being employed'
                renderChild={({ optionalFieldName }) => (
                    <HydrationTime
                        name={optionalFieldName}
                        colorSchema='light'
                    />
                )}
            />
        </div>
        <div className="mb-3">
            <OptionalField
                name={name}
                label='Ligand'
                fieldName='ligand'
                tooltip='Information about the ligand and how it was immobilized'
                renderChild={({ optionalFieldName }) => (
                    <LigandInformation
                        name={optionalFieldName}
                        colorSchema='light'
                    />
                )}
            />
        </div>
        <div>
            <Supplier
                name={`${name}.supplier`}
                colorSchema='light'
                tooltip='Information about the supplier of the sensor'
            />
        </div>
    </>
  );
}

export default Sensors;