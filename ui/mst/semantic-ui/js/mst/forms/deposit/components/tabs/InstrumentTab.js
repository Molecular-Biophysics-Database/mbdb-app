import React from 'react';
import Tooltip from '@material-ui/core/Tooltip';
import CustomField from "../buildingBlocks/CustomField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import Instrument from "../instrument/Instrument";
import MethodSpecificParameters from "../instrument/MethodSpecificParameters";

function InstrumentTab( { name } ) {

    return (
      <>
          <div>
            <div className="mb-3">
                <Instrument name={`${name}.instrument`} />
            </div>
            <FormWrapper>
                <div className="flex">
                    <div className="flex">
                        <div className="mr-3 my-auto text-dark">
                            Collection start time
                        </div>
                        <div className='-mt-1 -ml-2 mr-3'>
                            <Tooltip title='The date when collection of the raw data began' arrow="true">
                                <div>?</div>
                            </Tooltip>
                        </div>
                    </div>
                    <div>
                        <CustomField
                            name={name}
                            type='date'
                            fieldName='collection_start_time'
                        />
                    </div>
                </div>
            </FormWrapper>
            <div className="mt-3">
                <MethodSpecificParameters name='metadata.method_specific_parameters' />
            </div>
          </div>
      </>
    );
  }
  
  export default InstrumentTab;