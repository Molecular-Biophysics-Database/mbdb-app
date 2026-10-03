// The names used more than once in the entity list, trimmed and
// case-sensitive. A hint only, never a client-side error (guide §8). Pure, so
// it is table-tested (design EntitiesOfInterest.md).
export const duplicateNames = (entities) => {
  const counts = new Map();
  for (const entity of entities ?? []) {
    const name = entity?.name?.trim();
    if (!name) continue;
    counts.set(name, (counts.get(name) ?? 0) + 1);
  }
  return new Set(
    [...counts].filter(([, count]) => count > 1).map(([name]) => name)
  );
};
