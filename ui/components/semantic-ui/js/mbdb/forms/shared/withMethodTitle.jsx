import React from "react";

// The section with "You are depositing MST data" on top; `method` is the form's
// method code (MST, BLI, …).
export const withMethodTitle = (method, Section) => {
  const TitledSection = (props) => (
    <>
      <h2 className="mbdb-method-title">You are depositing {method} data</h2>
      <Section {...props} />
    </>
  );
  return TitledSection;
};
