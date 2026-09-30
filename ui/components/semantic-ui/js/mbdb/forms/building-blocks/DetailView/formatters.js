import React from "react";
import PropTypes from "prop-types";

// Path-suffix formatters for DetailView. The key is matched against the leaf
// name of a field path; add one only when the generic output is poor
// (design/building-blocks/DetailView.md §3). Everything not listed here —
// {value, unit} objects, {id} vocabularies, locations, booleans, arrays —
// is handled generically by DetailView.

// Monospace, first 60 characters, plus the residue count.
const SequenceValue = ({ value }) => (
  <span>
    <code>{value.slice(0, 60)}</code> {`(${value.length} residues)`}
  </span>
);

SequenceValue.propTypes = {
  value: PropTypes.string.isRequired,
};

export const formatters = {
  sequence: (value) => <SequenceValue value={value} />,
};
