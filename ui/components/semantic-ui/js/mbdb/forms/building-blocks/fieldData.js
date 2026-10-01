import { useFieldData } from "@js/oarepo_ui/forms";

// Untouched by callers: turns a ui_model path leaf ("some_field") into a
// readable label ("Some field").
const leafLabel = (path) => {
  const leaf = path.split(".").pop();
  const words = leaf.replace(/_/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
};

// Label fallback for paths with no ui_model entry. oarepo's getFieldData then
// returns the raw toModelPath string as the label — toModelPath always
// inserts ".children." segments, so a string label containing "children." is
// that raw path, not a real label. In that case show the readable leaf.
// `fallback` is the last resort when `label` is undefined. Used by
// useModelFieldData and the DetailView label/heading components; the needle
// is "children." WITH the dot so a genuine label containing the word
// "children" is not misread as a path. Remove once the backend's polymorphic
// ui_model issue is fixed.
export const readableLabel = (label, fallback) => {
  if (typeof label === "string")
    return label.includes("children.") ? leafLabel(label) : label;
  return label !== undefined ? label : fallback;
};

// Resolves label/helpText/required for a fieldPath from the model
// (ui_model), with explicit props winning over the model defaults.
// getFieldData internally calls useMemo, so it MUST be called
// unconditionally at the top of this hook.
export const useModelFieldData = (
  fieldPath,
  { label, helpText, required } = {}
) => {
  const { getFieldData } = useFieldData();
  // fieldPath is optional for some blocks (FieldGroup without a model path).
  // oarepo's getFieldData would crash on undefined (toModelPath does
  // path.split), so skip the lookup: explicit props become the only source.
  const modelData = fieldPath
    ? getFieldData({ fieldPath, fieldRepresentation: "text" })
    : { label: undefined, helpText: undefined, required: undefined };
  // readableLabel replaces a raw-path label with its readable leaf; helpText
  // stays null in that fallback case.
  const modelLabel = readableLabel(modelData.label, undefined);
  return {
    label: label !== undefined ? label : modelLabel,
    helpText: helpText !== undefined ? helpText : modelData.helpText,
    required: required !== undefined ? required : modelData.required,
  };
};
