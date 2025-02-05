import React from "react";
import Supplier from "./Supplier";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function Sensor({ name }) {
  const tooltips = {
    id: "The id of the sensor as given by the supplier",
    surfaceProperties:
      "The type surface properties the sensor has e.g. Protein A",
    sensorInitialization: "How the initialization of the sensor was performed",
    previouslyUsed:
      "Whether or not the sensor was used in previous measurements",
  };

  const sensorInitializationOptions = [
    { value: "Air", label: "Air" },
    { value: "Glycerol", label: "Glycerol" },
  ];

  const previouslyUsedOptions = [
    { value: "Yes", label: "Yes" },
    { value: "No", label: "No" },
  ];

  return (
    <>
      <FormWrapper headline="Sensor" tooltip="Sensor used for the measurements">
        <div className="flex -mt-3 mb-3">
          <OptionalField
            name={name}
            fieldName="id"
            label="Id"
            tooltip={tooltips.id}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Id"
                tooltip={tooltips.id}
              />
            )}
          />

          <div className="mx-3">
            <OptionalField
              name={name}
              fieldName="surface_properties"
              label="Surface properties"
              tooltip={tooltips.surfaceProperties}
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label="Surface properties"
                  tooltip={tooltips.surfaceProperties}
                />
              )}
            />
          </div>

          <div className="mr-3">
            <OptionalField
              name={name}
              fieldName="sensor_initialization"
              label="Sensor initialization"
              tooltip={tooltips.sensorInitialization}
              renderChild={({ optionalFieldName }) => (
                <OptionField
                  name={optionalFieldName}
                  label="Sensor initialization"
                  tooltip={tooltips.sensorInitialization}
                  options={sensorInitializationOptions}
                />
              )}
            />
          </div>

          <OptionalField
            name={name}
            fieldName="previously_used"
            label="Previously used"
            tooltip={tooltips.previouslyUsed}
            renderChild={({ optionalFieldName }) => (
              <OptionField
                name={optionalFieldName}
                label="Previously used"
                tooltip={tooltips.previouslyUsed}
                options={previouslyUsedOptions}
              />
            )}
          />
        </div>

        <Supplier
          name={`${name}.supplier`}
          tooltip="Information about the supplier of the sensor"
          colorSchema="light"
        />
      </FormWrapper>
    </>
  );
}

export default Sensor;
