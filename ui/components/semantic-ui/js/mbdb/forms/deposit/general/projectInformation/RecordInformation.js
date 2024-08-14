import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
//import OptionField from "../../buildingBlocks/OptionField";

function RecordInformation({ name }) {
  // Currently (2024-08-07), the only implemented access type is the open access, so these fields are set automatically
  /*
  const accessRightsOptions = [
    { value: "open access", label: "Open access" },
    { value: "embargoed access", label: "Embargoed access" },
    { value: "restricted access", label: "Restricted access" },
  ];

  const metadataAccessRightsOptions = [
    { value: "open access", label: "Open access" },
    { value: "embargoed access", label: "Embargoed access" },
    { value: "restricted access", label: "Restricted access" },
  ];
*/
  return (
    <>
      <FormWrapper>
        <div className="flex">
          <div className="mr-3">
            <CustomField
              name={name}
              fieldName="title"
              label="Title"
              required
              width="w-[1110px]"
              tooltip="Short descriptive title of the record"
            />
          </div>
          {/*
          <div className="mr-3">
            <OptionField
              options={accessRightsOptions}
              name={name}
              fieldName="access_rights"
              label="Access rights"
              required
              width="w-[14rem]"
              tooltip='The access rights to the uploaded files. There are three options, 1) "open access" where the files are accessible immediately when the deposition is published, 2) "embargoed access" where the files will only become available after a specified date, 3) "restricted access" where depositors are of the record are the only ones who has access'
            />
          </div>
          <div>
            <OptionField
              options={metadataAccessRightsOptions}
              name={name}
              fieldName="metadata_access_rights"
              label="Metadata access rights"
              required
              width="w-[14rem]"
              tooltip='The access rights to the metadata. Minimal metadata that includes title and depositors is accessible regardless of which type is chosen as it is required to obtain a DOI. There are three options, 1) "open access" where the complete metadata are accessible immediately when the deposition is published, 2) "embargoed access" where the files will only become available after a specified date, 3) "restricted access" where depositors are of the record are the only ones who has access'
            />
          </div>
        */}
        </div>
      </FormWrapper>
    </>
  );
}

export default RecordInformation;
