import React from 'react';
import { useField } from 'formik';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Tooltip from '@material-ui/core/Tooltip';

function OptionField({ label, name, fieldName, options, width, tooltip}) {
  const nameOptionField = `${name}.${fieldName}`;
  const [field, meta] = useField(nameOptionField);

  return (
    <div className='flex'>
      <div className={`${width} rounded-lg relative border min-w-[178px]`}>
        <FormControl fullWidth>
          <InputLabel id={nameOptionField} htmlFor={nameOptionField}>
            {label}
          </InputLabel>
          <Select
            {...field}
            labelid={nameOptionField}
            id={nameOptionField}
            name={nameOptionField}
            value={field.value || ''}
            label={label}
            size="small"
            error={meta.touched && !!meta.error}
            sx= {{ 
              "& .MuiButton-outlined": "background-color: #6D7575" ,
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
          <Tooltip title={tooltip} arrow="true">
            <div>?</div>
          </Tooltip>
        </div>
      }
    </div>
  );
}

export default OptionField;