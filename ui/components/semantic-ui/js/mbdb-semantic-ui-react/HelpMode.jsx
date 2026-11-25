import React from "react";
import PropTypes from "prop-types";
import { Icon, Popup } from "semantic-ui-react";

// Global switch between Invenio-style help under the field ("invenio") and
// a "?" popup next to the label ("popup"). A React context — not a module
// constant or a per-field prop — so one switch changes every field at run
// time (and reaches into Semantic Modals/Popups, which are portals).
export const HELP_MODES = ["invenio", "popup"];
export const DEFAULT_HELP_MODE = "invenio";

const HelpModeContext = React.createContext(DEFAULT_HELP_MODE);

export const HelpModeProvider = ({ mode, children }) => (
  // An unknown mode (e.g. a bad config value) falls back to the default
  // instead of throwing — a misconfiguration must not blank the page.
  <HelpModeContext.Provider
    value={HELP_MODES.includes(mode) ? mode : DEFAULT_HELP_MODE}
  >
    {children}
  </HelpModeContext.Provider>
);

HelpModeProvider.propTypes = {
  mode: PropTypes.oneOf(HELP_MODES),
  children: PropTypes.node,
};

// DEFAULT_HELP_MODE when there is no provider (tests, stories that forget
// it): React.useContext returns the value the context was created with.
export const useHelpMode = () => React.useContext(HelpModeContext);

export const HelpIcon = ({ help, label }) => {
  if (!help) return null;
  return (
    <Popup
      content={help}
      on={["hover", "focus"]}
      position="top center"
      size="small"
      wide
      trigger={
        <Icon
          name="question circle outline"
          link
          tabIndex={0}
          role="button"
          aria-label={typeof label === "string" ? `Help: ${label}` : "Help"}
          // the icon usually sits inside <label htmlFor=…>, and a click on
          // a label moves focus to the input, closing the popup at once
          onClick={(e) => e.preventDefault()}
        />
      }
    />
  );
};

HelpIcon.propTypes = {
  help: PropTypes.node,
  label: PropTypes.node,
};

// The label slot: renders the label; in popup mode (and only then, and only
// when there is help) appends the "?" icon. Never render a HelpIcon inside
// a <button> — labels only.
export const HelpLabel = ({ label, help }) => {
  const mode = useHelpMode();
  if (mode === "popup" && help) {
    return (
      <span>
        {label} <HelpIcon help={help} label={label} />
      </span>
    );
  }
  // A bare node (not a one-child fragment — react/jsx-no-useless-fragment),
  // but a component may not return undefined, so map it to null.
  return label === undefined ? null : label;
};

HelpLabel.propTypes = {
  label: PropTypes.node,
  help: PropTypes.node,
};
