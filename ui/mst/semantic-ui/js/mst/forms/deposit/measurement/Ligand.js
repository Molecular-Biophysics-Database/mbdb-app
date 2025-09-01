import React from "react";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Concentration from "@mbdb_deposit/sharedComponents/Concentration";
import { useFormikContext, getIn } from "formik";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

export default function Ligand({ name }) {
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
            options={entityOptions}
            label="Entity"
            fieldName="entity"
            required
            tooltip="List of names (ids) of entities (from the entities of interest defined in the record) that were used to alter the behavior of the target(s)"
          />
        </div>
        <Concentration
          name={`${name}.concentration`}
          colorSchema="light"
          tooltip="Concentration of the entity"
        />
      </div>
    </>
  );
}
