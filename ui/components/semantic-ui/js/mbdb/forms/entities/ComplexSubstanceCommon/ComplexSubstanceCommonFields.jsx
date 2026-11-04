import React from "react";
import PropTypes from "prop-types";
import { StringTableField } from "@js/mbdb/forms/building-blocks/StringTableField";
import { Protocol } from "@js/mbdb/forms/shared/Protocol";
import { Storage } from "@js/mbdb/forms/shared/Storage";

// The trailing block every complex-substance form shares, always in the same
// order: the preparation protocol (required, at least one step), an optional
// storage and the free-text specifications. Composition only, no logic of its
// own; every path is built from `fieldPath`. It is a fragment, so it also has
// its own story (design/index.md: every built component has one).
export const ComplexSubstanceCommonFields = ({ fieldPath }) => (
  <>
    <Protocol fieldPath={`${fieldPath}.preparation_protocol`} minItems={1} />
    <Storage fieldPath={`${fieldPath}.storage`} />
    <StringTableField
      fieldPath={`${fieldPath}.additional_specifications`}
      columnLabel="Specification"
      addButtonLabel="Add specification"
    />
  </>
);

ComplexSubstanceCommonFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
