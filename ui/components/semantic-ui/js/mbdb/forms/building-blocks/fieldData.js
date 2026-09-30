import { useFieldData } from "@js/oarepo_ui/forms";

// Resolves label/helpText/required for a fieldPath from the model
// (ui_model), with explicit props winning over the model defaults.
// getFieldData internally calls useMemo, so it MUST be called
// unconditionally at the top of this hook.
export const useModelFieldData = (
  fieldPath,
  { label, helpText, required } = {}
) => {
  const { getFieldData } = useFieldData();
  const modelData = getFieldData({ fieldPath, fieldRepresentation: "text" });
  return {
    label: label !== undefined ? label : modelData.label,
    helpText: helpText !== undefined ? helpText : modelData.helpText,
    required: required !== undefined ? required : modelData.required,
  };
};
