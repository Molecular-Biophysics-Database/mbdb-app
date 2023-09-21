import React from "react";
import ReactDOM from "react-dom";
import {getInputFromDOM} from "@js/oarepo_ui";


export function createFormAppInit() {
    const initFormApp = (rootElement) => {
        const record = getInputFromDOM("record");
        const formConfig = getInputFromDOM("form-config");
        const recordPermissions = getInputFromDOM("record-permissions");
        const links = getInputFromDOM("links");

        console.debug("Initializing form form app...");
        console.debug(
            "[record]:",
            record,
            "\n[formConfig]",
            formConfig,
            "\n[recordPermissions]",
            recordPermissions,
            "\n[UI links]",
            links
        );
        const stringifiedFormConfig = JSON.stringify(formConfig, null, 4);
        const stringifiedRecord = JSON.stringify(record, null, 4);

        ReactDOM.render(
            <>
                <h2>Form config</h2>
                <pre>{stringifiedFormConfig}</pre>
                <h2>Record</h2>
                <pre>{stringifiedRecord}</pre>
            </>,
            rootElement
        );
    }
    const appRoot = document.getElementById("form-app");
    initFormApp(appRoot)
}

createFormAppInit()