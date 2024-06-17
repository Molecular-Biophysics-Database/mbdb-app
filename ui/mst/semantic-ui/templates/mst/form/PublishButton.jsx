import React from "react";
import { i18next } from "@translations/oarepo_ui/i18next";
import {
  useConfirmationModal,
  useDepositApiClient,
  ConfirmationModal,
} from "@js/oarepo_ui";
import PropTypes from "prop-types";
import { Button } from "semantic-ui-react";

export const PublishButton = React.memo(
  ({ modalMessage, modalHeader, additionalInputs }) => {
    const {
      isOpen: isModalOpen,
      close: closeModal,
      open: openModal,
    } = useConfirmationModal();
    const { isSubmitting, publish } = useDepositApiClient();

    return (
      <ConfirmationModal
        additionalInputs={additionalInputs}
        header={modalHeader}
        content={modalMessage}
        isOpen={isModalOpen}
        close={closeModal}
        trigger={
          <Button
          style={{ backgroundColor: "#023850", color: "white" }}
            onClick={openModal}
            content={i18next.t("Publish")}
            type="button"
            disabled={isSubmitting}
            loading={isSubmitting}
          >Deposit</Button>
        }
        actions={
          <>
            <div className="flex justify-between">
              <button
                onClick={closeModal}
                floated="left"
                className="flex justify-center w-[120px] py-3 text-20px bg-dark rounded-normal text-white hover:bg-secondary hover:text-dark transition-all"
              >
                {i18next.t("Cancel")}
              </button>
              <button
                  disabled={isSubmitting}
                  loading={isSubmitting}
                  className="flex justify-center w-[120px] py-3 text-20px rounded-normal bg-secondary text-dark hover:bg-dark hover:text-white transition-all"
                  onClick={() => {
                      publish();
                      closeModal();
                  }}
                  content={i18next.t("Publish")}
                  type="submit"
              >Deposit</button>
            </div>
          </>
        }
      />
    );
  }
);

PublishButton.propTypes = {
  modalMessage: PropTypes.string,
  modalHeader: PropTypes.string,
  additionalInputs: PropTypes.node,
};

PublishButton.defaultProps = {
  modalHeader: i18next.t("Are you sure you wish to publish this draft?"),
  modalMessage: i18next.t(
    "Once the record is published you will no longer be able to change record's files! However, you will still be able to update the record's metadata later."
  ),
};

export default PublishButton;