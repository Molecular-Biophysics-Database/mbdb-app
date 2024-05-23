import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import LigandInformation from "@mbdb_deposit/sharedComponents/LigandInformation";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function MeasurementPositions( { name } ) {

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='name'
                label='Name'
                tooltip='Name of the measurement spot'
                width='w-full'
            />
        </div>
        <div className="flex mb-3">
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='flow_cell'
                    label='Flow cell'
                    tooltip='The flow cell where the measurement spot is located'
                />
            </div>
            <div className="-mt-3 mr-5">
                <OptionalField
                    name={name}
                    fieldName='position'
                    label='Position'
                    tooltip='Position of the measurement spot within the flow cell'
                    renderChild={({ optionalFieldName }) => (
                        <CustomField
                            name={optionalFieldName}
                            label='Position'
                            tooltip='Position of the measurement spot within the flow cell'
                        />
                    )}
                />
            </div>
        </div>
        <div>
            <OptionalField
                name={name}
                label='Ligand information'
                fieldName='ligand_information'
                tooltip='Information about the ligand and how it was immobilized'
                renderChild={({ optionalFieldName }) => (
                    <LigandInformation
                        name={optionalFieldName}
                        colorSchema='light'
                    />
                )}
            />
        </div>
    </>
  );
}

export default MeasurementPositions;