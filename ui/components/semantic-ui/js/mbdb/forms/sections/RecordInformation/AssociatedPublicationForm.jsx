import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Form } from "mbdb-semantic-ui-react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";

// The Publication type enum (model Publication_base.type). In its own module
// so tests can compare it against the model without pulling the form.
export const PUBLICATION_TYPES = ["Article", "Book", "Thesis"];

// The Thesis degree type enum (model Thesis.degree_type).
export const DEGREE_TYPES = ["PhD", "Habilitation", "Master", "Bachelor"];

// The help texts from the model (Publication_base, Article, Book, Thesis);
// passed explicitly because the ui_model does not carry the polymorphic
// children yet. The labels come from the leaf-name fallback and match the
// model ("Pid", "Title", "Journal", "Publisher", "Degree type").
const PID_HELP =
  "Persistent identifier associated with the publication (e.g. DOI, ISBN, URN)";
const TITLE_HELP = "The title of the publication";
const TYPE_HELP = "The type of the publication";

// The content of the associated publication modal (design mirrors the former
// RDM 12 form): the Type dropdown first, then the base fields (Pid, Title)
// and the type-specific field — journal for an Article, publisher for a Book,
// degree type for a Thesis — in one row. A type change keeps the base fields
// and drops the type-specific one.
export const AssociatedPublicationForm = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const type = getIn(values, `${fieldPath}.type`);
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="type"
        options={PUBLICATION_TYPES}
        variant="dropdown"
        keep={["pid", "title"]}
        help={TYPE_HELP}
        required
      />
      <Form.Group widths="equal">
        <TextField fieldPath={`${fieldPath}.pid`} help={PID_HELP} required />
        <TextField fieldPath={`${fieldPath}.title`} help={TITLE_HELP} />
        {type === "Article" && (
          <TextField
            fieldPath={`${fieldPath}.journal`}
            help="The full name of the journal the article appears in"
            required
          />
        )}
        {type === "Book" && (
          <TextField
            fieldPath={`${fieldPath}.publisher`}
            help="The full name of the publisher of the book"
            required
          />
        )}
        {type === "Thesis" && (
          <SelectField
            fieldPath={`${fieldPath}.degree_type`}
            options={DEGREE_TYPES}
            help="The type of degree (equivalent) the thesis was submitted to attain"
            required
          />
        )}
      </Form.Group>
    </>
  );
};

AssociatedPublicationForm.propTypes = {
  // the publication OBJECT path
  fieldPath: PropTypes.string.isRequired,
};
