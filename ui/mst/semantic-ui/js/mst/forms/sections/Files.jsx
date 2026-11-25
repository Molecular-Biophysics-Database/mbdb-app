import React, { useEffect, useRef, useState } from "react";
import PropTypes from "prop-types";
import { Formik, useFormikContext } from "formik";
import { useSelector } from "react-redux";
import { useQuery } from "@tanstack/react-query";
import {
  FormConfigProvider,
  computeFilesSectionCompletion,
  useFormConfig,
} from "@js/oarepo_ui/forms";
import { httpApplicationJson } from "@js/oarepo_ui/util";
import { UppyUploader } from "@js/invenio_rdm_records";
import { humanReadableBytes } from "react-invenio-forms";
import {
  Button,
  Dimmer,
  Grid,
  Header,
  Label,
  Loader,
  Message,
  Segment,
  useReviewMode,
} from "mbdb-semantic-ui-react";
import {
  DetailView,
  FieldRow,
  ModalArrayField,
  SelectField,
  TextField,
} from "@js/mbdb/forms";
import {
  FILE_CONTENT_TYPES,
  FILE_CONTEXTS,
  FILE_ORIGINS,
} from "./constants";
import {
  PROCESSING_COLUMNS,
  PROCESSING_GROUPS,
  ProcessingStepForm,
} from "./DataAnalysis";
import {
  fileUiModel,
  isComplete,
  toFormikErrors,
  toPayload,
} from "./fileMetadata";
import { isUploaded, isUploading, newFile } from "./newFile";

const FILE_GROUPS = [
  {
    title: "File",
    fields: [
      "creation_date",
      "originates_from",
      "context",
      "content_type",
      "description",
      "recommended_software",
    ],
  },
  {
    title: "Processing",
    fields: [
      {
        field: "processing_steps",
        itemColumns: PROCESSING_COLUMNS,
        itemGroups: PROCESSING_GROUPS,
      },
    ],
  },
];

const FileMetadataForm = () => (
  <>
    <FieldRow widths="equal">
      <TextField fieldPath="metadata.creation_date" type="date" />
      <SelectField
        fieldPath="metadata.originates_from"
        options={FILE_ORIGINS}
      />
    </FieldRow>
    <FieldRow widths="equal">
      <SelectField fieldPath="metadata.context" options={FILE_CONTEXTS} />
      <SelectField
        fieldPath="metadata.content_type"
        options={FILE_CONTENT_TYPES}
      />
    </FieldRow>
    <FieldRow widths="equal">
      <TextField fieldPath="metadata.description" />
      <TextField fieldPath="metadata.recommended_software" />
    </FieldRow>
    <ModalArrayField
      fieldPath="metadata.processing_steps"
      itemLabel={(v) => v?.name || "New processing step"}
      newItemOptions={[{ label: "processing step", value: {} }]}
      columns={PROCESSING_COLUMNS}
      detailGroups={PROCESSING_GROUPS}
      detailProps={{ exclude: ["name", "description"] }}
      crumbNoun="processing step"
      renderForm={(itemPath) => <ProcessingStepForm fieldPath={itemPath} />}
    />
  </>
);

// The latest metadata of each file by file_id. Cards unmount with the tab, so
// unfinished input and what was already saved have to outlive them.
const edited = new Map();

const SAVE_DELAY = 800;

