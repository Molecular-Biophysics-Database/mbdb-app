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
import {
  hasData,
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// A small optional object toggled by a checkbox in the header
// (design/building-blocks/ToggleFieldGroup.md).
export const ToggleFieldGroup = ({
  fieldPath,
  label,
  help,
  initialValue = {},
  children,
}) => {
  const { values, setFieldValue } = useFormikContext();
  const [confirming, setConfirming] = useState(false);
  // F2: an explicit local "open" so checking does not have to write `{}` into
  // Formik (guide §7). checked = a value exists OR the user just opened it.
  const [open, setOpen] = useState(false);
  const data = useModelFieldData(fieldPath, { label, helpText: help });
  const text = data.label;
  // F1: red header reads errors ∪ initialErrors so it survives edits
  const { hasError } = useFieldErrors(fieldPath);
  // object-level messages only (a string sitting exactly at fieldPath, F4)
  const objectMessages = useOwnErrorMessages(fieldPath);

  const value = getIn(values, fieldPath);
  const checked = value !== undefined || open;

  const onToggle = (e, { checked: next }) => {
    if (next) {
      // only write initialValue when it actually holds data; with `{}` write
      // nothing — the open flag alone keeps the body visible (guide §7, F2)
      if (hasData(initialValue))
        setFieldValue(fieldPath, cloneDeep(initialValue));
      setOpen(true);
    } else if (hasData(value)) {
      setConfirming(true);
    } else {
      setFieldValue(fieldPath, undefined);
      setOpen(false);
    }
  };

  return (
    <Form.Field id={fieldPath} error={hasError}>
      <Checkbox label={text} checked={checked} onChange={onToggle} />
      {data.helpText && <FieldHelp help={data.helpText} />}
      {objectMessages.length > 0 && (
        <div className="ui red text">{objectMessages.join(" ")}</div>
      )}
      {checked && (
        <Segment basic className="mbdb-indent">
          {children}
        </Segment>
      )}
      <Confirm
        open={confirming}
        header={`Remove ${text}?`}
        content="The entered data will be removed."
        confirmButton="Remove"
        onCancel={() => setConfirming(false)}
        onConfirm={() => {
          setConfirming(false);
          setFieldValue(fieldPath, undefined);
          setOpen(false);
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
