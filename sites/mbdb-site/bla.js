const x = {
  metadata: {
    General_parameters: {
      schema_version: "0.9.14",
      record_information: {
        title: "fds",
        keywords: ["fds"],
        measurement_group_id: "4438f6e8-7db7-4c26-b0bd-a4322c102a52",
        access_rights: "embargoed access",
        metadata_access_rights: "restricted access",
        publisher: "MBDB",
        resource_type_general: "Dataset",
        resource_type: "MST",
        internal_id: "7633c7d5-6cab-4975-8f80-565d2f688cdd",
        identifier: "cb6cd988-0ff5-4d54-ae01-8097f828dd63",
        subject_category: "Biophysics",
        deposition_date: "2023-11-08",
        date_available: "2023-11-08",
      },
      depositors: {
        depositor: { given_name: "fds", family_name: "fds" },
        principal_contact: { given_name: "fds", family_name: "fds" },
      },
      technique:
        "Microscale thermophoresis/Temperature related intensity change (MST/TRIC)",
      collection_start_time: "2023-11-08",
      instrument: { name: "fds", manufacturer: "Malvern Panalytical" },
      chemical_information: {
        chemical_environments: [
          {
            id: "af0d109d-1f46-4e33-8d6c-a61d6c773209",
            name: "fds",
            solvent: [
              {
                name: "gdfs",
                inchikey: "sfds",
                molecular_weight: { value: 12, unit: "kDa" },
                concentration: { value: 12, unit: "w/v %" },
                type: "Chemical",
              },
            ],
            pH: { value: 12, obtained_by: "Assumption" },
            degassing_method: "Heating",
          },
        ],
        entities_of_interest: [
          {
            name: "fdsfds",
            polymer_type: "polyribonucleotide",
            molecular_weight: { value: 13, unit: "Da" },
            variant: "fdsd",
            expression_source_type: "Recombinantly",
            id: "235ea59c-c808-4246-b8fd-e7f7cbad76ca",
            type: "Polymer",
          },
        ],
      },
    },
    method_specific_parameters: {
      schema_version: "0.9.6",
      experiment_type: "Affinity",
      signal_type: "TRIC/MST",
      excitation_led_color: "UV (ex 260-300nm, em 330-380nm)",
      excitation_led_power: 12,
      ir_mst_laser_power: 13,
      measurements: [
        {
          id: "6a9895e5-6ad5-4700-96f6-94431edf0385",
          name: "fdsfds",
          position: "jfkds",
          sample: {
            targets: [
              {
                entity: {
                  id: "235ea59c-c808-4246-b8fd-e7f7cbad76ca",
                  name: "fdsfds",
                },
                concentration: { value: 13, unit: "w/v %" },
              },
            ],
            ligands: [
              {
                entity: {
                  id: "235ea59c-c808-4246-b8fd-e7f7cbad76ca",
                  name: "fdsfds",
                },
                concentration: { value: 15, unit: "v/w %" },
              },
            ],
            chemical_environment: {
              id: "af0d109d-1f46-4e33-8d6c-a61d6c773209",
              name: "fds",
            },
            container: "Monolith NT.Automated LabelFree Premium Capillary Chip",
          },
        },
      ],
    },
  },
};
