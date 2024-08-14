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
        tooltip="List of identifiers of records in external databases containing information about the polymer can be specified here (e.g UNIPROT:Q8KRF6)"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`External database ${index + 1}`}
            colorSchema={colorSchema}
            tooltip="List of identifiers of records in external databases containing information about the polymer can be specified here (e.g UNIPROT:Q8KRF6)"
          >
            <ExternalDatabaseField
              name={`${arrayName}.${index}`}
              prefixTooltip="Name of the external database in lowercase letters (e.g., pdb)"
              dbTooltip="the identifier on external database that you wish to refer to e.g. 1GWD"
            />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ExternalDatabase;
