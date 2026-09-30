import React, { useState } from "react";
import { Button, Divider, Input } from "mbdb-semantic-ui-react";
import { FieldHelp } from "mbdb-semantic-ui-react";
import { TextField } from "mbdb-react-invenio-forms";

// FieldHelp is the one place where help texts are rendered. The mode is a
// module constant in mbdb-semantic-ui-react/FieldHelp.jsx, not a prop passed
// by fields; this story toggles it locally only to preview both looks.

// metadata.title is a plain keyword path with a ui_model entry, so the
// wrapped field reads label/help/required from the model without overrides.
// `metadata.record_information.title` has a ui_model entry (see the model),
// so the wrapped field reads label/help/required from the model.
const TITLE = "metadata.record_information.title";

const Demo = () => {
  const [mode, setMode] = useState("invenio");
  return (
    <>
      <Button
        type="button"
        size="small"
        onClick={() => setMode(mode === "invenio" ? "popup" : "invenio")}
      >
        Preview mode: {mode}
      </Button>
      <Divider />
      <span>
        Standalone FieldHelp:{" "}
        <FieldHelp help="Help text in grey, small." mode={mode} />
      </span>
      <p>
        Wrapped RIF TextField on `metadata.record_information.title`
        (label/help/required from the model):
      </p>
      <TextField fieldPath={TITLE} />
      <p>A plain input renders no help (nothing renders without it):</p>
      <Input placeholder="Plain input, no FieldHelp" />
      <code>(blank)</code>
    </>
  );
};

const story = {
  title: "AliasPackages and FieldHelp",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Demo },
    {
      name: "Filled",
      initialValues: {
        metadata: { record_information: { title: "MST of lysozyme vs NAG3" } },
      },
      render: Demo,
    },
    {
      name: "With errors",
      initialValues: { metadata: { record_information: { title: "" } } },
      initialErrors: {
        metadata: {
          record_information: { title: "Missing data for required field." },
        },
      },
      render: Demo,
    },
  ],
};

export default story;
