import React from "react";
import { Grid } from "semantic-ui-react";
import { TextField, FieldLabel } from "react-invenio-forms";
import {
  PropFieldsComponent,
  VocabularyMultilingualInputField,
} from "@js/oarepo_vocabularies";
import { useFormConfig } from "@js/oarepo_ui";
import { i18next } from "@translations/oarepo_vocabularies_ui/i18next";
import _has from "lodash/has";

const VocabularyFormFields = () => {
  const {
    formConfig: { vocabularyProps },
  } = useFormConfig();
  const hasPropFields = _has(vocabularyProps, "props");
  return (
    <Grid.Column id="main-content" mobile={16} tablet={16} computer={11}>
      <VocabularyMultilingualInputField
        fieldPath="title"
        textFieldLabel={i18next.t("Title")}
        displayFirstInputRemoveButton={false}
      />
      <TextField
        fieldPath="id"
        label={
          <FieldLabel htmlFor="id" label={i18next.t("ID")} />
        }
        required
      />
      {hasPropFields && (
        <PropFieldsComponent vocabularyProps={vocabularyProps} />
      )}
    </Grid.Column>
  );
};

export default VocabularyFormFields;