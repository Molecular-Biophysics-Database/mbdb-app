import React from "react";
import { FieldRow } from "@js/mbdb/forms/building-blocks/FieldRow";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { Input } from "mbdb-semantic-ui-react";

// A row that mixes a composite (a button group) with a simple control: both
// helps sit directly under their controls, so the two line up. This is the
// Purity case (design FieldRow.md, guide §8). Explicit texts: the demo paths
// have no model entry (guide §6).
const Mixed = () => (
  <FieldRow widths="equal">
    <SelectField
      fieldPath="demo.method"
      label="Method"
      help="The help sits under the select."
      options={["SDS-PAGE", "Capillary Electrophoresis"]}
    />
    <ButtonGroupField
      fieldPath="demo.purity_percentage"
      label="Purity percentage"
      help="…and under the buttons, at the same height."
      options={["<90 %", ">90 %", ">95 %", ">99 %"]}
    />
  </FieldRow>
);

// Outside a row a button group keeps its help under the label; a plain field's
// help is under its control in both cases.
const PlainRow = () => (
  <FieldRow widths="equal">
    <FieldShell inputId="demo-a" label="A" help="Help A, under the input.">
      <Input id="demo-a" />
    </FieldShell>
    <FieldShell inputId="demo-b" label="B" help="Help B, under the input.">
      <Input id="demo-b" />
    </FieldShell>
  </FieldRow>
);

const story = {
  title: "FieldRow",
  scenarios: [
    { name: "Mixed row (select + buttons)", initialValues: {}, render: Mixed },
    { name: "Row of plain fields", initialValues: {}, render: PlainRow },
  ],
};

export default story;
