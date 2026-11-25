import React from "react";
import ReactDOM from "react-dom";
import { AdvancedSearch } from "./AdvancedSearch";

const root = document.getElementById("advanced-search");
ReactDOM.render(
  <AdvancedSearch
    fields={JSON.parse(root.dataset.fields)}
    targets={JSON.parse(root.dataset.targets)}
  />,
  root
);
