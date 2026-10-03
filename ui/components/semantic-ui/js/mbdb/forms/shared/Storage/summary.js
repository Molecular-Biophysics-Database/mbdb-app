import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";

// The summary row of one storage object: "-80 °C for 3 months,
// 1 preparation step". An empty storage shows "" (SummaryItem shows "—").
export const summaryStorage = (value) => {
  if (!value) return "";
  const main = [
    valueUnitText(value.temperature),
    valueUnitText(value.duration) && `for ${valueUnitText(value.duration)}`,
  ]
    .filter((t) => t !== "")
    .join(" ");
  const steps = (value.storage_preparation ?? []).length;
  const stepsText =
    steps === 0
      ? ""
      : steps === 1
      ? "1 preparation step"
      : `${steps} preparation steps`;
  return [main, stepsText].filter((t) => t !== "").join(", ");
};
