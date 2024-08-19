import React from "react";
import Constituent from "./Constituent";
import Solvent from "./Solvent";
import CustomField from "../../buildingBlocks/CustomField";
import ArrayField from "../../buildingBlocks/ArrayField";
import Ph from "./Ph";
import CreateUuid from "../../buildingBlocks/CreateUuid";

function ChemicalEnvironment({ name }) {
  CreateUuid(name);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          fieldName="name"
          label="Name"
          required
          tooltip="Name of the chemical environment (e.g. Measurement Buffer). The name must be unique within a record as it will be referred to in the method specific section when describing the composition of the individual samples or measurement steps"
          width="w-full"
        />
      </div>
      <div className="flex mb-3">
        <div className="mr-3">
          <Ph name={`${name}.ph`} />
        </div>
        <div className="-mt-3">
          <ArrayField
            name={name}
            label="Additional specification"
            fieldName="additional_specifications"
            tooltip="Additional information about the chemical environment can be specified here (e.g. prepared just prior to conducting the measurement, additional treatments like UV irradiation, specific storage container of chemical environment if that influenced the measurement etc.)"
            renderChild={({ arrayName, index }) => (
              <CustomField
                name={`${arrayName}.${index}`}
                label={`Additional specification ${index + 1}`}
                width="w-[15rem]"
                tooltip="Additional information about the chemical environment can be specified here (e.g. prepared just prior to conducting the measurement, additional treatments like UV irradiation, specific storage container of chemical environment if that influenced the measurement etc.)"
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <Solvent name={name} />
      </div>
      <div>
        <Constituent name={name} />
      </div>
    </>
  );
}

export default ChemicalEnvironment;
