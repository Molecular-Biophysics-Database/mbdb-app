import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import cloneDeep from "lodash/cloneDeep";
import { applyEntityId } from "@js/mbdb/forms/building-blocks/DefaultsAndIds";
import {
  Button,
  Dropdown,
  FieldHelp,
  Form,
  HelpLabel,
  Icon,
  Table,
} from "mbdb-semantic-ui-react";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useArrayRows } from "@js/mbdb/forms/building-blocks/useArrayRows";
import { SummaryItem } from "@js/mbdb/forms/building-blocks/SummaryItem";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import {
  EditModal,
  useEditSession,
} from "@js/mbdb/forms/building-blocks/EditModal";

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
  const { values } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // error flag and list-level message read errors ∪ initialErrors
  const { hasError } = useFieldErrors(fieldPath);
  const listMessages = useOwnErrorMessages(fieldPath);
  // items/keys/remove/push/replace live in the shared array-rows hook
  const { items, keyFor, remove, push, replace } = useArrayRows(fieldPath);
  // the modal edit session is shared with ModalObjectField (open/snapshot/
  // cancel/done); this block keys it by item index and carries its
  // scrollToError flag through the open
  const {
    session,
    openNew: openNewSession,
    openExisting,
    cancel,
    done,
  } = useEditSession({
    read: (index) => getIn(values, `${fieldPath}.${index}`),
    restore: replace,
    remove,
  });

  const options = newItemOptions ?? [{ label: null, value: initialValue }];

  const openNew = (seed) => {
    // applyEntityId is the one place that decides how an entity gets its id
    const item = withIds ? applyEntityId(cloneDeep(seed)) : cloneDeep(seed);
    push(item);
    openNewSession(items.length);
  };
  const openEdit = (index, scrollToError = false) =>
    openExisting(index, { scrollToError });

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
                  <Table.HeaderCell key={column.label}>
                    {column.label}
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
                    key={keyFor(value, index)}
                    fieldPath={itemPath}
                    cells={columns.map((c) => c.value)}
                    itemName={itemLabel(value)}
                    onEdit={(scrollToError) => openEdit(index, scrollToError)}
                    onRemove={
                      index < minItems ? undefined : () => remove(index)
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
        <ErrorMessages messages={listMessages} />
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
          // menu items only fire onClick — Semantic's default
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
                  onClick={() => openNew(option.value)}
                />
              ))}
            </Dropdown.Menu>
          </Dropdown>
        )}
      </Form.Field>
      {/* the modal is a SIBLING of Form.Field, not nested inside it
          (guide §8), so depth-2 modals stack correctly */}
      {session !== null && (
        <EditModal
          size="large"
          open
          onCancel={cancel}
          onDone={done}
          scrollToError={session.scrollToError}
          header={`Edit ${itemLabel(
            getIn(values, `${fieldPath}.${session.key}`)
          )}`}
        >
          {renderForm(`${fieldPath}.${session.key}`)}
        </EditModal>
      )}
    </>
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
      label: PropTypes.string.isRequired,
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
  // extra DetailView props (exclude, requiredPaths).
  // `exclude` defaults to ["id"], the internal client uuid.
  detailProps: PropTypes.object,
};
