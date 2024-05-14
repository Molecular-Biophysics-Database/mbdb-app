import React from 'react';
import { getIn, useFormikContext } from 'formik';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';
import { Typography } from '@material-ui/core';

function OptionalField({ name, fieldName, label, renderChild, initialValue, tooltip }) {

  const { values, setFieldValue } = useFormikContext();
  const optionalFieldName = `${name}.${fieldName}`;
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
                    type='button'
                    className='text-dark'
                    variant="outlined"
                    onClick={() => remove()}
                    sx= {{ 
                        borderColor: '#6D7575',
                        backgroundColor: '#6D7575',
                        color: '#fff',
                        "&:hover": {
                        borderColor: "#939E9D",
                        backgroundColor: '#939E9D',
                        color: '#fff',
                        },
                    }}
                    >
                    <div>
                        -
                    </div>
                </Button>
            
            </div>
        )}
        {(value === undefined || !value === '') && (
            <div className='mt-3'>
                <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
                    <Button
                        variant="outlined"
                        onClick={() => add()}
                        sx= {{ 
                            borderColor: '#6D7575',
                            backgroundColor: '#6D7575',
                            color: '#fff',
                            "&:hover": {
                                borderColor: "#939E9D",
                                backgroundColor: '#939E9D',
                                color: '#fff',
                            },
                        }}
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