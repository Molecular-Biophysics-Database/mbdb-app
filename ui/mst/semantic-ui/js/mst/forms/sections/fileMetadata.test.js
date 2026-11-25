import { fileUiModel, isComplete, toFormikErrors, toPayload } from "./fileMetadata";

it("needs every required field", () => {
  const metadata = {
    creation_date: "2026-01-01",
    originates_from: "User",
    context: "Raw measurement data",
    content_type: "Text",
    processing_steps: [{ name: "export", description: "to xlsx" }],
  };
  expect(isComplete(metadata)).toBe(true);
  expect(isComplete({ ...metadata, context: undefined })).toBe(false);
  expect(isComplete({ ...metadata, processing_steps: undefined })).toBe(true);
  expect(isComplete({ ...metadata, processing_steps: [{}] })).toBe(false);
  expect(isComplete(undefined)).toBe(false);
});

it("leaves out an empty list of steps", () => {
  expect(toPayload({ context: "a", processing_steps: [] })).toEqual({
    context: "a",
  });
  const steps = [{ name: "a", description: "b" }];
  expect(toPayload({ processing_steps: steps })).toEqual({
    processing_steps: steps,
  });
});

it("nests server errors", () => {
  expect(
    toFormikErrors([
      { field: "metadata.processing_steps.0.name", messages: ["a", "b"] },
    ])
  ).toEqual({ metadata: { processing_steps: [{ name: "a b" }] } });
  expect(toFormikErrors(undefined)).toEqual({});
});

it("takes processing step labels from data analysis", () => {
  const steps = { label: "Data processing", child: { children: { name: {} } } };
  const model = fileUiModel({
    children: {
      metadata: {
        children: {
          method_specific_parameters: {
            children: {
              data_analysis: { child: { children: { data_processing: steps } } },
            },
          },
        },
      },
    },
  });
  expect(model.children.metadata.children.processing_steps).toMatchObject({
    label: "Processing steps",
    child: steps.child,
  });
});
