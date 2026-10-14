import React from "react";
import { LipidAssemblyDetails } from "@js/mbdb/forms/shared/LipidAssemblyDetails";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <LipidAssemblyDetails fieldPath={ENTITY_PATH} />;

// Constructed (no sample record has a lipid assembly); the component uses the
// Water chemical so its title resolves.
const FIELDS = {
  name: "POPC liposomes",
  assembly_type: "Liposome",
  number_of_mono_layers: 2,
  size: { type: "diameter", unit: "nm", mean: 120, lower: 90, upper: 150 },
  components: [
    {
      type: "Chemical",
      name: "Water",
      copy_number: -1,
      basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
    },
  ],
};

const WITHOUT_ASSEMBLY_TYPE = { ...FIELDS };
delete WITHOUT_ASSEMBLY_TYPE.assembly_type;

const story = {
  title: "Lipid assembly details",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        {},
        { class: "Lipid assembly" }
      ),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        FIELDS,
        { class: "Lipid assembly" }
      ),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        WITHOUT_ASSEMBLY_TYPE,
        { class: "Lipid assembly" }
      ),
      initialErrors: entityErrors(
        "assembly_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
