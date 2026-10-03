import { getIn, useFormikContext } from "formik";
import { useFieldData, useFormConfig } from "@js/oarepo_ui/forms";
import { useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";

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
// "children" is not misread as a path. Remove once every entity path has a
// ui_model entry (1R C9).
export const readableLabel = (label, fallback) => {
  if (typeof label === "string")
    return label.includes("children.") ? leafLabel(label) : label;
  return label !== undefined ? label : fallback;
};

// English-only localization for the ui_model's i18n dicts ({en: "…"}). It
// mirrors getLocalizedValue from @js/oarepo_ui/util (locale → fallback
// locale → first entry → default), reduced to this project's English-only
// rule. Not imported from oarepo because that module's import graph pulls
// `@translations/oarepo_ui/i18next`, which Jest cannot load.
const localized = (dict, fallback = undefined) => {
  if (!dict) return fallback;
  if (typeof dict === "string") return dict;
  if (typeof dict === "object") {
    if (Array.isArray(dict)) return dict[0] ?? fallback;
    if (typeof dict.en === "string") return dict.en;
    const first = Object.values(dict).find((v) => typeof v === "string");
    return first ?? fallback;
  }
  return fallback;
};

// Resolves a field's ui_model node for `fieldPath` against the CURRENT form
// values. ui_model shapes (implementation guide §6 "Polymorphic fields"):
//
// - object fields nest under `children`, array items under `child`;
// - a polymorphic node holds the complete UNION of every variant's fields in
//   `children`, plus `discriminator` (the field name whose value chooses the
//   variant) and `variants` (per discriminator value, only the DIFFERENT
//   fields, each stored whole);
// - variant entries can themselves be polymorphic (nested variants).
//
// Lookup order: a node's own `label` / `help` / `required` come from the node
// the walk arrived at — a variant entry's own texts describe the variant TYPE
// ("Yes purity", "Empty object", "Polymer"), not the property, so they are
// never applied to the node (implementation guide §6). A CHILD field is taken
// from the deepest matching variant entry, falling back to the union. Scalars
// of sibling nodes are never merged.
export const resolveUiNode = (uiModel, fieldPath, values) => {
  if (!uiModel || !fieldPath) return undefined;
  const segments = fieldPath.split(".");
  // The current node, with the children of every active variant (deepest
  // first) overlaid onto the union's — a variant child wins wholesale.
  const withVariants = (node, recordSoFar) => {
    let layered = node;
    while (layered?.variants && layered?.discriminator) {
      const discr = getIn(
        values,
        recordSoFar
          ? `${recordSoFar}.${layered.discriminator}`
          : layered.discriminator
      );
      const variant = discr !== undefined ? layered.variants[discr] : undefined;
      if (!variant) break;
      // Only the STRUCTURE comes from the variant entry. Its own `label`,
      // `help`, `hint` and `input` are the variant TYPE's texts, not the
      // property's — they must never replace the node's (guide §6). A
      // QualityControls row says "Purity" in every state; a variant only
      // changes what is inside.
      const next = { ...layered };
      next.children = { ...layered.children, ...variant.children };
      if (variant.child !== undefined) next.child = variant.child;
      // a variant entry re-declares `variants`/`discriminator` only when it
      // is itself polymorphic — do not keep the outer ones, or the loop
      // would re-apply the same variant forever (nested variants apply again)
      if (variant.variants) {
        next.variants = variant.variants;
        if (variant.discriminator !== undefined)
          next.discriminator = variant.discriminator;
      } else {
        delete next.variants;
        delete next.discriminator;
      }
      layered = next;
    }
    return layered;
  };

  let node = uiModel;
  let recordSoFar = "";
  for (const segment of segments) {
    const isIndex = /^\d+$/.test(segment);
    node = withVariants(node, recordSoFar);
    const next = isIndex
      ? node.children?.child ?? node.child
      : node.children?.[segment];
    if (next === undefined) return undefined;
    node = next;
    recordSoFar = recordSoFar ? `${recordSoFar}.${segment}` : segment;
  }
  return withVariants(node, recordSoFar);
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
  // when there is no Formik above (stories without a Form), formik's context
  // is `undefined`; discriminator lookups then just see an empty record
  const { values } = useFormikContext() ?? {};
  let uiModel;
  try {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const { config } = useFormConfig();
    uiModel = config?.ui_model;
  } catch {
    uiModel = undefined; // stories/tests without a form config: model-less
  }
  // fieldPath is optional for some blocks (FieldGroup without a model path).
  // oarepo's getFieldData would crash on undefined (toModelPath does
  // path.split), so skip the lookup: explicit props become the only source.
  const node = fieldPath
    ? resolveUiNode(uiModel, fieldPath, values)
    : undefined;
  const modelData = node
    ? {
        label: localized(node.label, null),
        helpText: localized(node.help, null),
        required: node.required,
      }
    : fieldPath
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

// Everything a single-value field needs, from one fieldPath: value, a
// writer, errors and the resolved model data. The one place that maps the
// public `help` prop onto the model's `helpText` key — blocks read
// `const f = useFieldBinding(fieldPath, { label, help, required })` and
// render <FieldShell inputId={fieldPath} label={f.label} help={f.help}
// required={f.required} messages={f.messages}>…</FieldShell>.
// Blocks that need more than model data (merged object-path messages, the
// whole record) still call useModelFieldData / useFormikContext directly.
export const useFieldBinding = (fieldPath, { label, help, required } = {}) => {
  // meant for fields inside a Form — without a Formik provider it throws,
  // as its siblings do (a story always has one, and a missing one is a bug,
  // not a supported shape).
  const { values, setFieldValue, handleBlur } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const { hasError, messages } = useFieldErrors(fieldPath);
  const unset = useUnsetField();
  return {
    value: getIn(values, fieldPath),
    // "" / null / undefined remove the key (guide §7); anything else is
    // written as is — 0 and false are data
    setValue: (next) =>
      next === "" || next === null || next === undefined
        ? unset(fieldPath)
        : setFieldValue(fieldPath, next),
    onBlur: handleBlur,
    label: data.label,
    help: data.helpText,
    required: data.required,
    hasError,
    messages,
  };
};
