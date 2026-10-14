import React, { useRef } from "react";
import PropTypes from "prop-types";
import { Input } from "mbdb-semantic-ui-react";

// The digit boxes of an ORCID: 16 single-digit inputs in four groups,
// separated by dashes (0000-0000-0000-0007). Controlled: the parent owns the
// digits — an array of exactly `length` strings, each "" or one digit — so a
// digit typed into a middle box keeps its position. Typing, pasting and
// keyboard navigation (arrows, backspace) behave like one input. On paste
// anything but digits is dropped, so pasting a full "https://orcid.org/
// 0000-…-0007" URL fills the boxes too. The styles are one LESS block
// (custom-components.less, .mbdb-orcid). Ported from mbdb-app-rdm-12's
// OrcidInput: each group is one joined segment of boxes, as there.
export const OrcidInput = ({ value, onChange, length = 16, groupSize = 4 }) => {
  const inputRefs = useRef([]);
  // The current digits, always padded to the full box count.
  const digits = Array.from({ length }, (_, index) => value?.[index] ?? "");

  const handleChange = (input, index) => {
    // One digit at a time; anything else (letters, a second digit) is ignored
    if (!/^\d?$/.test(input)) return;
    const next = [...digits];
    next[index] = input;
    onChange(next);
    if (input !== "" && index < length - 1)
      inputRefs.current[index + 1]?.focus();
  };

  const handleKeyDown = (e, index) => {
    // Backspace on an empty box clears and focuses the previous one
    if (e.key === "Backspace" && !digits[index] && index > 0) {
      e.preventDefault();
      const next = [...digits];
      next[index - 1] = "";
      onChange(next);
      inputRefs.current[index - 1]?.focus();
    }
    if (e.key === "ArrowRight" && index < length - 1)
      inputRefs.current[index + 1]?.focus();
    if (e.key === "ArrowLeft" && index > 0)
      inputRefs.current[index - 1]?.focus();
  };

  const handlePaste = (e) => {
    e.preventDefault();
    const pasted = (e.clipboardData.getData("text") ?? "")
      .replace(/[^0-9]/g, "")
      .slice(0, length);
    const next = Array.from({ length }, (_, index) => pasted[index] ?? "");
    onChange(next);
    inputRefs.current[pasted.length - 1]?.focus();
  };

  return (
    <div className="mbdb-orcid">
      {Array.from(
        { length: Math.ceil(length / groupSize) },
        (_, groupIndex) => (
          <React.Fragment key={groupIndex}>
            {groupIndex > 0 && <span className="mbdb-orcid-dash">-</span>}
            <div className="mbdb-orcid-group">
              {Array.from({ length: groupSize }, (_, index) => {
                const overallIndex = groupIndex * groupSize + index;
                return (
                  <Input
                    key={overallIndex}
                    className="mbdb-orcid-box"
                    type="text"
                    maxLength={1}
                    inputMode="numeric"
                    value={digits[overallIndex]}
                    onChange={(e, { value: input }) =>
                      handleChange(input, overallIndex)
                    }
                    onKeyDown={(e) => handleKeyDown(e, overallIndex)}
                    onPaste={handlePaste}
                    // the ref is the Input instance, whose focus() focuses the box
                    ref={(ref) => {
                      inputRefs.current[overallIndex] = ref;
                    }}
                  />
                );
              })}
            </div>
          </React.Fragment>
        )
      )}
    </div>
  );
};

OrcidInput.propTypes = {
  // the digits the parent stores (exactly `length` strings, "" or one digit)
  value: PropTypes.arrayOf(PropTypes.string),
  // called with the new array after every box change
  onChange: PropTypes.func.isRequired,
  length: PropTypes.number,
  groupSize: PropTypes.number,
};
