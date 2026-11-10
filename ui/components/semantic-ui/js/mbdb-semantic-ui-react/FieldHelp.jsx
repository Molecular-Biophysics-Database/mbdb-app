import React from "react";
import PropTypes from "prop-types";
import { useHelpMode } from "./HelpMode";

// The help slot of a field. "invenio" mode: helptext label (keep the
// mbdb-field-help class — LESS hooks on it). "popup" mode: nothing — the
// icon lives in the label slot (HelpLabel). Empty help → null either way.
//
// placement="control" (default): under the control, Invenio's convention.
// placement="label": directly under the label (the extra class lets LESS
// cancel Invenio's negative margin-top). Composite controls — button groups,
// lists with their own Add button, tables — use it so their help does not sit
// far away, under the Add button (implementation guide §8, help placement).
export const FieldHelp = ({ help, placement = "control" }) => {
  const mode = useHelpMode();
  if (!help || mode === "popup") return null;
  const className =
    placement === "label"
      ? "helptext mbdb-field-help mbdb-field-help-under-label"
      : "helptext mbdb-field-help";
  return <label className={className}>{help}</label>;
};

FieldHelp.propTypes = {
  help: PropTypes.node,
  placement: PropTypes.oneOf(["control", "label"]),
};
