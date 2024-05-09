import React from 'react';
import { useField } from 'formik';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { Tooltip } from '@mui/material';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';

function OptionField({ label, name, fieldName, options, width, tooltip}) {
  const nameOptionField = `${name}.${fieldName}`;
  const [field, meta] = useField(nameOptionField);

  return (
    <div className='flex'>
      <Box className={`${width} rounded-lg relative`} sx={{ minWidth: 195 }}>
        <FormControl fullWidth>
          <InputLabel id={nameOptionField} htmlFor={nameOptionField}>
            {label}
          </InputLabel>
          <Select
            {...field}
            labelId={nameOptionField}
            id={nameOptionField}
            name={nameOptionField}
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
      </Box>
      {tooltip ?
        <div className='ml-1 -mt-1'>
          <Tooltip title={tooltip} arrow>
            <HelpOutlineIcon fontSize="smaller"/>
          </Tooltip>
        </div>
        :
        <div className='w-5'>
        </div>
      }
    </div>
  );
}

export default OptionField;