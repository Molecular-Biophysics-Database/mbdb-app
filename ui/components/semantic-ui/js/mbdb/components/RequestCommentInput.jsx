import React, { useState } from "react";
import PropTypes from "prop-types";
import { Icon } from "semantic-ui-react";
import { RichEditor } from "react-invenio-forms";
import sanitizeHtml from "sanitize-html";
import { useQuery } from "@tanstack/react-query";
import { httpApplicationJson } from "@js/oarepo_ui";
import { i18next } from "@translations/oarepo_requests_ui/i18next";

const DEFAULT_MAX_COMMENT_LENGTH = 10000;
const OAREPO_MAX_COMMENT_LENGTH = 1000;

// Upstream forms compare the reported length with their hard-coded 1,000
// limit. Keep the visible/editor limit at 10,000 and map only the value passed
// back to the parent form so submit is disabled after the MBDB limit.
const lengthForOarepoForm = (length) =>
  Math.max(0, length - (DEFAULT_MAX_COMMENT_LENGTH - OAREPO_MAX_COMMENT_LENGTH));

export const RequestCommentInput = ({
  comment,
  handleChange,
  initialValue,
  setLength,
}) => {
  const [actualLength, setActualLength] = useState(0);

  const { data } = useQuery(
    ["allowedHtmlTagsAttrs"],
    () => httpApplicationJson.get("/requests/configs/publish_draft"),
    {
      refetchOnWindowFocus: false,
      staleTime: Infinity,
    }
  );

  const updateLength = (length) => {
    setActualLength(length);
    setLength(lengthForOarepoForm(length));
  };

  return (
    <React.Fragment>
      <RichEditor
        initialValue={initialValue}
        inputValue={comment}
        editorConfig={{
          auto_focus: true,
          min_height: 100,
          width: "100%",
          entity_encoding: "raw",
          toolbar:
            "blocks | bold italic | bullist numlist | outdent indent | undo redo",
          setup: (editor) => {
            editor.on("BeforeAddUndo", (event) => {
              if (
                editor.getContent({ format: "text" }).length >=
                DEFAULT_MAX_COMMENT_LENGTH
              ) {
                event.preventDefault();
              }
            });
            editor.on("init", () => {
              updateLength(editor.getContent({ format: "text" }).length);
            });
          },
        }}
        onEditorChange={(event, editor) => {
          const cleanedContent = sanitizeHtml(editor.getContent(), {
            allowedTags: data?.data?.allowedHtmlTags,
            allowedAttributes: data?.data?.allowedHtmlAttrs,
          });
          const textContent = editor.getContent({ format: "text" });
          const length =
            textContent.trim().length === 0 && textContent.length <= 1
              ? 0
              : textContent.length;

          handleChange(event, cleanedContent);
          updateLength(length);
        }}
        onFocus={(event, editor) => {
          editor.selection.select(editor.getBody(), true);
          editor.selection.collapse(false);
        }}
      />
      {actualLength <= DEFAULT_MAX_COMMENT_LENGTH ? (
        <small>{`${i18next.t("Remaining characters: ")}${
          DEFAULT_MAX_COMMENT_LENGTH - actualLength
        }`}</small>
      ) : (
        <small>
          <Icon name="warning circle" color="red" />
          {i18next.t("commentTooLong", {
            count: actualLength - DEFAULT_MAX_COMMENT_LENGTH,
          })}
        </small>
      )}
    </React.Fragment>
  );
};

RequestCommentInput.propTypes = {
  comment: PropTypes.string,
  handleChange: PropTypes.func.isRequired,
  initialValue: PropTypes.string,
  setLength: PropTypes.func.isRequired,
};

RequestCommentInput.defaultProps = {
  comment: "",
  initialValue: "",
};
