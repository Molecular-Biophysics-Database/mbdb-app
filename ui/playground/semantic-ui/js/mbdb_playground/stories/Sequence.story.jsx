import React from "react";
import { Sequence } from "@js/mbdb/forms/shared/Sequence";

const FIELD = "metadata.general_parameters.entities_of_interest.0.sequence";

const Content = () => <Sequence fieldPath={FIELD} />;

const story = {
  title: "Sequence",
  scenarios: [
    {
      name: "Empty",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ type: "Polymer" }],
          },
        },
      },
      render: Content,
    },
    {
      name: "Filled",
      // Hemoglobin subunit beta (design fixture)
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                type: "Polymer",
                sequence:
                  "MAHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH",
              },
            ],
          },
        },
      },
      render: Content,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ type: "Polymer", sequence: "MAH LTP" }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ sequence: "Invalid sequence." }],
          },
        },
      },
      render: Content,
    },
    {
      // blur the textarea to see the FASTA header stripped and whitespace folded
      name: "FASTA paste",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                type: "Polymer",
                sequence: ">sp|P68871|HBB_HUMAN\nMVHLTPEEKS\nAVTALWGKVN",
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
