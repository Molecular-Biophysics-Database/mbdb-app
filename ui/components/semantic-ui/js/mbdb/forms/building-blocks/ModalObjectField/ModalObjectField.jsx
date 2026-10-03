import React from "react";
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
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { SummaryItem } from "@js/mbdb/forms/building-blocks/SummaryItem";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import {
  EditModal,
  useEditSession,
} from "@js/mbdb/forms/building-blocks/EditModal";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";

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
  const unset = useUnsetField();
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

  // the modal edit session is shared with ModalArrayField; this block keys
  // it by fieldPath and removes/restores the whole object
  const {
    session,
    openNew: openNewSession,
    openExisting,
    cancel,
    done: closeSession,
  } = useEditSession({
    read: (path) => getIn(values, path),
    restore: (path, snapshot) => setFieldValue(path, snapshot),
    remove: unset,
  });

  const openNew = () => {
    setFieldValue(fieldPath, cloneDeep(initialValue));
    openNewSession(fieldPath);
  };
  const openEdit = () => openExisting(fieldPath);
  // Done-if-empty behaves as absent: a Done on an object that still holds no
  // data is treated like Cancel (lead decision) so no `{}` is left behind.
  const done = () => {
    if (!hasData(getIn(values, fieldPath))) unset(fieldPath);
    closeSession();
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
        <ErrorMessages messages={objectMessages} />
      </Form.Field>
      {/* the modal is a SIBLING of Form.Field, not nested inside it, so
          depth-2 modals stack correctly (same as ModalArrayField) */}
      {session !== null && (
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
      fields: PropTypes.arrayOf(
        PropTypes.oneOfType([
          PropTypes.string,
          PropTypes.shape({
            field: PropTypes.string.isRequired,
            vocabulary: PropTypes.string,
          }),
        ])
      ).isRequired,
    })
  ),
  // extra DetailView props (exclude, requiredPaths);
  // `exclude` defaults to ["id"], the internal client uuid.
  detailProps: PropTypes.object,
};
