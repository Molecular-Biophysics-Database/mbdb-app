import React from "react";
import { StringTableField } from "@js/mbdb/forms/building-blocks/StringTableField";
import { entityPath, entityValues } from "../fixtures";

const FIELD = entityPath("additional_specifications");

const Content = () => (
  <StringTableField
    fieldPath={FIELD}
    columnLabel="Specification"
    addButtonLabel="Add specification"
  />
);

const story = {
  title: "StringTableField",
  scenarios: [
    {
      name: "Empty",
      initialValues: {},
      render: Content,
    },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        additional_specifications: ["RNase free water", "desalted"],
      }),
      render: Content,
    },
    {
      name: "With errors",
      // a keyword-array item error lands AT the item path, not at a cell field
      initialValues: entityValues("Polymer", {
        additional_specifications: ["ok", ""],
      }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                additional_specifications: {
                  1: "Shorter than 1 character.",
                },
              },
            ],
          },
        },
      },
      render: Content,
    },
  ],
};

export default story;
