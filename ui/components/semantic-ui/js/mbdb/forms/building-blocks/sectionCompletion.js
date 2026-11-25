import { getIn } from "formik";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
import { resolveUiNode } from "@js/mbdb/forms/building-blocks/fieldData";

// A tab's completion for oarepo's SectionCompletionBar: the filled fraction of
// the fields the model requires below `includesPaths`. Optional fields do not
// count, but the required fields inside a filled optional object do. A section
// without required fields is complete.
//
// The ui_model of a polymorphic node holds the fields of ALL its variants, so
// it cannot tell whether a missing field belongs to the stored one.
// `belongs(value, name)` answers that; when it does not know (undefined), a
// missing field of a polymorphic node is skipped.
export const requiredCompletion = ({
  formikValues,
  reduxState,
  includesPaths,
  belongs = () => undefined,
}) => {
  const uiModel = reduxState.deposit.config?.ui_model;
  let required = 0;
  let filled = 0;

  const walk = (path) => {
    // resolved from the root, so polymorphic nodes follow the stored values
    const node = resolveUiNode(uiModel, path, formikValues);
    if (!node) return;
    const value = getIn(formikValues, path);
    if (isEmptyValue(value)) {
      if (node.required) required += 1;
      return;
    }
    if (Array.isArray(value) && typeof value[0] === "object") {
      value.forEach((_, index) => walk(`${path}.${index}`));
    } else if (node.children && node.input !== "vocabulary") {
      Object.keys(node.children).forEach((name) => {
        const counts =
          !isEmptyValue(value[name]) ||
          node.input !== "polymorphic" ||
          belongs(value, name);
        if (counts) walk(`${path}.${name}`);
      });
    }
    if (node.required) {
      required += 1;
      filled += 1;
    }
  };

  includesPaths.forEach(walk);
  return required === 0 ? 1 : filled / required;
};
