import React from "react";
import { i18next } from "@translations/oarepo_ui/i18next";
import { useDepositApiClient } from "@js/oarepo_ui";

export const SaveButton = React.memo(({ ...uiProps }) => {
  const { isSubmitting, save } = useDepositApiClient();
  return (
    <div>
        <button
          name="save"
          class="flex justify-center w-[120px] py-2 text-20px bg-dark rounded-normal text-white hover:bg-secondary hover:text-dark transition-all"
          disabled={isSubmitting}
          loading={isSubmitting}
          onClick={() => save()}
          content={i18next.t("Save")}
          type="submit"
          {...uiProps}
        >Save</button>
    </div>
  );
});

export default SaveButton;