import React from 'react';
import { useField } from 'formik';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import { Tooltip } from '@material-ui/core/Tooltip';
import { Typography } from '@material-ui/core';

function OptionField({ label, name, fieldName, options, width, tooltip}) {

  const nameOptionField = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`
  const [field, meta] = useField(nameOptionField);

  return (
    <div className='flex'>
      <div className={`${width} rounded-lg relative`} sx={{ minWidth: 195 }}>
        <FormControl fullWidth>
          <InputLabel>
            {label}
          </InputLabel>
          <Select
            {...field}
            value={field.value || ''}
            label={label}
            size="small"
            error={meta.touched && !!meta.error}
            sx= {{ 
              //"& .MuiOutlinedInput-notchedOutline": {
              //  borderColor: "#034459",
              //},
              "& .MuiInputLabel-root": {color: '#034459'}, //styles the label
              color: '#034459',
              "&:hover": {
                borderColor: "#034459",
              },
            }}
          >
            {options.map((option) => (
              <MenuItem key={option.value} value={option.value} >
                {option.label}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </div>
      {tooltip &&
        <div className='ml-1 -mt-1'>
          <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
            ?
          </Tooltip>
        </div>
      }
    </div>
  );
}

export default OptionField;