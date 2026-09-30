import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  Form,
  Header,
  Segment,
  Divider,
  FieldHelp,
  HelpLabel,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// A titled group of related fields. Does not bind to Formik; only reads
// errors under `fieldPath` to turn the header red and gives the header an
// `id` so OARepo error scrolling can find it. When `fieldPath` is set,
// title/help/required come from the model (explicit props win).
//
// Error state: server errors live in `initialErrors` and Formik clears
// `errors` on the first edit anywhere, so fall back to the initial error
// while the value at the path is untouched. (Local copy of the C1
// fallback; point at errors.js/useFieldErrors once that helper exists.)
const useGroupError = (fieldPath) => {
  const { errors, initialErrors, values, initialValues } = useFormikContext();
  if (!fieldPath) return false;
  // hasError-equivalent: any message leaf under path counts, including
  // OARepo { message, severity } objects and ""
  const anyMessage = (node) => {
    if (node === undefined || node === null || node === "") return false;
    if (typeof node === "string") return true;
    if (Array.isArray(node)) return node.some(anyMessage);
    if (typeof node === "object") {
      if (typeof node.message === "string") return true;
      return Object.values(node).some(anyMessage);
    }
    return false;
  };
  if (anyMessage(getIn(errors, fieldPath))) return true;
  if (getIn(values, fieldPath) === getIn(initialValues, fieldPath))
    return anyMessage(getIn(initialErrors, fieldPath));
  return false;
};

export const FieldGroup = ({
  title,
  help,
  required,
  fieldPath,
  inline,
  nested,
  divided,
  children,
}) => {
  // Resolved from the model via fieldPath; explicit props win. Fields
  // without a model entry fall back to their props (title is then the
  // label). Note: under polymorphic types (Entity) ui_model has no
  // children yet, so callers pass overrides there until the backend is
  // fixed.
  const data = useModelFieldData(fieldPath, {
    label: title,
    helpText: help,
    required,
  });
  const hasError = useGroupError(fieldPath);

  const content = inline ? (
    <Form.Group widths="equal">{children}</Form.Group>
  ) : (
    children
  );

  return (
    <>
      {divided && <Divider />}
      <Header as="h5" id={fieldPath} color={hasError ? "red" : undefined}>
        <HelpLabel label={data.label} help={data.helpText} />
        {data.required && <span className="mbdb-required">*</span>}
      </Header>
      <FieldHelp help={data.helpText} />
      {nested ? (
        <Segment basic className="mbdb-nested">
          {content}
        </Segment>
      ) : (
        content
      )}
    </>
  );
};

FieldGroup.propTypes = {
  // Optional: resolved from the model when fieldPath is set.
  title: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
  fieldPath: PropTypes.string,
  inline: PropTypes.bool,
  nested: PropTypes.bool,
  divided: PropTypes.bool,
  children: PropTypes.node,
};
