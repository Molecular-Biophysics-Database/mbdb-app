import { useFieldData } from "@js/oarepo_ui/forms";

// Untouched by callers: turns a ui_model path leaf ("some_field") into a
// readable label ("Some field").
const leafLabel = (path) => {
  const leaf = path.split(".").pop();
  const words = leaf.replace(/_/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
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
  // Temporary (until polymorphic ui_model is fixed on the backend): when
  // the ui_model has no entry for the path, oarepo's getFieldData returns
  // the toModelPath string as the label ("children.metadata.children.…name").
  // Showing that raw path is worse than a readable leaf, so detect the
  // fallback (toModelPath always inserts ".children." segments) and use the
  // leaf instead. helpText stays null in that case.
  const modelLabel =
    typeof modelData.label === "string" && modelData.label.includes("children.")
      ? leafLabel(modelData.label)
      : modelData.label;
  return {
    label: label !== undefined ? label : modelLabel,
    helpText: helpText !== undefined ? helpText : modelData.helpText,
    required: required !== undefined ? required : modelData.required,
  };
};
