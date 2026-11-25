import React from "react";
import PropTypes from "prop-types";

// One-shot default for the INITIAL open state of the collapsible parts the
// playground's "Expand all" / "Collapse all" buttons drive (a TableArrayField
// row's expanded part, a SummaryItem's / DetailView mini row's read-only
// details). The deposit form has no provider, so the value is `undefined`
// there and every block keeps its own default; the playground sets "open" or
// "closed" and remounts the story, so the blocks read it once, as their
// initial state (a later user toggle still wins).
export const DISCLOSURE_DEFAULTS = ["open", "closed"];

const DisclosureDefaultContext = React.createContext(undefined);

export const DisclosureDefaultProvider = ({ value, children }) => (
  // An unknown value falls back to `undefined` (no forcing), like HelpMode's
  // bad-value fallback: a misconfiguration must not blank or force the page.
  <DisclosureDefaultContext.Provider
    value={DISCLOSURE_DEFAULTS.includes(value) ? value : undefined}
  >
    {children}
  </DisclosureDefaultContext.Provider>
);

DisclosureDefaultProvider.propTypes = {
  value: PropTypes.oneOf(DISCLOSURE_DEFAULTS),
  children: PropTypes.node,
};

// `undefined` when there is no provider (the deposit form, and tests that do
// not wrap): React.useContext returns the value the context was created with,
// so every block's own default is used.
export const useDisclosureDefault = () =>
  React.useContext(DisclosureDefaultContext);
