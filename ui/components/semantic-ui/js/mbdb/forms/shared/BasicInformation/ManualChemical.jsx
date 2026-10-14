import React, { useState } from "react";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { Button, Confirm, Form, Header } from "mbdb-semantic-ui-react";
import { StringArrayField } from "mbdb-react-invenio-forms";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";

// Hand entry for a chemical PubChem does not have. Stored without an id,
// which is also what keeps the manual form mounted (isManualChemical).
// "Search PubChem instead" throws the manual data away after a Confirm and
// the picker renders again by itself; clearing the last manual field has
// the same effect (the pruning setter removes the emptied object).
export const ManualChemical = ({ fieldPath }) => {
  const { setFieldValue } = useFormikContext();
  const [confirming, setConfirming] = useState(false);
  const data = useModelFieldData(fieldPath, {});
  // String/{message} errors at the object itself ("Missing data…"); the
  // child fields show their own errors.
  const objectMessages = useOwnErrorMessages(fieldPath);
  // Server title errors land on `title` (the i18n dict), while the input
  // sits at `title.en`; pass them down explicitly, merged so they survive
  // the errors-reset like every other message.
  const titleMessages = useFieldErrors(`${fieldPath}.title`).messages;

  return (
    <>
      <Header as="h5" id={fieldPath}>
        {data.label} · Manual entry
        {data.required && <span className="mbdb-required">*</span>}
      </Header>
      <ErrorMessages messages={objectMessages} />
      <Form.Group widths="equal">
        <TextField
          fieldPath={`${fieldPath}.title.en`}
          width={8}
          // the vocabulary key `title` is an i18ndict; its `en` leaf has no
          // model label, so without the override the input shows "En".
          // Required: the backend errors at `….title` when it is missing.
          label="Name"
          required
          error={titleMessages.length > 0 ? titleMessages.join(" ") : undefined}
        />
        <TextField fieldPath={`${fieldPath}.chemical_formula`} width={8} />
      </Form.Group>
      <Form.Group widths="equal">
        <MolecularWeight
          fieldPath={`${fieldPath}.molecular_weight`}
          defaultUnit="g/mol"
        />
        <StringArrayField
          fieldPath={`${fieldPath}.additional_identifiers`}
          addButtonLabel="Add identifier"
        />
      </Form.Group>
      <Button
        type="button"
        basic
        size="small"
        content="Search PubChem instead"
        onClick={() => setConfirming(true)}
      />
      <Confirm
        open={confirming}
        header="Search PubChem instead?"
        content="The manually entered chemical data will be removed."
        confirmButton="Remove and search"
        onCancel={() => setConfirming(false)}
        onConfirm={() => {
          setConfirming(false);
          setFieldValue(fieldPath, undefined);
        }}
      />
    </>
  );
};

ManualChemical.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
