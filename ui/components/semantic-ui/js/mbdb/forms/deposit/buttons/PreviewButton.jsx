import React from "react";
import { useDepositApiClient } from "@js/oarepo_ui";

export default function PreviewButton() {
  const { save, values: recordMetadata } = useDepositApiClient();

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
      <button
        className="transition-all bg-dark text-white px-6 h-[36px] rounded-normal font-JostMedium hover:bg-dark/75"
        onClick={preview}
      >
        Preview
      </button>
  );
}