// Files have their own endpoint, so a card saves itself instead of being saved
// with the record: a moment after the last change, or when it unmounts.
const FileAutoSave = ({ file }) => {
  const { values, setErrors } = useFormikContext();
  const [status, setStatus] = useState(null);
  const mounted = useRef(true);
  const saveRef = useRef();
  const metadata = values.metadata ?? {};
  const payload = JSON.stringify(toPayload(metadata));
  const entry = edited.get(file.file_id);
  const unsaved = payload !== entry.saved;
  const complete = isComplete(metadata);

  useEffect(() => {
    entry.metadata = metadata;
  });

  saveRef.current = () => {
    // compared with the last request, which may still be on its way
    if (!complete || payload === (entry.requested ?? entry.saved)) return;
    entry.requested = payload;
    if (mounted.current) setStatus("saving");
    // one request at a time, so an older one can not overwrite a newer one
    entry.queue = entry.queue.then(async () => {
      try {
        await httpApplicationJson.put(file.links.self, {
          metadata: JSON.parse(payload),
        });
        entry.saved = payload;
        if (mounted.current && entry.requested === payload) setStatus("saved");
      } catch (error) {
        // a later change or Try again may send the same values again
        if (entry.requested === payload) entry.requested = undefined;
        if (!mounted.current) return;
        setErrors(toFormikErrors(error.response?.data?.errors));
        setStatus("failed");
      }
    });
  };

  useEffect(() => {
    const timer = setTimeout(() => saveRef.current(), SAVE_DELAY);
    return () => clearTimeout(timer);
  }, [payload]);

  useEffect(() => {
    // a request of the previous mount may still be on its way
    entry.queue.then(() => {
      if (!mounted.current) return;
      setStatus((previous) => previous ?? "saved");
      saveRef.current();
    });
    return () => {
      mounted.current = false;
      saveRef.current();
    };
  }, []);

  if (!complete)
    return (
      <Label basic color="red">
        Fill in the required details to save them
      </Label>
    );
  if (status === "failed" && unsaved)
    return (
      <Message negative visible>
        The file details could not be saved.{" "}
        <Button type="button" size="small" onClick={() => saveRef.current()}>
          Try again
        </Button>
      </Message>
    );
  return (
    <span className="mbdb-muted-text" aria-live="polite">
      {unsaved ? "Saving…" : "Saved"}
    </span>
  );
};
FileAutoSave.propTypes = { file: PropTypes.object.isRequired };

const FileCard = ({ file, readOnly }) => {
  if (!edited.has(file.file_id)) {
    const metadata = file.metadata ?? {};
    edited.set(file.file_id, {
      metadata,
      saved: JSON.stringify(toPayload(metadata)),
      queue: Promise.resolve(),
    });
  }
  const { metadata } = edited.get(file.file_id);
  const [initialValues] = useState({ metadata });
  return (
    <Segment>
      <Header as="h3">{file.key}</Header>
      <Formik initialValues={initialValues} onSubmit={() => {}}>
        {readOnly ? (
          <>
            {!isComplete(metadata) && (
              <Label basic color="red">
                Required details missing
              </Label>
            )}
            <DetailView
              fieldPath="metadata"
              groups={FILE_GROUPS}
              exclude={["width", "height"]}
            />
          </>
        ) : (
          <>
            <FileMetadataForm />
            <FileAutoSave file={file} />
          </>
        )}
      </Formik>
    </Segment>
  );
};
FileCard.propTypes = {
  file: PropTypes.object.isRequired,
  readOnly: PropTypes.bool.isRequired,
};

const FileCards = ({ locked }) => {
  const review = useReviewMode();
  const filesUrl = useSelector((state) => state.deposit.record?.links?.files);
  // names repeat when a file is deleted and uploaded again, file ids do not
  const uploaded = useSelector((state) =>
    Object.values(state.files.entries ?? {})
      .filter((f) => f.status === "finished")
      .map((f) => `${f.name}\n${f.checksum}`)
      .sort()
      .join("\n\n")
  );
  // refetched when a file is uploaded, deleted or imported
  const { data, isError, refetch } = useQuery(
    ["file-metadata", filesUrl, uploaded],
    async () => (await httpApplicationJson.get(filesUrl)).data.entries ?? [],
    {
      enabled: Boolean(filesUrl && uploaded),
      keepPreviousData: true,
      refetchOnWindowFocus: false,
    }
  );

  if (!uploaded) return review ? <p>No files uploaded</p> : null;
  if (isError)
    return (
      <Message negative visible>
        The file details could not be loaded.{" "}
        <Button type="button" size="small" onClick={() => refetch()}>
          Try again
        </Button>
      </Message>
    );

  const names = new Set(uploaded.split("\n\n").map((f) => f.split("\n")[0]));
  return (data ?? [])
    .filter((f) => f.file_id && names.has(f.key.normalize()))
    .map((file) => (
      <FileCard
        // the mode is in the key: it switches between two different contents
        key={`${file.file_id}-${review}`}
        file={file}
        readOnly={review || locked}
      />
    ));
};
FileCards.propTypes = { locked: PropTypes.bool.isRequired };

const NewFileSync = ({ onChange }) => {
  const { values } = useFormikContext();
  useEffect(() => {
    newFile.metadata = values.metadata ?? {};
    onChange(isComplete(newFile.metadata));
  }, [values, onChange]);
  return null;
};
NewFileSync.propTypes = { onChange: PropTypes.func.isRequired };

