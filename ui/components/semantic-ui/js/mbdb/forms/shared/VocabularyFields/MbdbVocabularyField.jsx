import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { FieldDataContext } from "@js/oarepo_ui/forms";
import { VocabularyField } from "@js/oarepo_vocabularies/form/components/VocabularyField";
import { FieldHelp, HelpLabel } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";
import { rememberTitle, useVocabularyTitle } from "./vocabularyTitles";

// The one way mbdb forms reference a vocabulary term. oarepo's
// VocabularyField is wrapped because its defaults break four form rules:
// it writes "" on clear, it renders its own helptext (bypassing the help
// mode), it takes the initial option from values.ui (which has no titles
// here), and the option description is an info popup instead of the facts
// that tell terms apart. The fixes go through props: VocabularyField
// spreads restProps last onto RemoteSelectField, so these win.

// RemoteSelectField turns a typed addition into an option by
// serializeAddedValue. Ours marks the option so onValueChange can tell a
// user-typed addition apart from a real suggestion; the marked keys ride
// along harmlessly in the dropdown state. VocabularyField passes its own
// serializeAddedValue before restProps, so this one wins.
const serializeAddedValue = (value) => ({
  text: value,
  value,
  key: value,
  name: value,
  id: value,
  mbdbAddition: true,
});

export const MbdbVocabularyField = ({
  fieldPath,
  vocabularyName,
  describe,
  label,
  help,
  required,
  onAddition,
  ...restProps
}) => {
  const { values } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // Covers <fieldPath> ("Missing data…") and <fieldPath>.id ("Invalid
  // vocabulary item"); RIF's own error lookup misses nested { id } errors.
  const { messages } = useFieldErrors(fieldPath);

  const value = getIn(values, fieldPath);
  // A stored { id } without a title needs its display title: from the
  // session cache, otherwise fetched once from the vocabulary API. A value
  // the server already enriched with a title needs no lookup.
  const storedTitle = value?.title?.en ?? value?.title;
  const fetchedTitle = useVocabularyTitle(
    vocabularyName,
    storedTitle ? undefined : value?.id
  );
  const title = storedTitle ?? fetchedTitle;

  const onValueChange = ({ data: changeData, formikProps }, suggestions) => {
    const suggestion = suggestions.find((o) => o.id === changeData.value);
    if (!suggestion) {
      // Clear (or anything else that matches no option): remove the key.
      unsetFieldValue(
        formikProps.form.values,
        formikProps.form.setFieldValue,
        fieldPath
      );
      return;
    }
    if (suggestion.mbdbAddition) {
      // The "Enter manually" option: the caller decides what to store.
      // Writing { id: typedText } here would send a fake reference.
      onAddition?.(changeData.value);
      return;
    }
    rememberTitle(vocabularyName, suggestion.id, suggestion.title_l10n);
    formikProps.form.setFieldValue(fieldPath, { id: suggestion.id });
  };

  // The nested provider feeds VocabularyField's own getFieldData: the same
  // resolved data minus helpText, so its built-in helptext label never
  // renders and the help shows only through the two help-mode slots.
  const innerFieldData = React.useMemo(
    () => ({
      getFieldData: () => ({
        label: data.label,
        required: data.required,
        helpText: undefined,
      }),
    }),
    [data.label, data.required]
  );

  return (
    <>
      <FieldDataContext.Provider value={innerFieldData}>
        <VocabularyField
          {...restProps}
          fieldPath={fieldPath}
          vocabularyName={vocabularyName}
          label={<HelpLabel label={data.label} help={data.helpText} />}
          required={data.required}
          helpText={undefined}
          clearable={!data.required}
          error={messages.length > 0 ? messages[0] : undefined}
          initialSuggestions={
            value?.id ? [{ id: value.id, title_l10n: title }] : []
          }
          serializeAddedValue={serializeAddedValue}
          onValueChange={onValueChange}
          filterFunction={(options) =>
            options.map((option) => ({
              ...option,
              description: describe?.(option),
            }))
          }
        />
      </FieldDataContext.Provider>
      <FieldHelp help={data.helpText} />
    </>
  );
};

MbdbVocabularyField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  vocabularyName: PropTypes.string.isRequired,
  // option (serialized suggestion) → short description shown in the dropdown
  describe: PropTypes.func,
  // called with the typed text when the user picks an allowed addition,
  // INSTEAD of the wrapper writing anything (manual-entry switch)
  onAddition: PropTypes.func,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
};
