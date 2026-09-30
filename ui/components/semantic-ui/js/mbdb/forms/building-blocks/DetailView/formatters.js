import React, { useState } from "react";
import PropTypes from "prop-types";

// Path-suffix formatters for DetailView. The key is matched against the leaf
// name of a field path; add one only when the generic output is poor
// (design/building-blocks/DetailView.md §3). Everything not listed here —
// {value, unit} objects, {id} vocabularies, locations, booleans, arrays —
// is handled generically by DetailView.

const WRAP = 60;

// Monospace, first 60 characters, plus the residue count. [Show all] expands
// to the full sequence wrapped at 60 characters (design §3).
const SequenceValue = ({ value }) => {
  const [all, setAll] = useState(false);
  const shown = all
    ? value.match(new RegExp(`.{1,${WRAP}}`, "g"))?.join("\n") ?? value
    : value.slice(0, WRAP);
  return (
    <span>
      <code className={all ? "mbdb-pre-line" : undefined}>{shown}</code>{" "}
      {`(${value.length} residues)`}{" "}
      {value.length > WRAP && (
        <button
          type="button"
          className="mbdb-link"
          onClick={() => setAll((prev) => !prev)}
        >
          {all ? "[Show less]" : "[Show all]"}
        </button>
      )}
    </span>
  );
};

SequenceValue.propTypes = {
  value: PropTypes.string.isRequired,
};

// Each entry is a formatter component: (value) => JSX.
export const formatters = {
  sequence: (value) => <SequenceValue value={value} />,
};
