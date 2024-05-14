import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import RawDataFile from "../rawDataFiles/RawDataFile";

function RawDataFilesTab( { name } ) {

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Raw data file"
                fieldName='raw_data_file'
                tooltip='List of file(s) containing the raw measurements'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Raw data file ${index + 1}`}
                        tooltip='List of file(s) containing the raw measurements'
                    >
                        <div>
                            <RawDataFile
                                name={`${arrayName}.${index}`}
                            />
                        </div>
                    </FormWrapper>
                )}
            />
        </div>
      </>
    );
  }
  
  export default RawDataFilesTab;