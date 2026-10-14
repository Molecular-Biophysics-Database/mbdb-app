import React from "react";
import PropTypes from "prop-types";
import { DisclosureDefaultProvider } from "./DisclosureDefault";

// Review mode (plan 4R Y18, design ReviewMode.md): a read-only mode for a
// reviewer. One context carries the boolean every block reads plus the setter
// the toggle button uses. The provider usually sits ABOVE Formik (the deposit
// form's Root, the playground app); the consumers that must re-read the mode
// (the section's content, the playground frame) key that content by it, so
// Formik keeps the values. When on, the provider also sets the "open" disclosure
// default, so every collapsible part starts open (Y15's initial-state rule).
const ReviewModeContext = React.createContext({
  review: false,
  setReview: () => {},
});

export const ReviewModeProvider = ({ review = false, onToggle, children }) => (
  <ReviewModeContext.Provider
    value={{ review: !!review, setReview: onToggle ?? (() => {}) }}
  >
    {
      // Only when on: providing it (undefined) when off would shadow an outer
      // DisclosureDefaultProvider (the playground's Expand all / Collapse all).
      review ? (
        <DisclosureDefaultProvider value="open">
          {children}
        </DisclosureDefaultProvider>
      ) : (
        children
      )
    }
  </ReviewModeContext.Provider>
);

ReviewModeProvider.propTypes = {
  review: PropTypes.bool,
  onToggle: PropTypes.func,
  children: PropTypes.node,
};

// false outside a provider (the leaf-block stories, the tests).
export const useReviewMode = () => React.useContext(ReviewModeContext).review;

// The toggle's setter; a no-op outside a provider.
export const useReviewModeToggle = () =>
  React.useContext(ReviewModeContext).setReview;
