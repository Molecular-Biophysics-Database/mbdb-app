import PropTypes from "prop-types";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// The label of one field, resolved the same way the form blocks resolve theirs
// (variant-aware, R0), so a nested label is never another variant's. One tiny
// component per label, because the lookup uses hooks (rows are few).
export const DetailLabel = ({ path, fallback }) => {
  const { label } = useModelFieldData(path);
  return label ?? fallback;
};
DetailLabel.propTypes = {
  path: PropTypes.string.isRequired,
  fallback: PropTypes.string.isRequired,
};
