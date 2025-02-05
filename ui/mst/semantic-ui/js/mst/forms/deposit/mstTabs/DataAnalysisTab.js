import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import DataAnalysis from "../dataAnalysis/DataAnalysis";

export default function DataAnalysisTab({ name }) {
  const tooltip =
    "The details of how data analysis was performed to obtain the result";

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about how data analysis was performed
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Data analysis"
        fieldName="data_analysis"
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Data analysis ${index + 1}`}
            tooltip={tooltip}
          >
            <DataAnalysis name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
