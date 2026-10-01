import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import {
  Button,
  FieldHelp,
  Form,
  HelpLabel,
  Icon,
  Label,
  Table,
} from "mbdb-semantic-ui-react";
import {
  hasData,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { SummaryItem } from "@js/mbdb/forms/building-blocks/SummaryItem";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { EditModal } from "@js/mbdb/forms/building-blocks/EditModal";

// One optional object too big for inline display (design/building-blocks/
// ModalObjectField.md). Same Cancel/Done semantics as ModalArrayField.
export const ModalObjectField = ({
  fieldPath,
  label,
  help,
  required,
  summary,
  initialValue = {},
  renderForm,
  detailGroups = null,
  detailProps,
}) => {
  const { values, setFieldValue } = useFormikContext();
  // { isNew, snapshot } while the modal is open
  const [editing, setEditing] = useState(null);
  // label/help/required come from the model, with explicit props as override
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const text = data.label;
  // object-level messages only (strings sitting exactly at fieldPath)
  const objectMessages = useOwnErrorMessages(fieldPath);

  const value = getIn(values, fieldPath);
  const present = value !== undefined;

  const openNew = () => {
    setFieldValue(fieldPath, cloneDeep(initialValue));
    setEditing({ isNew: true, snapshot: null });
  };
  const openEdit = () =>
    setEditing({ isNew: false, snapshot: cloneDeep(value) });
  const cancel = () => {
    setFieldValue(fieldPath, editing.isNew ? undefined : editing.snapshot);
    setEditing(null);
  };
  // Done-if-empty behaves as absent: a Done on an object that still holds no
  // data is treated like Cancel (lead decision) so no `{}` is left behind.
  const done = () => {
    if (!hasData(getIn(values, fieldPath))) setFieldValue(fieldPath, undefined);
    setEditing(null);
  };

  // A single-cell summary passes the one column directly; a multi-cell maps
  // each precomputed cell into the cell function SummaryItem expects.
  const summaryColumns = (v) => {
    const s = summary(v);
    return Array.isArray(s) ? s.map((cell) => () => cell) : [() => s];
  };

  return (
    <>
      <Form.Field required={data.required} error={objectMessages.length > 0}>
        {text && (
          <label htmlFor={fieldPath}>
            <HelpLabel label={text} help={data.helpText} />
          </label>
        )}
        {data.helpText && <FieldHelp help={data.helpText} />}
        {!present ? (
          <>
            {data.required && (
              <div>
                <Label color="red" size="small">
                  Not filled in
                </Label>
              </div>
            )}
            <Button
              type="button"
              icon
              labelPosition="left"
              size="small"
              onClick={openNew}
            >
              <Icon name="add" />
              {`Add ${text}`}
            </Button>
          </>
        ) : (
          <Table compact>
            <Table.Body>
              <SummaryItem
                fieldPath={fieldPath}
                cells={summaryColumns(value)}
                itemName={text}
                onEdit={openEdit}
                onRemove={
                  data.required
                    ? undefined
                    : () => setFieldValue(fieldPath, undefined)
                }
                detail={
                  detailGroups ? (
                    <DetailView
                      fieldPath={fieldPath}
                      groups={detailGroups}
                      exclude={["id"]}
                      {...detailProps}
                      onEdit={openEdit}
                      itemName={text}
                    />
                  ) : null
                }
              />
            </Table.Body>
          </Table>
        )}
        {objectMessages.length > 0 && (
          <div>
            <Label color="red" pointing prompt>
              {objectMessages.join(" ")}
            </Label>
          </div>
        )}
      </Form.Field>
      {/* the modal is a SIBLING of Form.Field, not nested inside it, so
          depth-2 modals stack correctly (same as ModalArrayField) */}
      {editing !== null && (
        <EditModal
          size="large"
          open
          onCancel={cancel}
          onDone={done}
          header={`Edit ${text}`}
        >
          {renderForm(fieldPath)}
        </EditModal>
      )}
    </>
  );
};

ModalObjectField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  required: PropTypes.bool,
  summary: PropTypes.func.isRequired,
  initialValue: PropTypes.object,
  renderForm: PropTypes.func.isRequired,
  // aligned with ModalArrayField — groups + extra DetailView props build
  // the SummaryItem detail internally (was a ready-made `detail` node).
  detailGroups: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      fields: PropTypes.arrayOf(PropTypes.string).isRequired,
    })
  ),
  // extra DetailView props (exclude, requiredPaths, vocabularyTitles);
  // `exclude` defaults to ["id"], the internal client uuid.
  detailProps: PropTypes.object,
};
