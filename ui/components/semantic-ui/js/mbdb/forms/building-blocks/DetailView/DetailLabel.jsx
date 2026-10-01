import PropTypes from "prop-types";
import { useFieldData } from "@js/oarepo_ui/forms";
import { readableLabel } from "@js/mbdb/forms/building-blocks/fieldData";

// getFieldData uses hooks, so one tiny component per label (rows are few).
// getFieldData also returns the raw model path as the "label" in production
// when the ui_model has no entry for the path; readableLabel maps that to the
// readable leaf instead.
export const DetailLabel = ({ path, fallback }) => {
  const { getFieldData } = useFieldData();
  const { label } = getFieldData({
    fieldPath: path,
    fieldRepresentation: "text",
  });
  return readableLabel(label, fallback);
};
DetailLabel.propTypes = {
  path: PropTypes.string.isRequired,
  fallback: PropTypes.string.isRequired,
};
