import React from 'react';
import { getIn, useFormikContext } from 'formik';
import Tooltip from '@material-ui/core/Tooltip';
import { Typography } from '@material-ui/core';
import { Button } from "semantic-ui-react";

function OptionalField({ name, fieldName, label, renderChild, initialValue, tooltip }) {

  const { values, setFieldValue } = useFormikContext();
  const optionalFieldName = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const value = getIn(values, optionalFieldName);

    function remove() {
        setFieldValue(optionalFieldName, undefined);
    }

    function add() {
        if (initialValue) {
            setFieldValue(optionalFieldName, initialValue);
        } else {
            setFieldValue(optionalFieldName, '');
        }
    }

  return (
    <>
        {(value || value === '') && (
            <div className='flex mt-3'>
                <div className='mr-3'>
                    {renderChild({ optionalFieldName })}
                </div>
                <Button
                    style={{ backgroundColor: '#023850', color: 'white' }}
                    onClick={() => remove()}
                >
                    -
                </Button>
            
            </div>
        )}
        {(value === undefined || !value === '') && (
            <div className='mt-3'>
                <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
                    <Button
                        style={{ backgroundColor: '#023850', color: 'white' }}
                        onClick={() => add()}
                    >
                        + {`${label}`}
                    </Button>
                </Tooltip>
            </div>
        )}
    </>
  );
}

export default OptionalField;