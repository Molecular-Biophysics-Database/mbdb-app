import React from "react";
import { DeleteButton } from "@js/oarepo_ui";
import PublishButton from "./PublishButton";

export const FormActionsContainer = ({ record }) => {
  return (
    <div className="flex ml-3">
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