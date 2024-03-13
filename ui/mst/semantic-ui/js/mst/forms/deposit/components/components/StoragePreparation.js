import React from 'react';
import CustomField from '../buildingBlocks/CustomField';
import FormWrapper from '../buildingBlocks/FormWrapper';

function StoragePreparation( {colorSchema, name} ) {

  return (
    <>
        <FormWrapper colorSchema={colorSchema} headline='Storage preparation'>
            <div className='flex'>
                <div className='mr-3'>
                    <CustomField
                        name={name}
                        label='Name'
                        fieldName='name'
                        width='w-[10rem]'
                    />
                </div>
                <div>
                    <CustomField
                        name={name}
                        label='Description'
                        fieldName='description'
                        width='w-[37rem]'
                    />
                </div>
            </div>
        </FormWrapper>
    </>
  );
}

export default StoragePreparation;