import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Form, Label } from "mbdb-semantic-ui-react";
import { hasData } from "@js/mbdb/forms/building-blocks/errors";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { ToggleFieldGroup } from "@js/mbdb/forms/building-blocks/ToggleFieldGroup";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";
import {
  FINGERPRINTING_METHODS,
  INTACT_MASS_METHODS,
  SEQUENCING_METHODS,
} from "./constants";

const METHOD_KEYS = ["by_intact_mass", "by_sequencing", "by_fingerprinting"];

// Shown under the Identity row of QualityControls when "Yes" is selected:
// three optional methods, each a checkbox that reveals its fields.
export const IdentityFields = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const identity = getIn(values, fieldPath) ?? {};
  // computed during render from the values — the hint is not an error (the
  // model does not require any of the three)
  const noMethod = !METHOD_KEYS.some((key) => hasData(identity[key]));
  return (
    <>
      <ToggleFieldGroup fieldPath={`${fieldPath}.by_intact_mass`}>
        <Form.Group widths="equal">
          <SelectField
            fieldPath={`${fieldPath}.by_intact_mass.method`}
            options={INTACT_MASS_METHODS}
          />
          <MolecularWeight
            fieldPath={`${fieldPath}.by_intact_mass.deviation_from_expected_mass`}
            defaultUnit="Da"
          />
        </Form.Group>
      </ToggleFieldGroup>
      <ToggleFieldGroup fieldPath={`${fieldPath}.by_sequencing`}>
        <Form.Group widths="equal">
          <SelectField
            fieldPath={`${fieldPath}.by_sequencing.method`}
            options={SEQUENCING_METHODS}
          />
          <NumberField
            fieldPath={`${fieldPath}.by_sequencing.coverage`}
            min={0}
            max={100}
          />
        </Form.Group>
      </ToggleFieldGroup>
      <ToggleFieldGroup fieldPath={`${fieldPath}.by_fingerprinting`}>
        <SelectField
          fieldPath={`${fieldPath}.by_fingerprinting.method`}
          options={FINGERPRINTING_METHODS}
        />
      </ToggleFieldGroup>
      {noMethod && (
        // a block wrapper so the hint does not sit tight against the last
        // toggle's checkbox
        <div>
          <Label basic color="yellow">
            Select at least one method, or choose No.
          </Label>
        </div>
      )}
    </>
  );
};

IdentityFields.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
