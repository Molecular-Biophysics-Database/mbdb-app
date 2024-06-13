import React from "react";
import { DeleteButton } from "@js/oarepo_ui";
import SaveButton from "./SaveButton";
import PublishButton from "./PublishButton";

export const FormActionsContainer = ({ record }) => {
  return (
    <div className="flex ml-3 -mb-3">
      <div className="mr-4">
        <SaveButton/>
      </div>
      <div>
        <PublishButton />
      </div>
      <div>
        <DeleteButton redirectUrl="/mst/" />
      </div>
    </div>
  );
};

export default FormActionsContainer;