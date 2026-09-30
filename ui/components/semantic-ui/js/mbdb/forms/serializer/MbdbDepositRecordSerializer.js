import {
  EmptyDepositRecordSerializer,
  OARepoDepositSerializer,
} from "@js/oarepo_ui/api";

// Used only for its cleanup helpers (drops "__key", null, "", [] and {}).
const cleaner = new OARepoDepositSerializer([], ["__key"]);

/**
 * EmptyDepositRecordSerializer sends metadata as-is, including empty values.
 * The model has `minItems: 1` on many optional arrays, so empty values must be
 * removed before sending, otherwise the server rejects the draft.
 */
export class MbdbDepositRecordSerializer extends EmptyDepositRecordSerializer {
  serialize(record) {
    const serialized = super.serialize(record);
    if (serialized.metadata) {
      serialized.metadata = cleaner.serialize(serialized.metadata);
    }
    return serialized;
  }
}
