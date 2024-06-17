import React from "react";
import { i18next } from "@translations/oarepo_ui/i18next";
import { useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";

export const SaveButton = React.memo(({ ...uiProps }) => {
  const { isSubmitting, save } = useDepositApiClient();
  return (
    <div>
        <Button
          name="save"
          style={{ backgroundColor: "#023850", color: "white" }}
          disabled={isSubmitting}
          loading={isSubmitting}
          onClick={() => save()}
          content={i18next.t("Save")}
          type="submit"
          {...uiProps}
        >Save</Button>
    </div>
  );
});

export default SaveButton;