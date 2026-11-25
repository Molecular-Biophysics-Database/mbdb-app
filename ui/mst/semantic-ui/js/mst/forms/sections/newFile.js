import { RDMDepositFileApiClient } from "@js/invenio_rdm_records/src/deposit/api/DepositApiClient";
import { isComplete, toPayload } from "./fileMetadata";

// The details of the file to be uploaded next and the name of the file being
// uploaded with them. Outside of React: the API client reads it and it
// survives switching tabs.
export const newFile = { metadata: {}, name: undefined };

export const isUploading = (entries) =>
  ["pending", "uploading"].includes(entries?.[newFile.name]?.status);

export const isUploaded = (entries) =>
  entries?.[newFile.name]?.status === "finished";

// Sends the details together with the file; the server refuses a file
// without them.
export class MstFileApiClient extends RDMDepositFileApiClient {
  initializeFileUpload(url, filename, transferOptions = {}) {
    if (!isComplete(newFile.metadata))
      throw new Error("Fill in the required details of the file first.");
    const {
      fileSize = 0,
      type = this.defaultTransferType,
      ...opts
    } = transferOptions;
    newFile.name = filename.normalize();
    return this.axiosWithConfig.post(
      url,
      [
        {
          key: filename,
          size: fileSize,
          transfer: { type, ...opts },
          metadata: toPayload(newFile.metadata),
        },
      ],
      {}
    );
  }
}
