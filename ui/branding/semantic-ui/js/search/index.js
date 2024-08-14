import React from "react";
import ReactDOM from "react-dom";
import ChooseSearchMethodDropdown from "./ChooseSearchMethodDropdown";
import DeleteButton from "./DeleteButton";
import TemplateButton from "./TemplateButton";


document.addEventListener("DOMContentLoaded", () => {
  const depositButton = document.getElementById("search-dropdown");
  const deleteButton = document.getElementById("delete-button");
  const templateButton = document.getElementById("template-button");
  if (depositButton) {
    ReactDOM.render(<ChooseSearchMethodDropdown />, depositButton);
  }

  if (deleteButton) {
    const selfLink = deleteButton.getAttribute("data-selflink");
    ReactDOM.render(<DeleteButton selfLink={selfLink} />, deleteButton);
  }
  if (templateButton) {
    const selfLink = templateButton.getAttribute("data-selflink");
    ReactDOM.render(<TemplateButton selfLink={selfLink} />, templateButton);
  }
});
