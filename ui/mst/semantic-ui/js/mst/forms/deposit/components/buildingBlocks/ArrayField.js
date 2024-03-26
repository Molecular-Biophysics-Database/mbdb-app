import React from 'react';
import { FieldArray, getIn, useFormikContext } from 'formik';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';

function ArrayField({ name, fieldName, label, renderChild, initialValue, required, maxItems, tooltip }) {

  const { values } = useFormikContext();

  const arrayName = `${name}.${fieldName}`;
  const value = getIn(values, arrayName);

  return (
    <div>
      <FieldArray
        name={arrayName}
        render={({ push, remove }) => ( 
          <>
            {Array.isArray(value) && (
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
                        &#8212;
                      </div>
                    </Button>
                  }
                </div>
              ))
            )}
            {(!maxItems || (!value || value.length < maxItems)) &&
                <div className='mt-3'>
                  <Tooltip title={tooltip} arrow="true">
                    <Button
                      className='text-dark'
                      variant="outlined"
                      onClick={() => push(initialValue !== undefined ? { ...initialValue } : '')}
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
            }
          </>
        )}
      />
    </div>
  );
}

export default ArrayField;