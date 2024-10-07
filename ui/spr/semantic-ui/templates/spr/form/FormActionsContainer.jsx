import React from "react";
import PublishButton from "./PublishButton";
import PreviewButton from "./PreviewButton";

export const FormActionsContainer = ({ record }) => {
  return (
    <div className="ml-3 flex">
      <div className="mr-3">
        <PublishButton />
      </div>
      <PreviewButton />
    </div>
  );
};

export default FormActionsContainer;
