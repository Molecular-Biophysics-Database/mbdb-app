import React, { useContext, useEffect, useRef } from "react";
import PropTypes from "prop-types";
import { Button, Form, Modal } from "mbdb-semantic-ui-react";

// The parent levels a nested modal shows as a breadcrumb, and the short noun of
// the level just above it (for the nested Done button). Each level provides
// [...trail, crumb] to its children (design ModalArrayField.md, "where am I in
// stacked modals"). The trail is text, never a link: clicking a parent crumb
// would have to guess whether it means Cancel or Done.
export const EditModalTrail = React.createContext([]);

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
  crumb,
  open,
  onCancel,
  onDone,
  children,
  size,
  scrollToError = false,
}) => {
  // the element with focus before the modal opened; focused back on close
  const triggerRef = useRef(null);
  // the modal's own content, used to scope the error scroll to this modal
  const contentRef = useRef(null);
  // the parent levels (empty at depth 1): one breadcrumb line + a return target
  const trail = useContext(EditModalTrail);
  // a nested modal is one size smaller, so the parent stays visible as a frame
  // (design cue 3); `size` is an explicit override.
  const modalSize = size ?? (trail.length > 0 ? undefined : "large");
  const parentNoun =
    trail.length > 0 ? trail[trail.length - 1]?.noun : undefined;

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
    <EditModalTrail.Provider value={crumb ? [...trail, crumb] : trail}>
      <Modal
        size={modalSize}
        open={open}
        onClose={onCancel}
        closeOnDimmerClick={false}
        onMount={() => {
          triggerRef.current = document.activeElement;
        }}
      >
        <Modal.Header>
          {trail.length > 0 && (
            // the parents, small and muted, above the title (cue 1)
            <div className="mbdb-modal-trail">
              {trail
                .map((parent) => parent?.label)
                .filter(Boolean)
                .join(" › ")}
              {" ›"}
            </div>
          )}
          {header}
        </Modal.Header>
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
            {/* cue 2 (B2): name the destination at depth 2, plain "Done" at
                depth 1 (there is nothing to return to) */}
            {parentNoun ? `Done, back to ${parentNoun}` : "Done"}
          </Button>
        </Modal.Actions>
      </Modal>
    </EditModalTrail.Provider>
  );
};

EditModal.propTypes = {
  header: PropTypes.node.isRequired,
  // this modal's own level: `{ label, noun }`, provided to a nested modal's
  // breadcrumb and return button. Omit at depth 1 (nothing nests above it).
  crumb: PropTypes.shape({
    label: PropTypes.node,
    noun: PropTypes.string,
  }),
  open: PropTypes.bool.isRequired,
  onCancel: PropTypes.func.isRequired,
  onDone: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
  size: PropTypes.oneOf(["small", "large", "fullscreen"]),
  scrollToError: PropTypes.bool,
};
