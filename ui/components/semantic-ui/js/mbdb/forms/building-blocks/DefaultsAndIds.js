// Defaults and ids (design/building-blocks/DefaultsAndIds.md): defaults are
// written at the moment an item is created, and never afterwards. No effects
// that refill values (the old UseDefault / CreateUuid hooks did that).
import { randomUUID } from "./randomUUID";

// Seed for a new entity: entities require an `id`, components get none.
export const newEntitySeed = (type) => ({
  id: randomUUID(),
  ...(type !== undefined ? { type } : {}),
});

// One-time pass on form load: assign ids to existing entities that have none.
export const ensureEntityIds = (entities) =>
  (entities || []).map((entity) =>
    entity != null && typeof entity === "object" && !entity.id
      ? { ...entity, id: randomUUID() }
      : entity
  );
