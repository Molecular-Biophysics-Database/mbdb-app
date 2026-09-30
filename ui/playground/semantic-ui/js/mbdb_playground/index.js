import React from "react";
import ReactDOM from "react-dom";
import { PlaygroundApp } from "./PlaygroundApp";

const rootEl = document.getElementById("mbdb-playground");

if (rootEl) {
  const uiModel = JSON.parse(rootEl.dataset.uiModel || "{}");
  ReactDOM.render(<PlaygroundApp uiModel={uiModel} />, rootEl);
}
