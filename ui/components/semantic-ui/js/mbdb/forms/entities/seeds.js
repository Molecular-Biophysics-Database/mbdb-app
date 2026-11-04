// The extra keys an entity of each type needs beyond `type`, written on create
// (Add entity) and on a Type change, so the server never rejects a freshly
// created entity (design/entities/index.md, "Creating an entity and type
// changes"). Defined once, so "Add entity" and the Type discriminator cannot
// drift apart. Only the chemical origin needs one: its single required `class`
// value is not offered as a choice.
export const ENTITY_SEEDS = {
  "Complex substance of chemical origin": { class: "Lipid assembly" },
};
