import React from "react";
import _isEmpty from "lodash/isEmpty";
import { BaseForm, TextField, FieldLabel } from "react-invenio-forms";
import { Container, Header, Message } from "semantic-ui-react";
import { DepositValidationSchema } from "./DepositValidationSchema";
import { useFormConfig, useOnSubmit, submitContextType } from "@js/oarepo_ui";
import { FormikStateLogger } from "@js/oarepo_vocabularies";

export const DepositForm = () => {
  const { record, formConfig } = useFormConfig();
  const values = {
    ...record,
    ...{ id: "" },
  };

  const context = formConfig.createUrl
    ? submitContextType.create
    : submitContextType.update;

  const { onSubmit } = useOnSubmit({
    apiUrl: formConfig.createUrl || formConfig.updateUrl,
    context: context,
    onSubmitSuccess: (result) => {
      window.location.href = editMode
        ? currentPath.replace("/edit", "")
        : currentPath.replace("_new", result.id);
    },
    onSubmitError: (error) => {
      console.error("Sumbission failed", error);
    },
  });

  return (
    <Container>
      <BaseForm
        onSubmit={onSubmit}
        formik={{
          initialValues: values,
          validationSchema: DepositValidationSchema,
          validateOnChange: false,
          validateOnBlur: true,
          enableReinitialize: true,
        }}
      >
        <Header textAlign="center">mbdb-mst-ui deposit form</Header>
        <TextField
          fieldPath="id"
          label={<FieldLabel htmlFor="id" icon="book" label="Record ID" />}
          placeholder="Enter a record ID"
          required
          className="id-field"
        />
        <pre>Add more of your deposit form fields here 👇</pre>
        {/* TODO: remove once you don't need to know Formik's internal state anymore */}
        <FormikStateLogger />
      </BaseForm>
    </Container>
  );
};
