import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import OptionField from "../../buildingBlocks/OptionField";
import { useFormikContext, getIn } from "formik";
import CreateOptions from "../../buildingBlocks/CreateOptions";

export default function EntityInvolved({ name }) {
  const { values } = useFormikContext();

  const entityOptions = CreateOptions(
    getIn(values, "metadata.general_parameters.entities_of_interest"),
    "Select Entity, if applicable"
  );

  return (
    <>
      <div className="flex">
        <div className="mr-3">
          <OptionField
            name={name}
            required
            options={entityOptions}
            fieldName="entity"
            label="Entity"
            tooltip="Name (id) of the entity (from the entities of interest defined in the general parameters)"
          />
        </div>

        <CustomField
          name={name}
          required
          fieldName="copy_number"
          label="Copy number"
          type="number"
          tooltip="Number of copies of the entity that contribute to the result, -1 if unknown (e.g. if two metals ions binds independent of each other to a monomeric protein, the copy number would be 2 and 1 for the metal ions and protein, respectively)"
        />
      </div>
    </>
  );
}
