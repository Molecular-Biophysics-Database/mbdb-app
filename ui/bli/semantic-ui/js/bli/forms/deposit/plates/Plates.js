import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Supplier from "../sharedComponents/Supplier";
import SurfaceModification from "./SurfaceModification";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

function Plates({ name }) {
  const tooltips = {
    type: "The type of the plate (e.g. half-area black polystyrene)",
    sealing: "The type of sealing used to seal the top of the plate",
    supplier: "Information about the supplier of the plate",
  };

  const wellsOptions = [
    { value: "96", label: "96" },
    { value: "384", label: "384" },
  ];

  CreateUuid(name);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          fieldName="name"
          label="Name"
          required
          tooltip="Name (id) of the plate which must be unique within a record"
          width="w-full"
        />
      </div>
      <div className="flex mb-3">
        <div className="mr-3">
          <OptionField
            name={name}
            label="Wells"
            fieldName="wells"
            options={wellsOptions}
            required
            tooltip="Number of wells in the plate"
          />
        </div>
        <div className="-mt-3 mr-3">
          <OptionalField
            name={name}
            label="Type"
            fieldName="type"
            tooltip={tooltips.type}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Type"
                tooltip={tooltips.type}
              />
            )}
          />
        </div>
        <div className="-mt-3">
          <OptionalField
            name={name}
            label="Sealing"
            fieldName="sealing"
            tooltip={tooltips.sealing}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Sealing"
                tooltip={tooltips.sealing}
              />
            )}
          />
        </div>
      </div>
      <OptionalField
        name={name}
        label="Supplier"
        fieldName="supplier"
        tooltip={tooltips.supplier}
        renderChild={({ optionalFieldName }) => (
          <Supplier
            name={optionalFieldName}
            colorSchema="light"
            tooltip={tooltips.supplier}
          />
        )}
      />

      <OptionalField
        name={name}
        label="Surface modification"
        fieldName="surface_modification"
        tooltip="If the plate had a modified surface, the modification can specified here (e.g. Non-binding surface)"
        renderChild={({ optionalFieldName }) => (
          <SurfaceModification name={optionalFieldName} colorSchema="light" />
        )}
      />
    </>
  );
}

export default Plates;
