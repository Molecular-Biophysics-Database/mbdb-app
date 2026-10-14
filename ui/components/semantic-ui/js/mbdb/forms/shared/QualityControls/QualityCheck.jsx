import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Segment } from "mbdb-semantic-ui-react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { ASSESSED } from "./constants";

// One quality-control row (Purity / Identity / Homogeneity): a
// Not specified / Yes / No button group; Yes reveals the check's fields
// directly below the row. The Yes fields live in the PARENT's children, so
// they render under the buttons.
export const QualityCheck = ({ fieldPath, children }) => {
  const { values } = useFormikContext();
  // The row is labelled by the check ("Purity"), not by its discriminator
  // ("Assessed"): both texts come from the model, read one level up.
  // (guide §6 override, with the reason here.)
  const check = useModelFieldData(fieldPath);
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="assessed"
        options={ASSESSED}
        variant="buttons"
        allowUnset
        keep={[]}
        label={check.label}
        help={check.helpText}
        // assessed is required only once the check exists; "Not specified"
        // (absent) is allowed, so no required marker
        required={false}
      />
      {getIn(values, `${fieldPath}.assessed`) === "Yes" && (
        <Segment basic className="mbdb-indent">
          {children}
        </Segment>
      )}
    </>
  );
};

QualityCheck.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};
