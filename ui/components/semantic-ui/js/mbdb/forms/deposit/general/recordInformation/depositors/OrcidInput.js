import React from "react";
import { useRef, useEffect, useState } from "react";

function OrcidInput({ length = 16, groupSize = 4, onComplete, orcid }) {
  const inputRefs = useRef([]); // Ref to store reference to all input fields for easy focus control
  const [orcidDigits, setOrcidDigits] = useState(Array(length).fill("")); // Holds individual ORCID digits as an array of strings

  // Sync internal ORCID input state with external prop unless already matching
  useEffect(() => {
    if (typeof orcid === "string") {
      const digits = orcid.replace(/[^0-9]/g, "").split("").slice(0, length);
      const isSame = digits.join("") === orcidDigits.join("");
  
      if (!isSame) {
        setOrcidDigits([...digits, ...Array(length - digits.length).fill("")]);
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [orcid, length]);

  const handleChange = (input, index) => {  
    // Only allow a single digit (0–9)
    if (!/^\d?$/.test(input)) return;
      
    // Ignore multi-character input
    if (input.length > 1) return;

    // Create a new array and update the digit at the current index
    const updatedOrcidDigits = [...orcidDigits];
    updatedOrcidDigits[index] = input;
    setOrcidDigits(updatedOrcidDigits);

    // Automatically focus the next input if a digit was entered and we're not at the end
    if (input !== "" && index < length - 1) {
      inputRefs.current[index + 1]?.focus();
    }
  };

  const handleKeyDown = (e, index) => {
    // Handle backspace: if the current field is empty, move focus to the previous field and clear it
    if (e.key === "Backspace" && !orcidDigits[index] && index > 0) {
      e.preventDefault();
      const updatedOrcidDigits = [...orcidDigits];
      inputRefs.current[index - 1]?.focus();
      updatedOrcidDigits[index - 1] = "";
      setOrcidDigits(updatedOrcidDigits);
    }

    // Navigate to the next field using the right arrow key
    if (e.key === "ArrowRight" && index < length - 1) {
      inputRefs.current[index + 1]?.focus();
    }

    // Navigate to the previous field using the left arrow key
    if (e.key === "ArrowLeft" && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e) => {
    // Prevent default paste behavior
    e.preventDefault();

    // Extract only digits from the pasted text
    const pastedText = e.clipboardData.getData("text").replace(/[^0-9]/g, "");
    // Convert the digits into an array and limit it to the allowed ORCID length
    const characters = pastedText.split("").slice(0, length);

    // Create a new array of fixed length and fill it with pasted characters
    const newPin = Array(length).fill("");
    characters.forEach((char, index) => {
      if (inputRefs.current[index]) {
        newPin[index] = char;
      }
    });

    setOrcidDigits(newPin);

    // Move focus to the last filled input field
    const lastFilledIndex = characters.length - 1;
    if (inputRefs.current[lastFilledIndex]) {
      inputRefs.current[lastFilledIndex]?.focus();
    }
  };

  const formatORCID = (orcidArray) => {
    // Join the array of digits into a single string
    const orcidString = orcidArray.join("");
    // Group the string into segments (e.g., "0000-0000-0000-0000")
    const formattedString =
      orcidString.match(new RegExp(`.{1,${groupSize}}`, "g"))?.join("-") || "";
    return formattedString;
  };

  return (
    <div className="flex">
      {Array.from({ length: length / groupSize }, (_, groupIndex) => (
        <div key={groupIndex} className="flex">
          {Array.from({ length: groupSize }, (_, index) => {
            const overallIndex = groupIndex * groupSize + index;
            return (
              <input
                key={overallIndex}
                type="text"
                maxLength={1}
                value={orcidDigits[overallIndex]}
                onChange={(e) => handleChange(e.target.value, overallIndex)}
                onKeyDown={(e) => handleKeyDown(e, overallIndex)}
                onPaste={handlePaste}
                ref={(ref) => (inputRefs.current[overallIndex] = ref)}
                className={`!border-gray focus:!border-dark !rounded-none 
                  ${
                    index === 0
                      ? "!rounded-tl-normal !rounded-bl-normal"
                      : "!border-l-0 focus:!border-l"
                  }
                  ${
                    index === groupSize - 1
                      ? "!rounded-tr-normal !rounded-br-normal"
                      : ""
                  }
                  p-0 !w-8 text-center`}
              />
            );
          })}
          {groupIndex < length / groupSize - 1 && (
            <span className="text-2xl font-semibold mx-2">-</span>
          )}
        </div>
      ))}
      {orcidDigits.every((digit) => digit !== "") && (
        <button className="bg-dark text-primary rounded-normal font-JostSemiBold px-2 ml-2 hover:bg-dark/85 transition-all" onClick={() => onComplete(formatORCID(orcidDigits))}>Prefill</button>
      )}
    </div>
  );
}

export default OrcidInput;