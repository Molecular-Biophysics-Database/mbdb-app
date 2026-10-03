import React, { useEffect, useRef } from "react";
import PropTypes from "prop-types";
import { Button, Form, Modal } from "mbdb-semantic-ui-react";

// The shared edit-modal shell used by ModalArrayField and ModalObjectField
// (design: Semantic Modal, scrolling content, Cancel/Done).
// closeOnDimmerClick={false}: one accidental click must not discard edits;
// Escape still reaches onClose, which IS Cancel.
//
// Focus return lives here so both modal blocks get it for free: the element
// that had focus when the modal opened is captured (Modal onMount, a read of
// document.activeElement — no querying) and focused back on unmount. The
// modal keeps itself mounted briefly for the dimmer transition, so the
// cleanup runs after close; that delay is accepted.
export const EditModal = ({
  header,
  open,
  onCancel,
  onDone,
  children,
  size = "large",
  scrollToError = false,
}) => {
  // the element with focus before the modal opened; focused back on close
  const triggerRef = useRef(null);
  // the modal's own content, used to scope the error scroll to this modal
  const contentRef = useRef(null);

  useEffect(
    () => () => {
      // unmount cleanup: focus returns to the element that opened the modal
      triggerRef.current?.focus?.();
    },
    []
  );

  // Opened from an error badge: scroll the first errored field into view.
  // DOM access is scoped to the modal's own contentRef (lead decision, guide
  // §8): no document.querySelector, no jQuery — a scoped querySelector on our
  // own element plus the native scrollIntoView (React 16.14 suffices).
  useEffect(() => {
    if (!open || !scrollToError) return;
    const el = contentRef.current?.querySelector(".field.error, .error.field");
    el?.scrollIntoView({ block: "center" });
  }, [open, scrollToError]);

  return (
    <Modal
      size={size}
      open={open}
      onClose={onCancel}
      closeOnDimmerClick={false}
      onMount={() => {
        triggerRef.current = document.activeElement;
      }}
    >
      <Modal.Header>{header}</Modal.Header>
      <Modal.Content scrolling>
        {/* A Semantic Modal is a portal on document.body, so nothing inside
            it has a `.ui.form` ancestor — and every Semantic form rule needs
            one: field/label spacing, Form.Group columns, required asterisks,
            textareas. `as="div"` gives the `ui form` class without a second
            <form> (Enter must not submit, and a submit cannot reach the
            portal from the deposit form). */}
        <Form as="div">
          <div ref={contentRef}>{children}</div>
        </Form>
      </Modal.Content>
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
};

EditModal.propTypes = {
  header: PropTypes.node.isRequired,
  open: PropTypes.bool.isRequired,
  onCancel: PropTypes.func.isRequired,
  onDone: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
  size: PropTypes.oneOf(["small", "large", "fullscreen"]),
  scrollToError: PropTypes.bool,
};
