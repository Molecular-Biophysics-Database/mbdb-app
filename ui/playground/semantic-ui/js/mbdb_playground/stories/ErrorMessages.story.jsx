import React from "react";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";

// The one look for block-level error messages. Nothing renders for an empty
// list, so callers can render it unconditionally.
const Intro = () => (
  <p>
    Below is the label when the list has messages, and nothing when it is empty:
  </p>
);

const Empty = () => (
  <>
    <Intro />
    <ErrorMessages messages={[]} />
    <p>(end)</p>
  </>
);

const One = () => (
  <>
    <Intro />
    <ErrorMessages messages={["Missing data for required field."]} />
    <p>(end)</p>
  </>
);

const Two = () => (
  <>
    <Intro />
    <ErrorMessages messages={["First problem.", "Second problem."]} />
    <p>(end)</p>
  </>
);

const story = {
  title: "ErrorMessages",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Empty },
    { name: "One message", initialValues: {}, render: One },
    { name: "Two messages", initialValues: {}, render: Two },
  ],
};

export default story;
