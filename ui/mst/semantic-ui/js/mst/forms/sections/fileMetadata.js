import get from "lodash/get";
import set from "lodash/set";
import { DATA_ANALYSIS_PATH } from "./constants";

const REQUIRED = ["creation_date", "originates_from", "context", "content_type"];

export const isComplete = (metadata) =>
  REQUIRED.every((f) => metadata?.[f]) &&
  (metadata.processing_steps ?? []).every(
    (step) => step?.name?.trim() && step?.description?.trim()
  );

// what is sent to the server: it rejects an empty list of steps
export const toPayload = ({ processing_steps: steps, ...metadata }) =>
  steps?.length > 0 ? { ...metadata, processing_steps: steps } : metadata;

// marshmallow's [{ field, messages }] as a Formik errors object
export const toFormikErrors = (errors) =>
  (errors ?? []).reduce(
    (acc, { field, messages }) => set(acc, field, messages.join(" ")),
    {}
  );

const field = (label, help, required = false) => ({ label, help, required });

// File metadata is not part of the record, so the record's ui_model has no
// labels for it. Processing steps are the same type as in data analysis.
export const fileUiModel = (recordUiModel) => ({
  children: {
    metadata: {
      children: {
        creation_date: field(
          "Creation date",
          "The date when the file was created (e.g. the measurement date)",
          true
        ),
        originates_from: field(
          "Originates from",
          "What is the source of the file",
          true
        ),
        context: field(
          "Context",
          "The context the file should be understood within (e.g. raw measurement data)",
          true
        ),
        content_type: field(
          "Content type",
          "Type of the file content in terms of how it can be read (text, binary, etc.)",
          true
        ),
        description: field(
          "Description",
          "Short description of what the file contains"
        ),
        recommended_software: field(
          "Recommended software",
          "The name of the software recommended for opening and working with the file"
        ),
        processing_steps: {
          // spread first: this list has its own label, help and required
          ...get(
            recordUiModel,
            `children.${DATA_ANALYSIS_PATH.replace(/\./g, ".children.")}.child.children.data_processing`
          ),
          ...field(
            "Processing steps",
            "List of the processing steps performed on the file before it was deposited (e.g. exported to xlsx)"
          ),
        },
      },
    },
  },
});
