import React from "react";
import PropTypes from "prop-types";
import { Button, Modal } from "mbdb-semantic-ui-react";

// The shared edit-modal shell used by ModalArrayField and ModalObjectField
// (design: Semantic Modal, large, scrolling content, Cancel/Done).
// closeOnDimmerClick={false}: one accidental click must not discard edits
// (F7); Escape still reaches onClose, which IS Cancel.
export const EditModal = ({
  header,
  open,
  onCancel,
  onDone,
  children,
  size = "large",
}) => (
  <Modal size={size} open={open} onClose={onCancel} closeOnDimmerClick={false}>
    <Modal.Header>{header}</Modal.Header>
    <Modal.Content scrolling>{children}</Modal.Content>
    <Modal.Actions>
      <Button type="button" onClick={onCancel}>
        Cancel
      </Button>
      <Button type="button" primary onClick={onDone}>
        Done
      </Button>
    </Modal.Actions>
  </Modal>
);

EditModal.propTypes = {
  header: PropTypes.node.isRequired,
  open: PropTypes.bool.isRequired,
  onCancel: PropTypes.func.isRequired,
  onDone: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
  size: PropTypes.string,
};
