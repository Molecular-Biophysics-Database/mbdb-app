import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import {
  Checkbox,
  Confirm,
  FieldHelp,
  Form,
  HelpLabel,
  Segment,
} from "mbdb-semantic-ui-react";
import {
  hasData,
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";

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
  const unset = useUnsetField();
  const [confirming, setConfirming] = useState(false);
  // An explicit local "open" so checking does not have to write `{}` into
  // Formik (guide §7). checked = a value exists OR the user just opened it.
  const [open, setOpen] = useState(false);
  const data = useModelFieldData(fieldPath, { label, helpText: help });
  const text = data.label;
  // Red header reads errors ∪ initialErrors so it survives edits
  const { hasError } = useFieldErrors(fieldPath);
  // object-level messages only (a string sitting exactly at fieldPath)
  const objectMessages = useOwnErrorMessages(fieldPath);

  const value = getIn(values, fieldPath);
  const checked = value !== undefined || open;

  const onToggle = (e, { checked: next }) => {
    if (next) {
      // only write initialValue when it actually holds data; with `{}` write
      // nothing — the open flag alone keeps the body visible (guide §7)
      if (hasData(initialValue))
        setFieldValue(fieldPath, cloneDeep(initialValue));
      setOpen(true);
    } else if (hasData(value)) {
      setConfirming(true);
    } else {
      unset(fieldPath);
      setOpen(false);
    }
  };

  return (
    <>
      {/* No `error` on this Form.Field: Semantic's error rules are descendant
          selectors, so one error under a child field would colour every input
          and label of the group (guide §8). The header label carries the
          state instead; the children live in a sibling, outside the field. */}
      <Form.Field id={fieldPath}>
        <Checkbox
          // semantic-ui-react drops its own <label> element when `label` is a
          // React node (createHTMLLabel returns the children raw), which hides
          // the checkbox square (it is drawn from `label:before`). Wrap the
          // HelpLabel in an explicit <label> so the box keeps rendering.
          label={
            // htmlFor points at the field path (also the Form.Field id) so
            // OARepo error scrolling finds it; the checkbox input inside is
            // the labelled control, as with the other blocks' dropdowns.
            <label
              htmlFor={fieldPath}
              className={hasError ? "mbdb-error-text" : undefined}
            >
              <HelpLabel label={text} help={data.helpText} />
            </label>
          }
          checked={checked}
          onChange={onToggle}
        />
        {data.helpText && <FieldHelp help={data.helpText} />}
        <ErrorMessages messages={objectMessages} />
      </Form.Field>
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
          unset(fieldPath);
          setOpen(false);
        }}
      />
    </>
  );
};

ToggleFieldGroup.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  initialValue: PropTypes.object,
  children: PropTypes.node.isRequired,
};
