import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import Volume from "../../../sharedComponents/Volume";

function InjectionParameter( { name } ) {

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='n_injections'
                label='N injections'
                type='number'
                tooltip=''
            />
        </div>
        <div>
            <Volume
                name={`${name}.volume`}
                colorSchema='light'
            />
        </div> 
    </>
  );
}

export default InjectionParameter;