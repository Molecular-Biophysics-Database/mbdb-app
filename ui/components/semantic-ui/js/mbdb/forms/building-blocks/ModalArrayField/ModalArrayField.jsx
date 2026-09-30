import React, { useRef, useState } from "react";
import PropTypes from "prop-types";
import { FieldArray, getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import { applyEntityId } from "@js/mbdb/forms/building-blocks/DefaultsAndIds";
import { randomUUID } from "@js/mbdb/forms/building-blocks/randomUUID";
import {
  Button,
  Dropdown,
  FieldHelp,
  Form,
  HelpLabel,
  Icon,
  Label,
  Table,
} from "mbdb-semantic-ui-react";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { SummaryItem } from "@js/mbdb/forms/building-blocks/SummaryItem";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { EditModal } from "@js/mbdb/forms/building-blocks/EditModal";

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
  detailProps,
}) => {
  const { values, setFieldValue } = useFormikContext();
  // { index, isNew, snapshot } while the modal is open
  const [editing, setEditing] = useState(null);
  // the Edit/Add button that opened the modal — focus returns to it (F7)
  const triggerRef = useRef(null);
  // F3/C5: client-only keys for items without an id (components), parallel
  // to the items: grown on render, spliced on remove, pushed on add.
  // Entities keep their `id` as the key; components must NOT get an id.
  const keysRef = useRef([]);
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // F5/C1: error flag and list-level message read errors ∪ initialErrors
  const { hasError } = useFieldErrors(fieldPath);
  const listMessages = useOwnErrorMessages(fieldPath);

  const options = newItemOptions ?? [{ label: null, value: initialValue }];
  const items = getIn(values, fieldPath) ?? [];
  while (keysRef.current.length < items.length)
    keysRef.current.push(randomUUID());

  return (
    <FieldArray
      name={fieldPath}
      render={(arrayHelpers) => {
        const close = (button) => {
          setEditing(null);
          // focus back on the button that opened the modal
          if (button) setTimeout(() => button.focus(), 0);
        };
        // F1/C3: formik's remove leaves [] behind; never write []
        const removeAt = (index) => {
          keysRef.current.splice(index, 1);
          if (items.length <= 1) setFieldValue(fieldPath, undefined);
          else arrayHelpers.remove(index);
        };
        const openNew = (seed, e) => {
          triggerRef.current = e?.currentTarget ?? null;
          // F10: one helper decides how an entity gets its id
          const item = withIds
            ? applyEntityId(cloneDeep(seed))
            : cloneDeep(seed);
          arrayHelpers.push(item);
          keysRef.current.push(randomUUID());
          setEditing({ index: items.length, isNew: true, snapshot: null });
        };
        const openEdit = (index, e) => {
          triggerRef.current = e?.currentTarget ?? null;
          setEditing({
            index,
            isNew: false,
            snapshot: cloneDeep(getIn(values, `${fieldPath}.${index}`)),
          });
        };
        const cancel = () => {
          if (editing.isNew) removeAt(editing.index);
          else setFieldValue(`${fieldPath}.${editing.index}`, editing.snapshot);
          close(triggerRef.current);
        };
        const done = () => close(triggerRef.current);

        return (
          <>
            <Form.Field required={data.required} error={hasError}>
              {data.label && (
                // htmlFor points at the field path for OARepo error
                // scrolling; the list rows carry their own labels.
                <label htmlFor={fieldPath}>
                  <HelpLabel label={data.label} help={data.helpText} />
                </label>
              )}
              {data.helpText && <FieldHelp help={data.helpText} />}
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
                          key={value?.id ?? keysRef.current[index]}
                          fieldPath={itemPath}
                          columns={columns.map((c) => c.value)}
                          itemName={itemLabel(value)}
                          onEdit={(e) => openEdit(index, e)}
                          onRemove={
                            index < minItems ? undefined : () => removeAt(index)
                          }
                          detail={
                            detailGroups ? (
                              <DetailView
                                fieldPath={itemPath}
                                groups={detailGroups}
                                // id is an internal client uuid — never show it;
                                // detailProps (e.g. exclude) can override
                                exclude={["id"]}
                                {...detailProps}
                              />
                            ) : null
                          }
                        />
                      );
                    })}
                  </Table.Body>
                </Table>
              )}
              {listMessages.length > 0 && (
                <div>
                  <Label color="red" pointing prompt>
                    {listMessages.join(" ")}
                  </Label>
                </div>
              )}
              {options.length === 1 ? (
                <Button
                  type="button"
                  icon
                  labelPosition="left"
                  size="small"
                  onClick={(e) => openNew(options[0].value, e)}
                >
                  <Icon name="add" />
                  {`Add${options[0].label ? ` ${options[0].label}` : ""}`}
                </Button>
              ) : (
                // F2: menu items only fire onClick — Semantic's default
                // selectOnBlur/selectOnNavigation would ADD an item on blur
                // or arrow keys. "icon" + "small" match the one-option button.
                <Dropdown
                  text="Add"
                  button
                  labeled
                  floating
                  icon="add"
                  className="icon small"
                >
                  <Dropdown.Menu>
                    {options.map((option, i) => (
                      <Dropdown.Item
                        key={option.label ?? i}
                        text={option.label}
                        onClick={(e) => openNew(option.value, e)}
                      />
                    ))}
                  </Dropdown.Menu>
                </Dropdown>
              )}
            </Form.Field>
            {/* the modal is a SIBLING of Form.Field, not nested inside it
                (guide §8), so depth-2 modals stack correctly */}
            {editing !== null && (
              <EditModal
                size="large"
                open
                onCancel={cancel}
                onDone={done}
                header={`Edit ${itemLabel(
                  getIn(values, `${fieldPath}.${editing.index}`)
                )}`}
              >
                {renderForm(`${fieldPath}.${editing.index}`)}
              </EditModal>
            )}
          </>
        );
      }}
    />
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
  // F4: extra DetailView props (exclude, requiredPaths, vocabularyTitles).
  // `exclude` defaults to ["id"], the internal client uuid.
  detailProps: PropTypes.object,
};
