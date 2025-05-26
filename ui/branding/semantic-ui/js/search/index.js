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

document.addEventListener("DOMContentLoaded", () => {
  const mainTabs = document.querySelectorAll(".main-tab");
  const mainContents = document.querySelectorAll(".main-tab-content");

  function activateMainTab(tabId) {
    mainContents.forEach((content) => content.classList.add("hidden"));

    mainTabs.forEach((tab) => {
      tab.classList.remove("bg-primary");
      tab.classList.add("hover:bg-primary/50");
    });

    const tabToShow = document.getElementById(tabId);
    if (tabToShow) {
      tabToShow.classList.remove("hidden");
    }

    const activeTab = document.querySelector(`[data-main-tab="${tabId}"]`);
    if (activeTab) {
      activeTab.classList.add("bg-primary");
      activeTab.classList.remove("hover:bg-primary/50");
    }
  }

  mainTabs.forEach((tab) => {
    tab.addEventListener("click", function () {
      const tabId = this.getAttribute("data-main-tab");
      if (tabId) {
        activateMainTab(tabId);
      }
    });
  });

  activateMainTab("tab1");
});
