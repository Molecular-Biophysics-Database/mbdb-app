import TextField from '@mui/material/TextField';
import { useField } from 'formik';
import Tooltip from '@mui/material/Tooltip';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import InputAdornment from '@mui/material/InputAdornment';

function CustomField( {label, name, fieldName, type, index, tooltip, width, multiline, unit}) {

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
              id={nameTextField}
              label={label}
              name={nameTextField}
              type={type}
              value={field.value || ''}
              disabled={false}
              InputProps={{
                endAdornment: <InputAdornment position="end">{unit}</InputAdornment>
              }}
              variant="outlined"
              {...(multiline && { multiline: true })}
              size="small"
              error={meta.touched && !!meta.error}
            />
        </div>
        {tooltip &&
          <div className='ml-1 -mt-1'>
            <Tooltip title={tooltip} arrow>
              <HelpOutlineIcon fontSize="smaller"/>
            </Tooltip>
          </div>
        }
      </div>
    </>
  );
}

export default CustomField;