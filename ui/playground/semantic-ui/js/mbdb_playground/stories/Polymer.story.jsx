import React from "react";
import { PolymerFields } from "@js/mbdb/forms/entities/Polymer";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <PolymerFields fieldPath={ENTITY_PATH} />;

const story = {
  title: "Polymer",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Polymer"), render: Fields },
    {
      name: "Filled",
      // sample record, "Hemoglobin subunit beta" (there an assembly component)
      initialValues: entityValues("Polymer", {
        name: "Hemoglobin subunit beta",
        polymer_type: "polypeptide(L)",
        expression_source_type: "Recombinantly",
        variant: "V2A",
        sequence:
          "MAHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH",
        molecular_weight: { value: 16.0, unit: "kDa" },
        external_databases: ["Uniprot:P68871"],
        source_organism: { id: "taxid:12374" },
        modifications: {
          biological_postprocessing: [
            { position: "S10", type: "Phosphorylation" },
          ],
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        name: "Hemoglobin subunit beta",
      }),
      initialErrors: entityErrors(
        "polymer_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
