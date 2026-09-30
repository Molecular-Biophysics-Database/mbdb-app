import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { Form, Header, FieldHelp } from "mbdb-semantic-ui-react";

// A titled group of related fields. Does not bind to Formik; only reads
// `errors` under `fieldPath` to turn the header red and gives the header
// an `id` so OARepo error scrolling can find it.
export const FieldGroup = ({
  title,
  help,
  required,
  fieldPath,
  inline,
  children,
}) => {
  const { errors } = useFormikContext();
  const hasError = fieldPath ? !!getIn(errors, fieldPath) : false;

  return (
    <>
      <Header as="h5" id={fieldPath} color={hasError ? "red" : undefined}>
        {title}
        {required && " *"}
      </Header>
      <FieldHelp help={help} />
      {inline ? <Form.Group widths="equal">{children}</Form.Group> : children}
    </>
  );
};

FieldGroup.propTypes = {
  title: PropTypes.node.isRequired,
  help: PropTypes.node,
  required: PropTypes.bool,
  fieldPath: PropTypes.string,
  inline: PropTypes.bool,
  children: PropTypes.node,
};
