// Defaults and ids (design/building-blocks/DefaultsAndIds.md): defaults are
// written at the moment an item is created, and never afterwards. No effects
// that refill values (the old UseDefault / CreateUuid hooks did that).
import { randomUUID } from "./randomUUID";

// Single source of truth for "give this object a client id" — used by
// newEntitySeed, ensureEntityIds and ModalArrayField's withIds (via .id).
export const applyEntityId = (item) => ({ ...item, id: randomUUID() });

// Seed for a new entity: entities require an `id`, components get none
// (callers that seed a component pass withIds=false, not this helper).
export const newEntitySeed = (type) =>
  applyEntityId(type !== undefined ? { type } : {});

// One-time pass on form load: assign ids to existing entities that have none.
// Returns the input unchanged (undefined stays undefined, never []) when it
// is not an array, and the SAME array reference when nothing changed, so a
// caller can write back only when `result !== input` and not mark the form
// dirty (guide §7: never write []).
export const ensureEntityIds = (entities) => {
  if (!Array.isArray(entities)) return entities;
  let changed = false;
  const withIds = entities.map((entity) => {
    if (entity != null && typeof entity === "object" && !entity.id) {
      changed = true;
      return applyEntityId(entity);
    }
    return entity;
  });
  return changed ? withIds : entities;
};
