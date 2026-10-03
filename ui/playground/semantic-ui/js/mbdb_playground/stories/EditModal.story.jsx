import React, { useState } from "react";
import { Button, Form, Input, Message } from "mbdb-semantic-ui-react";
import { EditModal } from "@js/mbdb/forms/building-blocks/EditModal";

// The shared modal shell used by ModalArrayField and ModalObjectField. The
// open/close state is local here: the caller owns the session (snapshot,
// what Cancel restores, what Done keeps); the shell only reports the choice.
// A dimmer click does nothing; Escape is Cancel.
const LONG =
  "The modal body scrolls when the content is taller than the viewport. ".repeat(
    40
  );

const makeDemo = (long) => {
  const Demo = () => {
    const [open, setOpen] = useState(true);
    return (
      <>
        <Message
          info
          size="small"
          content="Cancel and Done just close the modal here. Try a click on the dimmer: nothing is discarded (closeOnDimmerClick is off)."
        />
        <Button type="button" onClick={() => setOpen(true)}>
          Open modal
        </Button>
        <EditModal
          header="Edit item"
          open={open}
          onCancel={() => setOpen(false)}
          onDone={() => setOpen(false)}
        >
          <Form.Field>
            <label htmlFor="edit-modal-demo-name">Name</label>
            <Input id="edit-modal-demo-name" placeholder="Lysozyme" />
          </Form.Field>
          {long && <p>{LONG}</p>}
        </EditModal>
      </>
    );
  };
  return Demo;
};

const story = {
  title: "EditModal",
  scenarios: [
    { name: "Open", initialValues: {}, render: makeDemo(false) },
    {
      name: "Long content (scrolls)",
      initialValues: {},
      render: makeDemo(true),
    },
  ],
};

export default story;
