import React from "react";
import { Input } from "mbdb-semantic-ui-react";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";

// The one frame every single-value field renders (design/index.md "one root
// element"): label, control, error messages and help, in that order. Use the
// Help switch in the page header to see both help modes.
const Required = () => (
  <FieldShell
    inputId="field-shell-required"
    label="Name"
    help="Short descriptive name."
    required
  >
    <Input id="field-shell-required" placeholder="Lysozyme" />
  </FieldShell>
);

const WithError = () => (
  <FieldShell
    inputId="field-shell-error"
    label="Name"
    messages={["Missing data for required field."]}
  >
    <Input id="field-shell-error" />
  </FieldShell>
);

const Composite = () => (
  <FieldShell label="A composite control (no inputId)">
    <Input />
  </FieldShell>
);

const NoLabel = () => (
  <FieldShell inputId="field-shell-no-label">
    <Input id="field-shell-no-label" placeholder="No label slot" />
  </FieldShell>
);

const story = {
  title: "FieldShell",
  scenarios: [
    { name: "Label, help, required", initialValues: {}, render: Required },
    { name: "With an error", initialValues: {}, render: WithError },
    { name: "Composite (no inputId)", initialValues: {}, render: Composite },
    { name: "No label", initialValues: {}, render: NoLabel },
  ],
};

export default story;
