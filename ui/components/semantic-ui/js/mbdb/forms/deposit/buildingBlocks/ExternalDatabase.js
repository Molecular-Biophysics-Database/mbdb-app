import React from "react";
import FormWrapper from "./FormWrapper";
import ArrayField from "./ArrayField";
import ExternalDatabaseField from "./ExternalDatabaseField";

function ExternalDatabase({ name, colorSchema }) {
  return (
    <>
      <ArrayField
        name={name}
        label="External Database"
        fieldName="external_databases"
        tooltip="List of identifiers to records in external databases containing information about the polymer can be specified here (e.g UNIPROT:Q8KRF6)"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`External database ${index + 1}`}
            colorSchema={colorSchema}
          >
            <ExternalDatabaseField
              name={`${arrayName}.${index}`}
              dbTooltip="hello"
              prefixTooltip="tokfdjs"
            />
            {/*
              <CustomField
                name={`${arrayName}.prefix.${index}`}
                label="Prefix"
                width="w-[7rem]"
                tooltip="List of identifiers to records in external databases containing information about the polymer can be specified here (e.g UNIPROT:Q8KRF6)"
              />
              <CustomField
                name={`${arrayName}.${index}`}
                label="External database"
                width="w-[15rem]"
                tooltip="List of identifiers to records in external databases containing information about the polymer can be specified here (e.g UNIPROT:Q8KRF6)"
              />
              
              */}
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ExternalDatabase;
