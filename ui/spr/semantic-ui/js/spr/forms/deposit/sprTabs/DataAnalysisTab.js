import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import DataAnalysis from "@mbdb_deposit/sharedComponents/DataAnalysis";

function DataAnalysisTab( { name } ) {

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Data analysis"
                fieldName='data_analysis'
                tooltip='The details of how data analysis was performed to obtain results'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Data analysis ${index + 1}`}
                        tooltip='The details of how data analysis was performed to obtain results'
                    >
                        <div>
                            <DataAnalysis
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
  
  export default DataAnalysisTab;