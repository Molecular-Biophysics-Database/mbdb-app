import React from "react";
import ReactDOM from "react-dom";
import ChooseSearchMethodDropdown from "./ChooseSearchMethodDropdown";
import DeleteButton from "./DeleteButton";

document.addEventListener("DOMContentLoaded", () => {
  const depositButton = document.getElementById("search-dropdown");
  const deleteButton = document.getElementById("delete-button");

  if (depositButton) {
    ReactDOM.render(<ChooseSearchMethodDropdown />, depositButton);
  }

  if (deleteButton) {
    const selfLink = deleteButton.getAttribute("data-selflink");
    ReactDOM.render(<DeleteButton selfLink={selfLink} />, deleteButton);
  }
});
