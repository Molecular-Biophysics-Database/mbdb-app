import React from 'react';
import { FieldArray, getIn, useFormikContext } from 'formik';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';
import { Typography } from '@material-ui/core';
import { v4 as uuidv4 } from 'uuid';

function ArrayField({
  name,
  fieldName,
  label,
  renderChild,
  initialValue,
  required,
  maxItems,
  tooltip,
  uuid
}) {

  const { values } = useFormikContext();

  const handlePush = (push) => {
    const newItem = initialValue !== undefined ? { ...initialValue } : uuid ? { id: uuidv4() } : undefined;
    push(newItem);
  };

  const arrayName = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const value = getIn(values, arrayName);

  return (
    <div>
      <FieldArray
        name={arrayName}
        render={({ push, remove }) => ( 
          <>
            {value && (
              value.map((item, index) => (
                <div key={index} className='flex mt-3'>
                  <div className='mr-3'>
                    {renderChild({ arrayName, name, index })}
                  </div>
                  { (!required || index > 0 ) && 
                    <Button
                      type='button'
                      className='text-dark'
                      variant="outlined"
                      onClick={() => remove(index)}
                      sx= {{ 
                        borderColor: '#023850',
                        backgroundColor: '#023850',
                        color: '#fff',
                        "&:hover": {
                          borderColor: "#023850",
                          backgroundColor: '#023850',
                          color: '#fff',
                        },
                      }}
                    >
                      <div>
                        -
                      </div>
                    </Button>
                  }
                </div>
              ))
            )}
            {(!maxItems || (!value || value.length < maxItems)) &&
                <div className='mt-3'>
                  <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
                    <Button
                      variant="outlined"
                      onClick={() => handlePush(push)}
                      sx= {{ 
                          borderColor: '#023850',
                          backgroundColor: '#023850',
                          color: '#fff',
                          "&:hover": {
                            borderColor: "#023850",
                            backgroundColor: '#023850',
                            color: '#fff',
                          },
                      }}
                    >
                      + {`${label}`}
                    </Button>
                  </Tooltip>
                </div>
            }
          </>
        )}
      />
    </div>
  );
}

export default ArrayField;