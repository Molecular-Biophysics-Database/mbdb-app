import React from "react";
import PropTypes from "prop-types";
import { Form, FieldHelp, HelpLabel } from "mbdb-semantic-ui-react";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";

// The label slot of a field: a real <label htmlFor> holding the HelpLabel
// (model label + optional "?" icon in popup mode). Without an `inputId`
// the caller's control labels itself (oarepo's fields wrap the label node
// in their own <label>), so the HelpLabel renders bare.
export const FieldLabel = ({ inputId, label, help }) =>
  inputId ? (
    <label htmlFor={inputId}>
      <HelpLabel label={label} help={help} />
    </label>
  ) : (
    <HelpLabel label={label} help={help} />
  );
FieldLabel.propTypes = {
  inputId: PropTypes.string,
  label: PropTypes.node,
  help: PropTypes.node,
};

// The outer structure of every single-value field: one root Form.Field
// holding label, control, errors and help — in this order, defined here
// and nowhere else. One root element, so the shell works as one column in
// a Form.Group (guide §8). Both help modes are honored by the two slots:
// HelpLabel (the "?" icon in popup mode) and FieldHelp (the helptext label
// under the control in invenio mode).
export const FieldShell = ({
  inputId,
  label,
  help,
  required,
  messages = [],
  width,
  className,
  children,
}) => (
  <Form.Field
    required={required}
    error={messages.length > 0}
    width={width}
    className={className}
  >
    {
      // a falsy label (", undefined, an empty override) renders no label
      // slot at all — never an empty <label> element
      label ? <FieldLabel inputId={inputId} label={label} help={help} /> : null
    }
    {children}
    <ErrorMessages messages={messages} />
    <FieldHelp help={help} />
  </Form.Field>
);

FieldShell.propTypes = {
  // id of the control, for <label htmlFor>; omit when the control labels
  // itself (oarepo's fields) — the label then renders without a wrapper
  inputId: PropTypes.string,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
  messages: PropTypes.arrayOf(PropTypes.string),
  width: PropTypes.number,
  // lands on the Form.Field (e.g. "mbdb-monospace": the LESS rule
  // .mbdb-monospace textarea then matches the control below)
  className: PropTypes.string,
  children: PropTypes.node.isRequired,
};
