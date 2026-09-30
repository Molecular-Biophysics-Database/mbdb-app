import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import {
  Checkbox,
  Confirm,
  FieldHelp,
  Form,
  Segment,
} from "mbdb-semantic-ui-react";
import { hasError, hasData } from "../errors";
import { useModelFieldData } from "../fieldData";

// A small optional object toggled by a checkbox in the header
// (design/building-blocks/ToggleFieldGroup.md).
export const ToggleFieldGroup = ({
  fieldPath,
  label,
  help,
  initialValue = {},
  children,
}) => {
  const { values, errors, setFieldValue } = useFormikContext();
  const [confirming, setConfirming] = useState(false);
  const data = useModelFieldData(fieldPath, { label, helpText: help });
  const text = data.label;

  const value = getIn(values, fieldPath);
  const checked = value !== undefined;

  const onToggle = (e, { checked: next }) => {
    if (next) setFieldValue(fieldPath, cloneDeep(initialValue));
    else if (hasData(value)) setConfirming(true);
    else setFieldValue(fieldPath, undefined);
  };

  return (
    <Form.Field error={hasError(errors, fieldPath)}>
      <Checkbox label={text} checked={checked} onChange={onToggle} />
      {data.helpText && <FieldHelp help={data.helpText} />}
      {checked && (
        <Segment basic className="mbdb-indent">
          {children}
        </Segment>
      )}
      <Confirm
        open={confirming}
        header={`Remove ${text}?`}
        content="This cannot be undone."
        confirmButton="Remove"
        onCancel={() => setConfirming(false)}
        onConfirm={() => {
          setConfirming(false);
          setFieldValue(fieldPath, undefined);
        }}
      />
    </Form.Field>
  );
};

ToggleFieldGroup.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  initialValue: PropTypes.object,
  children: PropTypes.node.isRequired,
};
