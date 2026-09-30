import React from "react";
import PropTypes from "prop-types";
import { Icon, Popup } from "semantic-ui-react";

// One-line switch between Invenio-style help under the field and a popup
// icon next to the label. A module constant, not a per-field prop.
export const FIELD_HELP_MODE = "invenio"; // or "popup"

export const FieldHelp = ({ help, mode = FIELD_HELP_MODE }) => {
  if (!help) return null;
  if (mode === "popup") {
    return (
      <Popup
        content={help}
        on={["hover", "focus"]}
        trigger={
          <Icon
            name="question circle outline"
            tabIndex={0}
            link
            role="button"
            aria-label="Help"
          />
        }
      />
    );
  }
  return <label className="helptext mbdb-field-help">{help}</label>;
};

FieldHelp.propTypes = {
  help: PropTypes.node,
  mode: PropTypes.oneOf(["invenio", "popup"]),
};
