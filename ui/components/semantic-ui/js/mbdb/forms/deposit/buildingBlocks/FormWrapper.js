import { Tooltip } from '@mui/material';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';

function FormWrapper( { headline, children, colorSchema, tooltipHeader } ) {

return (
  <>                    
      <div className={`${colorSchema === 'light' ? 'bg-white' : 'bg-primary' } p-3 rounded-lg text-dark`}>
        {headline ?
          <div className="flex">
            <div className='font-JostMedium text-18px mb-2'>
              {headline}
            </div>
            {tooltipHeader ?
              <div className='ml-1 -mt-1'>
                <Tooltip title={tooltipHeader} arrow>
                  <HelpOutlineIcon fontSize="smaller"/>
                </Tooltip>
              </div>
              :
              ''
            }
          </div>
          :
          ''
        }
          {children}
      </div>  
  </>
);
}

export default FormWrapper;