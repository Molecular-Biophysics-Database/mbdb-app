import React from "react";
import { TextField, FieldLabel } from "react-invenio-forms";
import {
  PropFieldsComponent,
} from "@js/oarepo_vocabularies";
import { useFormConfig } from "@js/oarepo_ui";
import { i18next } from "@translations/oarepo_vocabularies_ui/i18next";
import _has from "lodash/has";
import TitleField from "./TitleField";
import { useFormikContext } from "formik";
import { v4 as uuidv4 } from 'uuid';
import { useEffect } from "react";

const VocabularyFormFields = () => {
  const {
    formConfig: { vocabularyProps },
  } = useFormConfig();
  const hasPropFields = _has(vocabularyProps, "props");
  const { values } = useFormikContext();
  const type = values.type;
  console.log(type, 'Type')
  useEffect(() => {
    if (type === "grants") {
      values.id = `oa:${uuidv4()}`
    }
  }, [type, values]);
  return (
    <div>
      <div className="mb-4">
        <TitleField
          name='title'
          label='Title'
          fieldName='en'
          required
        />
      </div>
      {type === "chemicals" &&
      <>
        <TitleField
          name='id'
          label='ID'
          fieldName='inchikey'
        />
        <TextField
          fieldPath="id"
          label={
            <FieldLabel htmlFor="id" label={i18next.t("ID")} />
          }
          required
        />
      </>
      }
      {hasPropFields && (
        <PropFieldsComponent vocabularyProps={vocabularyProps} />
      )}
    </div>
  );
};

export default VocabularyFormFields;