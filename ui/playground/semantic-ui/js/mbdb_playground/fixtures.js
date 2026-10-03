// Story-only fixtures for the entity paths that recur across the stories
// (duplications.md §9). Not shipped: the playground never loads these in the
// built bundle. Keeping the one-entity shape here means a story cannot forget
// the entity `type` (VocabularyFields / ExternalDatabases review findings)
// and the long metadata.general_parameters.entities_of_interest.0 path stops
// being hand-typed per story.

export const ENTITY_PATH = "metadata.general_parameters.entities_of_interest.0";
export const entityPath = (field) => `${ENTITY_PATH}.${field}`;

// initialValues with one entity of the given type (required: every entity has
// a type). `fields` are the entity's own keys; `extra` carries polymorphic
// variant keys (e.g. { derived_from: "Body fluid" }) that must sort with
// `type`, before the field values.
export const entityValues = (type, fields = {}, extra = {}) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [{ type, ...extra, ...fields }],
    },
  },
});

// initialErrors at one entity field.
export const entityErrors = (field, message) => ({
  metadata: {
    general_parameters: { entities_of_interest: [{ [field]: message }] },
  },
});
