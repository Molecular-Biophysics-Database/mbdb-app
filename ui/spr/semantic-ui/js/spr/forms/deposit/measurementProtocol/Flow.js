import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import Path from "./Path";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";

function Flow( { colorSchema, name } ) {

    const unitOptions = [
        { value: 'mL/min', label: 'mL/min' },
        { value: 'µl/s', label: 'µl/s' },
      ];

    const directionOptions = [
        { value: 'Vertical', label: 'Vertical' },
        { value: 'Horizontal', label: 'Horizontal' },
    ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline='Flow'
        tooltip='Information about the flow during the measurement step'>
            <div className="flex">
                <div className="-mt-3 mr-3">
                    <ArrayField
                        name={name}
                        label='Path'
                        fieldName='path'
                        tooltip='list of the flow-path, in terms of measurement positions. Measurement positions that are connected by a flow running serially through them should be mentioned within the inner list, while parallel flows should be mentioned in the outer list'
                        renderChild={({ arrayName, index }) => (
                            <FormWrapper
                                headline={`Path ${index + 1}`}
                                tooltip='list of the flow-path, in terms of measurement positions. Measurement positions that are connected by a flow running serially through them should be mentioned within the inner list, while parallel flows should be mentioned in the outer list'
                            >
                                <Path
                                    name={`${arrayName}.${index}`}
                                />
                            </FormWrapper>
                        )}
                    />
                </div>
                <div className="mr-3">
                    <CustomField
                        name={name}
                        fieldName='rate'
                        label='Rate'
                        required={true}
                        tooltip='Numerical value of the flow-rate'
                        type='number'
                    />
                </div>
                <div className="mr-3">
                    <OptionField
                        name={name}
                        fieldName='unit'
                        label='Unit'
                        required={true}
                        tooltip='The unit of the flow-rate'
                        options={unitOptions}
                    />
                </div>
                <div className="-mt-3">
                    <OptionalField
                        name={name}
                        label='Direction'
                        fieldName='direction'
                        tooltip='Direction of the flow'
                        renderChild={({ optionalFieldName }) => (
                            <OptionField
                                name={optionalFieldName}
                                label='Direction'
                                tooltip='Direction of the flow'
                                options={directionOptions}
                            />
                        )}
                    />
                </div>
            </div>
      </FormWrapper>
    </>
  );
}

export default Flow;