import React, { useState } from "react";
import PropTypes from "prop-types";
import { FieldArray, getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import { randomUUID } from "../randomUUID";
import {
  Button,
  Dropdown,
  FieldHelp,
  Form,
  Icon,
  Modal,
  Table,
} from "mbdb-semantic-ui-react";
import { countErrors } from "../errors";
import { useModelFieldData } from "../fieldData";
import { SummaryItem } from "../SummaryItem";
import { DetailView } from "../DetailView";

// Summary table of complex objects; editing happens in a modal bound directly
// to the real Formik path (design/building-blocks/ModalArrayField.md).
export const ModalArrayField = ({
  fieldPath,
  label,
  help,
  required,
  minItems = 0,
  itemLabel,
  columns,
  newItemOptions,
  initialValue = {},
  withIds = false,
  renderForm,
  detailGroups,
}) => {
  const { values, errors, setFieldValue } = useFormikContext();
  // { index, isNew, snapshot } while the modal is open
  const [editing, setEditing] = useState(null);
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });

  const options = newItemOptions ?? [{ label: null, value: initialValue }];
  const items = getIn(values, fieldPath) ?? [];

  return (
    <Form.Field
      required={data.required}
      error={countErrors(errors, fieldPath) > 0}
    >
      {data.label && <label>{data.label}</label>}
      {data.helpText && <FieldHelp help={data.helpText} />}
      <FieldArray
        name={fieldPath}
        render={(arrayHelpers) => {
          const openNew = (seed) => {
            const item = { ...cloneDeep(seed) };
            if (withIds) item.id = randomUUID();
            arrayHelpers.push(item);
            setEditing({ index: items.length, isNew: true, snapshot: null });
          };
          const openEdit = (index) =>
            setEditing({
              index,
              isNew: false,
              snapshot: cloneDeep(getIn(values, `${fieldPath}.${index}`)),
            });
          const cancel = () => {
            if (editing.isNew) arrayHelpers.remove(editing.index);
            else
              setFieldValue(`${fieldPath}.${editing.index}`, editing.snapshot);
            setEditing(null);
          };

          return (
            <>
              {items.length === 0 ? (
                <p className="ui grey text">No items yet</p>
              ) : (
                <Table compact>
                  <Table.Header>
                    <Table.Row>
                      <Table.HeaderCell />
                      {columns.map((column) => (
                        <Table.HeaderCell key={column.title}>
                          {column.title}
                        </Table.HeaderCell>
                      ))}
                      <Table.HeaderCell />
                    </Table.Row>
                  </Table.Header>
                  <Table.Body>
                    {items.map((value, index) => {
                      const itemPath = `${fieldPath}.${index}`;
                      return (
                        <SummaryItem
                          key={value?.id ?? index}
                          fieldPath={itemPath}
                          columns={columns.map((c) => c.value)}
                          itemName={itemLabel(value)}
                          onEdit={() => openEdit(index)}
                          onRemove={
                            index < minItems
                              ? undefined
                              : () => arrayHelpers.remove(index)
                          }
                          detail={
                            detailGroups ? (
                              <DetailView
                                fieldPath={itemPath}
                                groups={detailGroups}
                              />
                            ) : null
                          }
                        />
                      );
                    })}
                  </Table.Body>
                </Table>
              )}
              {options.length === 1 ? (
                <Button
                  type="button"
                  icon
                  labelPosition="left"
                  size="small"
                  onClick={() => openNew(options[0].value)}
                >
                  <Icon name="add" />
                  {`Add${options[0].label ? ` ${options[0].label}` : ""}`}
                </Button>
              ) : (
                // "icon" makes Semantic style it as a labeled icon button,
                // "small" matches the single-type Add button.
                <Dropdown
                  text="Add"
                  button
                  labeled
                  floating
                  icon="add"
                  className="icon small"
                  options={options.map((option, i) => ({
                    key: i,
                    text: option.label,
                    value: i,
                  }))}
                  value={null}
                  onChange={(e, { value: i }) => openNew(options[i].value)}
                />
              )}
              {editing !== null && (
                <Modal size="large" open onClose={cancel}>
                  <Modal.Header>
                    {`Edit ${itemLabel(
                      getIn(values, `${fieldPath}.${editing.index}`)
                    )}`}
                  </Modal.Header>
                  <Modal.Content scrolling>
                    {renderForm(`${fieldPath}.${editing.index}`)}
                  </Modal.Content>
                  <Modal.Actions>
                    <Button type="button" onClick={cancel}>
                      Cancel
                    </Button>
                    <Button
                      type="button"
                      primary
                      onClick={() => setEditing(null)}
                    >
                      Done
                    </Button>
                  </Modal.Actions>
                </Modal>
              )}
            </>
          );
        }}
      />
    </Form.Field>
  );
};

ModalArrayField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.string,
  help: PropTypes.string,
  required: PropTypes.bool,
  minItems: PropTypes.number,
  itemLabel: PropTypes.func.isRequired,
  columns: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      value: PropTypes.func.isRequired,
    })
  ).isRequired,
  newItemOptions: PropTypes.arrayOf(
    PropTypes.shape({ label: PropTypes.string, value: PropTypes.object })
  ),
  initialValue: PropTypes.object,
  withIds: PropTypes.bool,
  renderForm: PropTypes.func.isRequired,
  detailGroups: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      fields: PropTypes.arrayOf(PropTypes.string).isRequired,
    })
  ),
};
