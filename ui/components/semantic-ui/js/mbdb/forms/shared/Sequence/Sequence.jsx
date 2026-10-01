import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Label } from "mbdb-semantic-ui-react";
import { TextAreaField } from "@js/mbdb/forms/building-blocks/TextField";
import { blastUrl, countResidues, normalizeSequence } from "./sequence";

// The primary sequence of a polymer: a monospace textarea, a BLAST lookup link
// and a residue counter. Normalization (drop FASTA header, strip whitespace) is
// onBlur only — never on every keystroke or in an effect, or the cursor would
// jump mid-paste. The blur handler reads the value from Formik because the
// DOM value can lag one keystroke in tests and because semantic may pass the
// event only.
export const Sequence = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  const sequence = getIn(values, fieldPath);
  return (
    <>
      <TextAreaField
        fieldPath={fieldPath}
        monospace
        autoHeight
        onBlur={() => {
          const current = getIn(values, fieldPath);
          const normalized = normalizeSequence(current);
          // Skip the write when already normalized: setFieldValue clones the
          // whole values tree, so a no-op blur would still rerender every
          // field that reads `values` by reference.
          if (normalized !== current) setFieldValue(fieldPath, normalized);
        }}
        links={
          sequence
            ? [{ label: "BLAST ↗", href: blastUrl(sequence) }]
            : undefined
        }
      />
      <Label basic size="tiny">
        {`${countResidues(sequence)} residues`}
      </Label>
    </>
  );
};

Sequence.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
