import React from 'react';
import FormWrapper from '../buildingBlocks/FormWrapper';
import CustomField from '../buildingBlocks/CustomField';

function Location( { name, tooltipHeader, colorSchema } ) {

  return (
    <>
        <FormWrapper headline='Location' colorSchema={colorSchema} tooltipHeader={tooltipHeader}>
            <div className='flex'>
                <div className='mr-3'>
                    <CustomField
                        name={name}
                        label='Latitude'
                        fieldName='latitude'
                        tooltip='The latitude, from south to north, in degrees (decimal notation)'
                    />
                </div>
                <div>
                    <CustomField
                        name={name}
                        label='Longitude'
                        fieldName='longitude'
                        tooltip='The longitude, from west to east, in degrees (decimal notation)'
                    />
                </div>
            </div>
        </FormWrapper>
    </>
  );
}

export default Location;