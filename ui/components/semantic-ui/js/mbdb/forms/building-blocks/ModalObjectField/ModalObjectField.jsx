import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import {
  Button,
  FieldHelp,
  Form,
  Icon,
  Label,
  Modal,
  Table,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "../fieldData";
import { SummaryItem } from "../SummaryItem";

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
  detail = null,
}) => {
  const { values, setFieldValue } = useFormikContext();
  // { isNew, snapshot } while the modal is open
  const [editing, setEditing] = useState(null);
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const text = data.label;

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

  const summaryCells = (v) => {
    const s = summary(v);
    return (Array.isArray(s) ? s : [s]).map((cell) => () => cell);
  };

  return (
    <Form.Field required={data.required}>
      {text && <label>{text}</label>}
      {data.helpText && <FieldHelp help={data.helpText} />}
      {!present ? (
        <>
          {required && (
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
              columns={summaryCells(value)}
              itemName={text}
              onEdit={openEdit}
              onRemove={
                required ? undefined : () => setFieldValue(fieldPath, undefined)
              }
              detail={detail}
            />
          </Table.Body>
        </Table>
      )}
      {editing !== null && (
        <Modal size="large" open onClose={cancel}>
          <Modal.Header>{`Edit ${text}`}</Modal.Header>
          <Modal.Content scrolling>{renderForm(fieldPath)}</Modal.Content>
          <Modal.Actions>
            <Button type="button" onClick={cancel}>
              Cancel
            </Button>
            <Button type="button" primary onClick={() => setEditing(null)}>
              Done
            </Button>
          </Modal.Actions>
        </Modal>
      )}
    </Form.Field>
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
  detail: PropTypes.node,
};
