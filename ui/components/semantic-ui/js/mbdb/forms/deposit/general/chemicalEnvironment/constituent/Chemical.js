import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";

function Chemical( { name } ) {

  return (
    <>
      <div className='flex'>
          <div className='mr-3'>
            <CustomField
              name={name}
              label='Basic information'
              fieldName='basic_information'
              tooltip='The basic information about the chemical. This information is pulled from Pubchem, however if the information is not available it can be manually filled'
            />
          </div>
          <div className="-mt-3 mr-5">
              <ArrayField
                  name={name}
                  label='Additional specification'
                  fieldName='additional_specifications'
                  tooltip='Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)'
                  renderChild={({ arrayName, index }) => (
                      <CustomField
                          name={`${arrayName}.${index}`}
                          label={`Additional specification ${index + 1}`}
                          width='w-[15rem]'
                          tooltip='Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)'
                      />
                  )}
              />
          </div>
      </div>
    </>
  );
}

export default Chemical;