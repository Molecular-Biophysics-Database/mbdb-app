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
    // label without htmlFor or a nested control: the label is for a composite
    // control (button groups, dropdowns), same as every other block in this
    // codebase — Semantic's `.field.required label` styles it and OARepo's
    // scroll-to-error resolves it by field path.
    // eslint-disable-next-line jsx-a11y/label-has-associated-control
    <label>
      <HelpLabel label={label} help={help} />
    </label>
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
//
// helpPlacement="control" (default) keeps help under the control — right for
// a single input/select/value+unit. helpPlacement="label" moves it directly
// under the label, for composite controls (button groups, tables) whose help
// would otherwise sit far below, after an Add button (guide §8, help
// placement). Errors always stay after the control.
export const FieldShell = ({
  inputId,
  label,
  help,
  required,
  hasError,
  markError = true,
  messages = [],
  width,
  className,
  helpPlacement = "control",
  children,
}) => (
  <Form.Field
    required={required}
    error={markError ? hasError ?? messages.length > 0 : false}
    width={width}
    className={className}
  >
    {
      // a falsy label (", undefined, an empty override) renders no label
      // slot at all — never an empty <label> element
      label ? <FieldLabel inputId={inputId} label={label} help={help} /> : null
    }
    {helpPlacement === "label" && <FieldHelp help={help} placement="label" />}
    {children}
    <ErrorMessages messages={messages} />
    {helpPlacement === "control" && <FieldHelp help={help} />}
  </Form.Field>
);

FieldShell.propTypes = {
  // id of the control, for <label htmlFor>; omit to render <label> without
  // one (the control still gets styled as an input label)
  inputId: PropTypes.string,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
  // explicit error state; defaults to messages.length > 0 so callers that
  // already merge their own error state (the binding's `hasError`, the
  // boolean `error` prop of the wrapper) tint the whole field as well
  hasError: PropTypes.bool,
  // false for lists whose nested items must not turn red as a whole (the
  // list-level message still shows) — e.g. StringArrayField
  markError: PropTypes.bool,
  messages: PropTypes.arrayOf(PropTypes.string),
  width: PropTypes.number,
  // lands on the Form.Field (e.g. "mbdb-monospace": the LESS rule
  // .mbdb-monospace textarea then matches the control below)
  className: PropTypes.string,
  // "control" (default): help under the control. "label": help directly
  // under the label — composite controls (guide §8)
  helpPlacement: PropTypes.oneOf(["control", "label"]),
  children: PropTypes.node.isRequired,
};
