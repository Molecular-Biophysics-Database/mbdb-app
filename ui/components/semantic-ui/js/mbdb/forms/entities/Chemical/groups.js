// The group spec of the Chemical entity. The entity form and, through
// shared/Components, a chemical component's details both read it, so the two
// cannot drift apart (guide §8). `basic_information` is a
// vocabulary reference: the `{ field, vocabulary }` entry is what lets the
// details view resolve its title from the shared cache.
export const CHEMICAL_GROUPS = [
  {
    title: "Chemical",
    fields: [
      { field: "basic_information", vocabulary: "chemicals" },
      "additional_specifications",
    ],
  },
];
