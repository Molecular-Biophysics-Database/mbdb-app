import ReactDOM from "react-dom";
import React from "react";
import ChooseSearchMethodDropdown from "./ChooseSearchMethodDropdown";

document.addEventListener("DOMContentLoaded", () => {
  const depositButton = document.getElementById("search-dropdown");
  if (depositButton) {
    ReactDOM.render(<ChooseSearchMethodDropdown />, depositButton);
  }
});
