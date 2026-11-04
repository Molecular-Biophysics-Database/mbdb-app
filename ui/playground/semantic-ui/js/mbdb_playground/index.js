import React from "react";
import ReactDOM from "react-dom";
import { PlaygroundApp } from "./PlaygroundApp";
// the playground's rdm-12 skin, in the entry so the page loads it
import "./mbdb_playground.less";

const rootEl = document.getElementById("mbdb-playground");

if (rootEl) {
  const uiModel = JSON.parse(rootEl.dataset.uiModel || "{}");
  ReactDOM.render(<PlaygroundApp uiModel={uiModel} />, rootEl);
}
