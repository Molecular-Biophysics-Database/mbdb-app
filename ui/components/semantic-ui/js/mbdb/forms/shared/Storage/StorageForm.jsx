import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { Protocol } from "@js/mbdb/forms/shared/Protocol";
import { TEMPERATURE_UNITS, TIME_UNITS } from "@js/mbdb/forms/shared/units";

// The storage modal content: temperature (required once storage exists) and
// duration side by side, plus optional preparation steps. Labels, help and
// required come from the model. durations's min reaches the number input
// (spinner only; the server checks the minimum); temperature has none —
// Celsius users type negative numbers.
export const StorageForm = ({ fieldPath }) => (
  <>
    <Form.Group widths="equal">
      <ValueUnitField
        fieldPath={`${fieldPath}.temperature`}
        units={TEMPERATURE_UNITS}
        defaultUnit="°C"
      />
      <ValueUnitField
        fieldPath={`${fieldPath}.duration`}
        units={TIME_UNITS}
        defaultUnit="days"
        min={0}
      />
    </Form.Group>
    <Protocol fieldPath={`${fieldPath}.storage_preparation`} />
  </>
);

StorageForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