// One file at a time: its details first, they unlock the uploader for a single
// file and are sent together with it.
const NewFile = ({ record }) => {
  const formConfig = useFormConfig();
  const { config, permissions, filesLocked, fileModification } = formConfig;
  const { values } = useFormikContext();
  const entries = useSelector((state) => state.files.entries);
  const [complete, setComplete] = useState(() => isComplete(newFile.metadata));
  const [formKey, setFormKey] = useState(0);
  const uploading = isUploading(entries);
  const uploaded = isUploaded(entries);
  const locked = Boolean(record?.is_published && filesLocked);
  const count = Object.keys(entries ?? {}).length;
  const open = complete || uploading;

  useEffect(() => {
    if (!uploaded) return;
    newFile.metadata = {};
    newFile.name = undefined;
    setComplete(false);
    setFormKey((key) => key + 1);
  }, [uploaded]);

  return (
    <>
      {values.files?.enabled && !locked && (
        <Dimmer.Dimmable as={Segment} dimmed={uploading}>
          <Dimmer active={uploading} inverted>
            <Loader>Uploading the file</Loader>
          </Dimmer>
          <Header as="h3">Add a raw measurement file</Header>
          <p>
            Fill in the required details, then choose the file below. Files are
            added one at a time.
          </p>
          <Formik
            key={formKey}
            initialValues={{ metadata: newFile.metadata }}
            onSubmit={() => {}}
          >
            <FileDetailsProvider>
              <FileMetadataForm />
              <NewFileSync onChange={setComplete} />
            </FileDetailsProvider>
          </Formik>
          {!open && (
            <Label basic color="red">
              Fill in the required details to choose a file
            </Label>
          )}
        </Dimmer.Dimmable>
      )}
      <UppyUploader
        // remounted when it locks, so a file chosen earlier is not uploaded
        // with incomplete details
        key={open ? "open" : "locked"}
        isDraftRecord={!record?.is_published}
        config={config}
        quota={{
          ...config.quota,
          // the uploader is disabled when the limit is reached
          maxFiles:
            complete && !uploading
              ? Math.min(config.quota.maxFiles, count + 1)
              : count,
        }}
        decimalSizeDisplay={config.decimal_size_display}
        allowEmptyFiles={config.allowEmptyFiles}
        showMetadataOnlyToggle={permissions?.can_manage_files}
        filesLocked={filesLocked}
        fileModification={fileModification}
        fileManagerSelectionType="files"
      />
    </>
  );
};
NewFile.propTypes = { record: PropTypes.object };

// Replaces the uploader's own counter, which would show the one-file limit.
export const FilesQuota = ({ filesList, filesSize, filesEnabled }) => {
  const { config } = useFormConfig();
  if (!filesEnabled) return null;
  const size = (bytes) => humanReadableBytes(bytes, config.decimal_size_display);
  return (
    <Grid.Column mobile={16} tablet={12} computer={12} className="storage-col">
      <Header size="tiny" className="mr-10">
        Storage available
      </Header>
      <Label>{`${filesList.length} out of ${config.quota.maxFiles} files`}</Label>
      <Label>{`${size(filesSize)} out of ${size(config.quota.maxStorage)}`}</Label>
    </Grid.Column>
  );
};
FilesQuota.propTypes = {
  filesList: PropTypes.array.isRequired,
  filesSize: PropTypes.number.isRequired,
  filesEnabled: PropTypes.bool.isRequired,
};

const FileDetailsProvider = ({ children }) => {
  const formConfig = useFormConfig();
  const { config } = formConfig;
  return (
    <FormConfigProvider
      value={{
        ...formConfig,
        config: { ...config, ui_model: fileUiModel(config.ui_model) },
      }}
    >
      {children}
    </FormConfigProvider>
  );
};
FileDetailsProvider.propTypes = { children: PropTypes.node };

const FilesSectionComponent = ({ record }) => {
  const review = useReviewMode();
  const { filesLocked, config } = useFormConfig();
  return (
    <>
      <p>
        Information about the file(s) containing the raw data. Maximum number of
        uploaded files is {config.quota?.maxFiles}.
      </p>
      {!review && <NewFile record={record} />}
      <FileDetailsProvider>
        <FileCards locked={Boolean(record?.is_published && filesLocked)} />
      </FileDetailsProvider>
    </>
  );
};
FilesSectionComponent.propTypes = { record: PropTypes.object };

export const FilesSection = {
  key: "files",
  label: "Raw measurement files",
  component: FilesSectionComponent,
  includesPaths: ["files.enabled"],
  // a metadata-only record needs no files
  sectionCompletion: ({ formikValues, reduxState }) =>
    formikValues.files?.enabled === false
      ? 1
      : computeFilesSectionCompletion({ reduxState }),
};
