import React from "react";
import PropTypes from "prop-types";
import { FieldRow } from "@js/mbdb/forms/building-blocks/FieldRow";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { Size } from "@js/mbdb/forms/shared/Size";
import { Components } from "@js/mbdb/forms/shared/Components";
import { ASSEMBLY_TYPES } from "./constants";

// The fields specific to a lipid assembly: plain fields in the entity modal,
// directly after the "Class: Lipid assembly" text (design
// LipidAssemblyDetails). `fieldPath` is the entity item path — these fields
// sit directly on the item, unlike the other step 3 blocks which take their
// own object or array path.
export const LipidAssemblyDetails = ({ fieldPath }) => (
  <>
    <FieldRow widths="equal">
      {/* assembly_type is required, so its buttons cannot be toggled off
          (ButtonGroupField); that is not a trap, it is required for every
          lipid assembly */}
      <ButtonGroupField
        fieldPath={`${fieldPath}.assembly_type`}
        options={ASSEMBLY_TYPES}
      />
      <NumberField
        fieldPath={`${fieldPath}.number_of_mono_layers`}
        integer
        min={-1}
      />
    </FieldRow>
    <Size fieldPath={`${fieldPath}.size`} />
    <Components fieldPath={`${fieldPath}.components`} />
  </>
);

LipidAssemblyDetails.propTypes = {
  // the entity item path (the fields sit directly on it)
  fieldPath: PropTypes.string.isRequired,
};
