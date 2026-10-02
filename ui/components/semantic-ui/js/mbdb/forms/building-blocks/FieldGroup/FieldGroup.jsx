import React from "react";
import PropTypes from "prop-types";
import {
  Form,
  Header,
  Segment,
  Divider,
  FieldHelp,
  HelpLabel,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";

// A titled group of related fields. Does not bind to Formik; only reads
// errors under `fieldPath` to turn the header red and gives the header an
// `id` so OARepo error scrolling can find it. When `fieldPath` is set,
// title/help/required come from the model (explicit props win).
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
  // fieldPath is optional; the shared error hook must run unconditionally,
  // so point it at a path that never matches anything when there is none.
  const { hasError } = useFieldErrors(fieldPath ?? "__fieldgroup_no_path__");
  // Object-level message for the group's own path ("Missing data for
  // required field." on a required group, etc.), shown under the header.
  const ownMessages = useOwnErrorMessages(
    fieldPath ?? "__fieldgroup_no_path__"
  );

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
      <ErrorMessages messages={ownMessages} />
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
