import React from "react";
import PropTypes from "prop-types";
import { FieldDataContext } from "@js/oarepo_ui/forms";
import { VocabularyField } from "@js/oarepo_vocabularies/form/components/VocabularyField";
import { HelpLabel } from "mbdb-semantic-ui-react";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";
import { rememberItem, useVocabularyItem } from "./vocabularyTitles";

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
  const f = useFieldBinding(fieldPath, { label, help, required });
  // Covers <fieldPath> ("Missing data…") and <fieldPath>.id ("Invalid
  // vocabulary item"); RIF's own error lookup misses nested { id } errors.
  const { messages } = f;

  const value = f.value;
  // A stored { id } without a title needs its display title: from the
  // session cache, otherwise fetched once from the vocabulary API. A value
  // the server already enriched with a title needs no lookup. The title is
  // used only when it is a string — a stored title object without an `en`
  // leaf would otherwise become the option's text and crash React.
  const storedTitle = value?.title?.en ?? value?.title;
  const { title: fetchedTitle } = useVocabularyItem(
    vocabularyName,
    typeof storedTitle === "string" ? undefined : value?.id
  );
  const title =
    (typeof storedTitle === "string" ? storedTitle : undefined) ?? fetchedTitle;

  // The id this field itself last wrote. While the stored id equals it,
  // the remount key below must stay constant: a pick remembers the item
  // before the write, so the same render already has the title and no
  // remount is ever needed for the field's own changes.
  const selfWrittenIdRef = React.useRef(undefined);

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
    // The serialized suggestion spreads the whole vocabulary item, so the
    // title and custom_fields are at hand without a second GET.
    rememberItem(vocabularyName, suggestion.id, {
      title: suggestion.title_l10n,
      customFields: suggestion.custom_fields,
    });
    selfWrittenIdRef.current = suggestion.id;
    formikProps.form.setFieldValue(fieldPath, { id: suggestion.id });
  };

  // The nested provider feeds VocabularyField's own getFieldData: the same
  // resolved data minus helpText, so its built-in helptext label never
  // renders and the help shows only through the two help-mode slots.
  const innerFieldData = React.useMemo(
    () => ({
      getFieldData: () => ({
        label: f.label,
        required: f.required,
        helpText: undefined,
      }),
    }),
    [f.label, f.required]
  );

  // VocabularyField renders the label inside its own <label> (and that is
  // also where ChemicalPicker's links sit): the shell gets none, so each
  // label renders exactly once — text and the popup-mode icon alike. The
  // required asterisk still marks it (Semantic's `.field.required label`).
  const labelNode =
    f.label !== undefined && f.label !== null ? (
      <HelpLabel label={f.label} help={f.help} />
    ) : undefined;

  return (
    // messages stay empty: the list-level error shows ONCE, as the
    // dropdown's own error prop label below (never duplicated under the
    // label, so the shell gets no error list)
    <FieldShell
      label={undefined}
      help={f.help}
      required={f.required}
      hasError={messages.length > 0}
      messages={[]}
    >
      <FieldDataContext.Provider value={innerFieldData}>
        <VocabularyField
          // RemoteSelectField reads initialSuggestions only in its
          // constructor, so a title fetched after mount never shows unless
          // the field remounts once it is known. The key is the constant
          // "titled" whenever the title is known (or the id came from this
          // field's own pick — the pick remembers the item first, so the
          // same re-render has it): empty → pick → clear never remount and
          // the dropdown keeps its focus. Only a stored id whose title is
          // still unknown gets an `id:<id>` key — a freshly loaded draft —
          // and remounts exactly once, when either the title arrives or
          // the id is changed from outside the field.
          key={
            value?.id &&
            title === undefined &&
            selfWrittenIdRef.current !== value.id
              ? `id:${value.id}`
              : "titled"
          }
          {...restProps}
          fieldPath={fieldPath}
          vocabularyName={vocabularyName}
          label={labelNode}
          required={f.required}
          // suppresses the help RIF renders inside the vocabulary field —
          // the help is the wrapper's own (the HelpMode label slot). Same
          // reason the alias fields keep internal `helpText`.
          // eslint-disable-next-line no-restricted-syntax
          helpText={undefined}
          clearable={!f.required}
          error={messages.length > 0 ? messages.join(" ") : undefined}
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
    </FieldShell>
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
