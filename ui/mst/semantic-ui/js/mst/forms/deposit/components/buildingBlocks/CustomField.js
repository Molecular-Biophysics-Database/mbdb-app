import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useField } from 'formik';
import Tooltip from '@material-ui/core/Tooltip';

function CustomField( {label, name, fieldName, type, index, tooltip, width, multiline}) {

  const nameTextField = index !== undefined
  ? (fieldName !== undefined ? `${name}.${fieldName}[${index}]` : `${name}[${index}]`)
  : (fieldName !== undefined ? `${name}.${fieldName}` : `${name}`);
  
    const [field, meta] = useField(nameTextField);

  return (
    <>
      <div className='flex'>
        <div className={`${width}`}>
            <TextField
              {...field}
              className={`rounded-lg p-2 text-16px ${width}`}
              id={nameTextField}
              label={label}
              name={nameTextField}
              type={type}
              value={field.value || ''}
              disabled={false}
              variant="outlined"
              {...(multiline && { multiline: true })}
              size="small"
              error={meta.touched && !!meta.error}
            />
        </div>
        {tooltip &&
          <div className='ml-1 -mt-1'>
            <Tooltip title={tooltip} arrow="true">
              <div>?</div>
            </Tooltip>
          </div>
        }
      </div>
    </>
  );
}

export default CustomField;