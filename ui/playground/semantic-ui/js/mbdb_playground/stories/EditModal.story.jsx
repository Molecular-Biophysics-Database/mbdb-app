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

// A nested modal (design ModalArrayField.md, "where am I in stacked modals"):
// the inner modal shows the parent's crumb above its title, names the
// destination on its Done button ("Done, back to assembly"), and is one size
// smaller than the outer one, so the entity's modal stays visible around it.
const Nested = () => {
  const [outer, setOuter] = useState(true);
  const [inner, setInner] = useState(false);
  return (
    <>
      <Message
        info
        size="small"
        content="Open the component modal inside the entity's: the inner header shows the parent crumb, its Done names the destination, and it is smaller than the outer modal."
      />
      <Button type="button" onClick={() => setOuter(true)}>
        Open entity modal
      </Button>
      <EditModal
        header="Edit entity: human Hemoglobin"
        crumb={{
          label: "human Hemoglobin (Molecular assembly)",
          noun: "assembly",
        }}
        open={outer}
        onCancel={() => setOuter(false)}
        onDone={() => setOuter(false)}
      >
        <Button type="button" onClick={() => setInner(true)}>
          Edit component
        </Button>
        <EditModal
          header="Edit Hemoglobin subunit alpha"
          crumb={{ label: "Hemoglobin subunit alpha", noun: "component" }}
          open={inner}
          onCancel={() => setInner(false)}
          onDone={() => setInner(false)}
        >
          <Form.Field>
            <label htmlFor="edit-modal-nested-name">Name</label>
            <Input
              id="edit-modal-nested-name"
              placeholder="Hemoglobin subunit alpha"
            />
          </Form.Field>
        </EditModal>
      </EditModal>
    </>
  );
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
    { name: "Nested (stacked)", initialValues: {}, render: Nested },
  ],
};

export default story;
