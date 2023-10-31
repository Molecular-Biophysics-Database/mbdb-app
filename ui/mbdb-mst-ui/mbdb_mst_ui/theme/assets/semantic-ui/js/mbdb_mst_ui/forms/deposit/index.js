import React from "react";
import ReactDOM from "react-dom";
import { getInputFromDOM } from "@js/oarepo_ui";
import { DepositForm } from "./DepositForm";

function initFormApp(rootElement) {
    const formConfig = getInputFromDOM("form-config");
    const initialRecord = getInputFromDOM("record");

    ReactDOM.render(
        <DepositForm
            createDraftUrl={formConfig.updateUrl ?? formConfig.createUrl}
            update={formConfig.updateUrl ? true : false}
            initialRecord={initialRecord}
        />,
        rootElement
    );
}

export function createFormAppInit() {
    const appRoot = document.getElementById("form-app");
    initFormApp(appRoot);
}

createFormAppInit();
