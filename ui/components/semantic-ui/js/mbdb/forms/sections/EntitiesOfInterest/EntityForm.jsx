import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { ENTITY_SEEDS } from "@js/mbdb/forms/entities/seeds";
import { ENTITY_TYPES, ENTITY_TYPE_ORDER } from "./entityTypes";

// The content of the entity modal: Type (a dropdown discriminator; changing it
// asks for confirmation, keeps only `id`, and writes the new type's seed),
// Name, then the type-specific form. Once a type is set the fields are always
// present (the item is created from a seed), so there is no unknown-type case.
export const EntityForm = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const type = getIn(values, `${fieldPath}.type`);
  const Fields = ENTITY_TYPES[type]?.Fields;
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="type"
        options={ENTITY_TYPE_ORDER}
        variant="dropdown"
        keep={["id"]}
        seed={(newType) => ENTITY_SEEDS[newType]}
      />
      <TextField fieldPath={`${fieldPath}.name`} />
      {Fields ? <Fields fieldPath={fieldPath} /> : null}
    </>
  );
};

EntityForm.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
