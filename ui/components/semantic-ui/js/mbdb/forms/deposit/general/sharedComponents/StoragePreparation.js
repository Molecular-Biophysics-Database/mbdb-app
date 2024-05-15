import CustomField from "../../buildingBlocks/CustomField";

function StoragePreparation( { name } ) {

  return (
    <>
        <div className="flex">
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='name'
                    label='Name'
                    tooltip='Descriptive name of the step'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='description'
                    label='Description'
                    tooltip='Short description of the step'
                />
            </div>
        </div>
    </>
  );
}

export default StoragePreparation;