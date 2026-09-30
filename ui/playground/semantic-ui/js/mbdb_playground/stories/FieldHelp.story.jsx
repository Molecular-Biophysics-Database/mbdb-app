import React, { useState } from "react";
import { Button, Divider, Input } from "mbdb-semantic-ui-react";
import { FieldHelp } from "mbdb-semantic-ui-react";

// FieldHelp is the one place where help texts are rendered. The mode is a
// module constant in mbdb-semantic-ui-react/FieldHelp.jsx, not a prop passed
// by fields; this story toggles it locally only to preview both looks.
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
      <div>
        <span>
          Name{" "}
          <FieldHelp help="Short descriptive name of the entity" mode={mode} />
        </span>
        <Input placeholder="Plain input; the help below comes from FieldHelp" />
        <FieldHelp
          help="Short descriptive name (id) of the entity; must be unique within a record."
          mode={mode}
        />
      </div>
      <p>Empty help renders nothing:</p>
      <FieldHelp help="" mode={mode} />
      <code>(blank above)</code>
    </>
  );
};

const story = {
  title: "AliasPackages and FieldHelp",
  scenarios: [{ name: "Invenio style", initialValues: {}, render: Demo }],
};

export default story;
