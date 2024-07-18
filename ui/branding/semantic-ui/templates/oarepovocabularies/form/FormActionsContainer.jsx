import React from "react";
import { PublishButton } from "./PublishButton";
import { useLocation } from "react-router-dom";

const VocabularyFormControlPanel = () => {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const newChildItemParentId = searchParams.get("h-parent");
  return (
    <>
      <PublishButton newChildItemParentId={newChildItemParentId} />
    </>
  );
};

export default VocabularyFormControlPanel;