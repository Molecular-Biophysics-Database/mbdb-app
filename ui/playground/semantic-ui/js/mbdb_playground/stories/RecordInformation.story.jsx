import React from "react";
import { RecordInformationSection } from "@js/mbdb/forms/sections/RecordInformation";
import mstRecord from "./data/mst.json";

const Section = RecordInformationSection.component;
const Fields = () => (
  <Section formConfig={{ overridableIdPrefix: "mbdb.playground" }} />
);

const values = (recordInformation, publication) => ({
  metadata: {
    general_parameters: { record_information: recordInformation },
    ...(publication ? { associated_publication: publication } : {}),
  },
});

const depositors = (value) => ({
  metadata: { general_parameters: { depositors: value } },
});

// The Record information section: the record's Title, the optional
// Associated publication, the Depositors (depositor, principal contact,
// contributors) and the Funding references.

const story = {
  title: "RecordInformation",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Fields },
    { name: "MST record", initialValues: mstRecord, render: Fields },
    {
      name: "Article",
      initialValues: values(
        { title: "MST measurement of hemoglobin serum elements" },
        {
          type: "Article",
          pid: "doi:10.1038/s41592-022-01476-y",
          title: "Hemoglobin serum elements measured by MST",
          journal: "Nature Methods",
        }
      ),
      render: Fields,
    },
    {
      name: "Thesis",
      initialValues: values(undefined, {
        type: "Thesis",
        pid: "urn:nbn:cz:ds-12345",
        title: "Microscale thermophoresis of blood proteins",
        degree_type: "PhD",
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: values(undefined, { type: "Article" }),
      initialErrors: {
        metadata: {
          general_parameters: {
            associated_publication: {
              pid: "Missing data for required field.",
              journal: "Missing data for required field.",
            },
          },
        },
      },
      render: Fields,
    },
    {
      name: "Depositors",
      initialValues: depositors({
        depositor: {
          given_name: "Max",
          family_name: "Mustermann",
          affiliations: [{ id: "02hpadn98" }],
        },
        principal_contact: {
          given_name: "Josiah",
          family_name: "Carberry",
          identifiers: ["orcid:0000-0002-1825-0097"],
          affiliations: [{ id: "05gq02987" }],
        },
        contributors: [
          { given_name: "Jane", family_name: "Doe" },
          { given_name: "John", family_name: "Doe" },
        ],
      }),
      render: Fields,
    },
    {
      name: "Funding references",
      initialValues: {
        metadata: {
          general_parameters: {
            funding_references: [
              {
                funder: { id: "05k73zm37" },
                award: { id: "05k73zm37::213912" },
              },
            ],
          },
        },
      },
      render: Fields,
    },
  ],
};

export default story;
