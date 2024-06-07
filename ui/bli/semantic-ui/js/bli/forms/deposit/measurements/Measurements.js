import React from "react";
import { getIn, useFormikContext } from "formik";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Sample from "./Sample";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

function Measurements( {name} ) {

    CreateUuid(name);

    const { values } = useFormikContext();

    const sensorValue = getIn(values, `metadata.method_specific_parameters.sensors`);
    const sensorOptions = CreateOptions(sensorValue, 'Select Sensor, if applicable');

    const measurementProtocolStepValue = getIn(values, `metadata.method_specific_parameters.measurement_protocol`);
    const measurementProtocolStepOptions = CreateOptions(measurementProtocolStepValue, 'Select Measurement protocol step, if applicable');

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='name'
                label='Name'
                required={true}
                tooltip='Name (id) of the measurement which must be unique within a record (i.e. triplicates must be named individually in the raw data file). The name must allow location of the measurement data within the raw data file as well as processed data files if these are present'
                width='w-full'
            />
        </div>
        <div className="flex mb-3">
            <div className="mr-3">
                <OptionField
                    name={name}
                    label='Sensor'
                    fieldName='sensor'
                    required={true}
                    options={sensorOptions}
                    tooltip='Link to the sensor used for the measurement'
                />
            </div>
            <div className="mr-3">
                <OptionField
                    name={name}
                    label='Measurement protocol step'
                    fieldName='measurement_protocol_step'
                    required={true}
                    options={measurementProtocolStepOptions}
                    tooltip='Link to one of the measurement steps'
                    width='w-[17rem]'
                />
            </div>
        </div>
        <div>
            <Sample
                name={`${name}.sample`}
                colorSchema='light'
            />
        </div>
    </>
  );
}

export default Measurements;