import React from "react";
import { Sequence } from "@js/mbdb/forms/shared/Sequence";
import { entityPath, entityValues, entityErrors } from "../fixtures";

const FIELD = entityPath("sequence");

const Content = () => <Sequence fieldPath={FIELD} />;

const story = {
  title: "Sequence",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Polymer"),
      render: Content,
    },
    {
      name: "Filled",
      // Hemoglobin subunit beta (design fixture)
      initialValues: entityValues("Polymer", {
        sequence:
          "MAHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH",
      }),
      render: Content,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", { sequence: "MAH LTP" }),
      initialErrors: entityErrors("sequence", "Invalid sequence."),
      render: Content,
    },
    {
      // blur the textarea to see the FASTA header stripped and whitespace folded
      name: "FASTA paste",
      initialValues: entityValues("Polymer", {
        sequence: ">sp|P68871|HBB_HUMAN\nMVHLTPEEKS\nAVTALWGKVN",
      }),
      render: Content,
    },
  ],
};

export default story;
