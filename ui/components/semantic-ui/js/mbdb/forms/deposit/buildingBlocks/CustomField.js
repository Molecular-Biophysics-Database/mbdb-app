import React from "react";
import TextField from '@material-ui/core/TextField';
import { useField } from 'formik';
import Tooltip from '@material-ui/core/Tooltip';
import { Typography } from '@material-ui/core';

function CustomField( { label, name, fieldName, type, tooltip, width, multiline }) {

  const nameCustomField = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta] = useField(nameCustomField);

  return (
    <>
      <div className='flex'>
        <div className={`${width}`}>
            <TextField
              {...field}
              className={`rounded-lg p-2 text-16px ${width}`}
              sx= {{
                "& .MuiInputLabel-root": {color: '#034459'}, //styles the label
                "& .MuiOutlinedInput-root": {
                  "& > fieldset": {color: '#034459'},
                },
                borderColor: '#666666',
                color: '#034459',
                "&:hover": {
                  borderColor: '#666666',
                },
              }}
              label={label}
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
            <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
              ?
            </Tooltip>
          </div>
        }
      </div>
    </>
  );
}

export default CustomField;