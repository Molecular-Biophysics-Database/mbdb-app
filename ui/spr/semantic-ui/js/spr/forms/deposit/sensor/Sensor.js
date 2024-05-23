import React from "react";
import Supplier from "./Supplier";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function Sensor( { name } ) {

    const sensorInitializationOptions = [
        { value: 'Air', label: 'Air' },
        { value: 'Glycerol', label: 'Glycerol' },
    ];

    const previouslyUsedOptions = [
        { value: 'Yes', label: 'Yes' },
        { value: 'No', label: 'No' },
    ];

    return (
      <>
        <FormWrapper
            headline='Sensor'
            tooltip='Sensor used for the measurements'
        >
            <div className="flex -mt-3 mb-3">
                <div className="mr-3">
                    <OptionalField
                        name={name}
                        fieldName='id'
                        label='Id'
                        tooltip='The id of the sensor as given by the supplier'
                        renderChild={({ optionalFieldName }) => (
                            <CustomField
                                name={optionalFieldName}
                                label='Id'
                                tooltip='The id of the sensor as given by the supplier'
                            />
                        )}
                    />
                </div>
                <div className="mr-3">
                    <OptionalField
                        name={name}
                        fieldName='surface_properties'
                        label='Surface properties'
                        tooltip='The type surface properties the sensor has e.g. Protein A'
                        renderChild={({ optionalFieldName }) => (
                            <CustomField
                                name={optionalFieldName}
                                label='Id'
                                tooltip='The type surface properties the sensor has e.g. Protein A'
                            />
                        )}
                    />
                </div>
                <div className="mr-3">
                    <OptionalField
                        name={name}
                        fieldName='sensor_initialization'
                        label='Sensor initialization'
                        tooltip='How the initialization of the sensor was performed'
                        renderChild={({ optionalFieldName }) => (
                            <OptionField
                                name={optionalFieldName}
                                label='Sensor initialization'
                                tooltip='How the initialization of the sensor was performed'
                                options={sensorInitializationOptions}
                            />
                        )}
                    />
                </div>
                <div>
                    <OptionalField
                        name={name}
                        fieldName='previously_used'
                        label='Previously used'
                        tooltip='Whether or not the sensor was used in previous measurements'
                        renderChild={({ optionalFieldName }) => (
                            <OptionField
                                name={optionalFieldName}
                                label='Previously used'
                                tooltip='Whether or not the sensor was used in previous measurements'
                                options={previouslyUsedOptions}
                            />
                        )}
                    />
                </div>
            </div>
            <div>
                <Supplier
                    name={`${name}.supplier`}
                    tooltip='Information about the supplier of the sensor'
                    colorSchema='light'
                />
            </div>
        </FormWrapper>
      </>
    );
  }
  
  export default Sensor;