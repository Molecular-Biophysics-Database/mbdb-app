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
              prefixTooltip="Hello"
              dbTooltip="world"
            />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ExternalDatabase;
