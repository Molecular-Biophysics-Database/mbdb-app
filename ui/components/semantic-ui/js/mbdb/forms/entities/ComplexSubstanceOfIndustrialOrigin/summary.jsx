import React from "react";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";

// Text of the entity table's "Details" column: the product title from the
// shared vocabulary cache, "" when there is no product (SummaryItem shows
// "—"). VocabularyValue is a component — never a hook here (plan step 4).
export const summaryIndustrialOrigin = (value) =>
  value?.product?.id ? (
    <VocabularyValue vocabulary="products" value={value.product} />
  ) : (
    ""
  );
