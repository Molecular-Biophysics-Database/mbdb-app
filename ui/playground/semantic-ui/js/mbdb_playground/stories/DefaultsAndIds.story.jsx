import React from "react";
import { Message } from "mbdb-semantic-ui-react";
import { useFormikContext, getIn } from "formik";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { ensureEntityIds } from "@js/mbdb/forms/building-blocks/DefaultsAndIds";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { Button } from "mbdb-semantic-ui-react";

const PATH = "metadata.general_parameters.entities_of_interest";

// Defaults are written at the moment an item is created (withIds), never in
// an effect afterwards. Existing entities without an id get one in a
// one-time pass on form load (here: a button, in the section: on load).
const IdPass = () => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <Button
      type="button"
      size="small"
      onClick={() => {
        const list = getIn(values, PATH);
        // identical-reference contract: callers write only when ids changed
        const withIds = ensureEntityIds(list);
        if (withIds !== list) setFieldValue(PATH, withIds);
      }}
    >
      One-time id pass
    </Button>
  );
};

const Entities = () => (
  <>
    <Message
      info
      size="small"
      content="Add a Polymer/Chemical: the new entity gets `id` + `type` at push time. Open the Form values panel to watch it. Components would be pushed without an id (no withIds). The Filled scenario has entities without ids; use the button for the one-time load pass."
    />
    <ModalArrayField
      fieldPath={PATH}
      label="Entities of interest"
      itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
      columns={[
        { title: "Name", value: (v) => v.name },
        { title: "Type", value: (v) => v.type },
      ]}
      newItemOptions={["Polymer", "Chemical"].map((t) => ({
        label: t,
        value: { type: t },
      }))}
      withIds
      renderForm={(itemPath) => <TextField fieldPath={`${itemPath}.name`} />}
    />
    <IdPass />
  </>
);

const story = {
  title: "Defaults and ids",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Entities },
    {
      name: "Filled (legacy, no ids)",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { type: "Polymer", name: "Lysozyme" },
              { id: "e-2", type: "Chemical", name: "NaCl" },
            ],
          },
        },
      },
      render: Entities,
    },
  ],
};

export default story;
