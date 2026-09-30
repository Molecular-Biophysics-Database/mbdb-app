import React from "react";
import PropTypes from "prop-types";
import { useHelpMode } from "./HelpMode";

// The help slot under a control. "invenio" mode: helptext label (keep the
// mbdb-field-help class — LESS hooks on it). "popup" mode: nothing — the
// icon lives in the label slot (HelpLabel). Empty help → null either way.
export const FieldHelp = ({ help }) => {
  const mode = useHelpMode();
  if (!help || mode === "popup") return null;
  return <label className="helptext mbdb-field-help">{help}</label>;
};

FieldHelp.propTypes = {
  help: PropTypes.node,
};
