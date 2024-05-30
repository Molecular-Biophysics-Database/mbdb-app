import ReactDOM from "react-dom";
import React from "react";
import ChooseSearchMethodDropdown from "./ChooseSearchMethodDropdown"

const depositButton = document.getElementById('search-dropdown');
ReactDOM.render(
    <ChooseSearchMethodDropdown />,
    depositButton
);