import Input from '@material-ui/core/Input';
import { useState } from 'react';
import { useField } from 'formik';
import Tooltip from '@material-ui/core/Tooltip';
import { useEffect } from 'react';
import { Typography } from '@material-ui/core';

function FileField({ name, fieldName, tooltip, width }) {
  const nameCustomField = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta, helpers] = useField(nameCustomField);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleChange = (e) => {
    e.preventDefault();
    const file = e.target.files[0];
    helpers.setValue(file);
    setSelectedFile(file);
  };

  useEffect(() => {
    console.log('Selected file:', selectedFile);
  }, [selectedFile]);

  return (
    <>
      <div className='flex'>
        <div className={`${width}`}>
          <Input
            type='file'
            className={`rounded-lg p-2 text-16px ${width}`}
            onChange={handleChange}
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

export default FileField;