import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

import Sample from "./Sample";

function Measurement( { name } ) {

    CreateUuid(name);

    return (
    <>
        <div className='flex mb-3'>
          <div className="mr-3">
            <CustomField
                name={name}
                label='Name'
                fieldName='name'
                required={true}
                tooltip='Name (id) of the measurement which must be unique within a record (i.e. triplicates must be named individually in the raw data file). The name must allow location of the measurement data within the raw data file as well as processed data files if these are present'
            />
          </div>
          <div>
            <CustomField
                name={name}
                label='Positon'
                fieldName='position'
                required={true}
                tooltip='Position where the container (capillary) of the measured sample within the instrument (e.g. 1, 2, 3)'
            />
          </div>
        </div>
        <div>
            <Sample
                name={`${name}.sample`}
                colorSchema='light'
                tooltip='Information about the sample including concentrations of ligands and targets, and which chemical environment the sample was composed of'
            />
        </div>
    </>
  );
}

export default Measurement;