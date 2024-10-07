import React from "react";
import { useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";

export default function PreviewButton() {
  const { save, values: recordMetadata } = useDepositApiClient();

  console.log(recordMetadata, "RecordMetadata");

  async function preview() {
    await save(true);

    const selfLink = recordMetadata?.links?.self_html;

    if (selfLink) {
      window.location.href = selfLink;
    } else {
      console.error("selfLink is not available");
    }
  }

  return (
    <div>
      <Button
        style={{ backgroundColor: "#023850", color: "white" }}
        onClick={preview}
      >
        Preview
      </Button>
    </div>
  );
}
