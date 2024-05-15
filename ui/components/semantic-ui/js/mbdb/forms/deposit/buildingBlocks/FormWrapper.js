import { Tooltip } from '@material-ui/core';
import { Typography } from '@material-ui/core';

function FormWrapper( { headline, children, colorSchema, tooltip } ) {

return (
  <>
      <div className={`${colorSchema === 'light' ? 'bg-white' : 'bg-primary' } p-3 rounded-lg text-dark`}>
        {headline &&
          <div className="flex">
            <div className='font-JostMedium text-18px mb-2'>
              {headline}
            </div>
            {tooltip &&
              <div className='ml-1 -mt-1'>
                <Tooltip title={<Typography fontSize={13}>{tooltip}</Typography>} arrow>
                  ?
                </Tooltip>
              </div>
            }
          </div>
        }
          {children}
      </div>
  </>
);
}

export default FormWrapper;