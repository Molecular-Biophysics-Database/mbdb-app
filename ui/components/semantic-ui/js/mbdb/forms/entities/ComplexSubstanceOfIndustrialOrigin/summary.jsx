import { vocabularyPart } from "@js/mbdb/forms/entities/summary";

// Text of the entity table's "Details" column: the product title from the
// shared vocabulary cache, "" when there is no product (SummaryItem shows
// "—"). vocabularyPart is a component — never a hook here.
export const summaryIndustrialOrigin = (value) =>
  vocabularyPart("products", value?.product);
