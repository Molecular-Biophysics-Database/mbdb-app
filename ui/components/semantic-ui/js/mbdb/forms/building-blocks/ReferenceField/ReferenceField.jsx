import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Dropdown } from "mbdb-semantic-ui-react";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";

const defaultDescribe = (item) => item.name;

// Items of `targetPath` as dropdown options, plus the stored references that no
// longer exist there, so a deleted target is visible instead of silently lost.
export const referenceOptions = (targets, stored, describe) => {
  const options = (targets ?? [])
    .filter((item) => item?.id)
    .map((item) => ({
      key: item.id,
      value: item.id,
      text: describe(item) || "(unnamed)",
    }));
  const known = new Set(options.map((option) => option.value));
  stored
    .filter((ref) => ref?.id && !known.has(ref.id))
    .forEach((ref) =>
      options.push({
        key: ref.id,
        value: ref.id,
        text: `${ref.name ?? ref.id} (no longer exists)`,
      })
    );
  return options;
};

// A model `internal-relation`: picks one item (or, with `multiple`, several) of
// a list in the same record. Writes `{ id, name }`; the server takes the id and
// copies the name again on save.
export const ReferenceField = ({
  fieldPath,
  targetPath,
  describe = defaultDescribe,
  multiple = false,
  label,
  help,
  required,
  placeholder,
  ...uiProps
}) => {
  const { values } = useFormikContext();
  const f = useFieldBinding(fieldPath, { label, help, required });
  const targets = getIn(values, targetPath) ?? [];
  const stored = multiple ? f.value ?? [] : [f.value].filter(Boolean);

  const toReference = (id) => {
    const target = targets.find((item) => item?.id === id);
    return target
      ? { id, name: target.name }
      : stored.find((ref) => ref?.id === id);
  };

  const onChange = (e, { value: next }) => {
    if (multiple)
      f.setValue(next.length > 0 ? next.map(toReference) : undefined);
    else f.setValue(next === "" ? undefined : toReference(next));
  };

  return (
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={f.hasError}
      messages={f.messages}
    >
      <Dropdown
        {...uiProps}
        id={fieldPath}
        fluid
        search
        selection
        multiple={multiple}
        clearable={!f.required}
        selectOnBlur={false}
        error={f.hasError || undefined}
        options={referenceOptions(targets, stored, describe)}
        value={
          multiple ? stored.map((ref) => ref?.id).filter(Boolean) : f.value?.id ?? ""
        }
        placeholder={placeholder}
        onBlur={f.onBlur}
        onChange={onChange}
      />
    </FieldShell>
  );
};

ReferenceField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  // absolute path of the list the reference points into
  targetPath: PropTypes.string.isRequired,
  // target item → option text (default: its name)
  describe: PropTypes.func,
  multiple: PropTypes.bool,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
  placeholder: PropTypes.string,
};
