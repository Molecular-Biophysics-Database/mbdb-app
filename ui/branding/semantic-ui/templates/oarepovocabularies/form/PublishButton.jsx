import React from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/oarepo_vocabularies_ui/i18next";
import { useVocabularyApiClient } from "@js/oarepo_vocabularies";

export const PublishButton = ({ newChildItemParentId }) => {
  const { createOrUpdate } =
    useVocabularyApiClient(newChildItemParentId);
  return (
    <button
      onClick={() => createOrUpdate()}
      class="flex justify-center w-[100px] -my-4 py-1 text-20px bg-dark rounded-normal text-white hover:bg-secondary hover:text-dark transition-all"
      type="button"
    >{i18next.t("save")}</button>
  );
};

PublishButton.propTypes = {
  newChildItemParentId: PropTypes.string,
};