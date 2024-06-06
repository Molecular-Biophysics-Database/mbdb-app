import React from "react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import { useFormikContext, useField } from "formik";
import { useDepositApiClient } from "@js/oarepo_ui";
import { useFormConfig } from "@js/oarepo_ui";

async function SubmitFile(values, file, index) {
  if (!file) return ({ code: 400, errors: ["No file selected."] });

  const fileName = file.name;

  // Submit the file name
  let resp = await fetch(values?.links?.files, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify([{ key: fileName }])
  });

  if (!resp.ok) {
      return ({ code: resp.status, errors: [`Failed to submit file "${fileName}": ${resp.statusText}`] });
  }

  const response = await resp.json();

  // Upload the file content
  resp = await fetch(response.entries[index].links.content, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/stream-octet'
      },
      body: file
  });

  if (!resp.ok) {
      return ({ code: resp.status, errors: [`Failed to upload content of file "${fileName}": ${resp.statusText}`] });
  }

  // Commit the result
  resp = await fetch(response.entries[index].links.commit, {
      method: 'POST'
  });

  if (!resp.ok) {
      return ({ code: resp.status, errors: [`Failed to commit uploaded file "${fileName}": ${resp.statusText}`] });
  }

  return (void 0);
}

function FileField({ name, fieldName, tooltip, width, required, index }) {
  const nameCustomField = fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const [field, meta, helpers] = useField(nameCustomField);
  const { values, setFieldValue } = useFormikContext();
  const { save } = useDepositApiClient();
  const { files: recordFiles } = useFormConfig();

  console.log(values, 'Formik values')

  console.log(recordFiles, 'RecordFiles');

  const handleOnClick = () => {
    if(!values.id) {
      save(true);
    }
  }

  const handleChange = (e, index) => {
    const file = e.target.files[0];
    SubmitFile(values, file, index);
    if(file) {
      console.log('File found')
      setFieldValue(`${nameCustomField}.name`, file.name);
    }
  };

  return (
    <>
      <div className='flex'>
        <div className={`${width}`}>
          
          <input
            type='file'
            className={`rounded-lg p-2 text-16px ${width}`}
            onChange={(e) => handleChange(e, index)}
            onClick={handleOnClick}
            size="small"
            error={meta.touched && !!meta.error}
          />
        </div>
        {required &&
          <div className='text-accent ml-1'>
            <Tooltip title={<Typography fontSize={13}>This field is required and cannot be left blank or unset</Typography>} arrow>
              <span>*</span>
            </Tooltip>
          </div>
        }
        {tooltip &&
          <div className='ml-1 -mt-1'>
            <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
              <span>?</span> 
            </Tooltip>
          </div>
        }
      </div>
    </>
  );
}

export default FileField;
