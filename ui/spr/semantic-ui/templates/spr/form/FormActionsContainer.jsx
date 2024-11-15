import React from "react";
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";

export const FormActionsContainer = ({ record }) => {
  return (
    <div className="ml-3 flex">
      <PreviewButton />
    </div>
  );
};

export default FormActionsContainer;
