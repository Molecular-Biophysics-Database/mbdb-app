import cloneDeep from "lodash/cloneDeep";
import get from "lodash/get";
import set from "lodash/set";
import {
  EmptyDepositRecordSerializer,
  OARepoDepositSerializer,
} from "@js/oarepo_ui/api";
import { ensureEntityIds } from "@js/mbdb/forms/building-blocks/DefaultsAndIds";
import { ENTITIES_OF_INTEREST_PATH } from "@js/mbdb/forms/sections/EntitiesOfInterest/path";

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

  /**
   * The load path, before Formik sees the record. Old records may have
   * entities without an `id` (`id` is not required by the model but the server
   * rejects an entity without one), so give each one an id here — the one
   * place with no value-writing effect (design EntitiesOfInterest.md,
   * "Legacy entities without id"). Returns the record unchanged (same
   * reference) when nothing needs an id.
   */
  deserialize(record) {
    const deserialized = super.deserialize(record);
    const entities = get(deserialized, ENTITIES_OF_INTEREST_PATH);
    const ensured = ensureEntityIds(entities);
    if (ensured === entities) return deserialized;
    // copy the path so the input record is not mutated
    const next = cloneDeep(deserialized);
    set(next, ENTITIES_OF_INTEREST_PATH, ensured);
    return next;
  }
}
