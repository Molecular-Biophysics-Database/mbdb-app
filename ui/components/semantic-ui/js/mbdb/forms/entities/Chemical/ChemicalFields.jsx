import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { StringTableField } from "@js/mbdb/forms/building-blocks/StringTableField";
import { BasicInformation } from "@js/mbdb/forms/shared/BasicInformation";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";

// The content of a chemical's entity modal, after Type and Name: the
// PubChem-backed picker and the free-text specifications. Reused as a
// component's field set (ComponentChemical), so it assumes nothing about
// where it sits — every path is built from `fieldPath`.
export const ChemicalFields = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  // Prefill an empty Name with the picked chemical's title (lead decision
  // 2026-10-03, design Chemical "prefill Name"): it happens here, in the pick
  // handler, never in an effect, and a non-empty name is left untouched.
  const onPicked = (suggestion) => {
    if (!isEmptyValue(getIn(values, `${fieldPath}.name`))) return;
    const title =
      suggestion.title_l10n ?? suggestion.title?.en ?? suggestion.title;
    if (typeof title === "string" && title !== "")
      setFieldValue(`${fieldPath}.name`, title);
  };
  return (
    <>
      <BasicInformation
        fieldPath={`${fieldPath}.basic_information`}
        onPicked={onPicked}
      />
      <StringTableField
        fieldPath={`${fieldPath}.additional_specifications`}
        columnLabel="Specification"
        addButtonLabel="Add specification"
      />
    </>
  );
};

ChemicalFields.propTypes = {
  // the entity item path (or a component item path)
  fieldPath: PropTypes.string.isRequired,
};
