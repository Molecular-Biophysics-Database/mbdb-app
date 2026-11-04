import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  typeInto,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Location } from "./Location";
import { mapUrl } from "./mapUrl";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const PATH = "location";

const UI_MODEL = {
  [PATH]: {
    label: "Location",
    helpText:
      "The coordinates, in decimal notation, where the sample was collected",
    required: true,
  },
  [`${PATH}.latitude`]: { label: "Latitude", required: true },
  [`${PATH}.longitude`]: { label: "Longitude", required: true },
  [`${PATH}.altitude`]: { label: "Altitude", required: true },
};

let container;

beforeEach(() => {
  setFakeUiModel(UI_MODEL);
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

const renderWithUnrelated = (ui, opts = {}) =>
  render(ui, { ...opts, withUnrelatedField: true });

const location = () => (
  <>
    <Location fieldPath={PATH} />
    <ValueProbe path={PATH} />
  </>
);

const probe = () => readProbe(container);

// the three number inputs render in field order: latitude, longitude, altitude
const inputs = () => [...container.querySelectorAll('input[type="number"]')];

const mapLink = () =>
  [...container.querySelectorAll("a")].find((a) =>
    a.textContent.includes("Show on map")
  );

describe("Location", () => {
  it("renders the group title and the three inputs on one row", () => {
    render(location());
    expect(container.querySelector("h5.ui.header").textContent).toContain(
      "Location"
    );
    const row = container.querySelector(".fields.equal.width");
    expect(row.querySelectorAll('input[type="number"]').length).toBe(3);
    // step="any": decimal degrees are not rounded
    inputs().forEach((input) => expect(input.getAttribute("step")).toBe("any"));
  });

  it("typing 49.1951 stores a number", async () => {
    render(location());
    await typeInto(inputs()[0], "49.1951");
    expect(probe()).toEqual({ latitude: 49.1951 });
  });

  it("clearing all three prunes location but keeps the entity sibling (real array path)", async () => {
    // the real path sits under entities_of_interest.<i>: pruning must stop
    // at the array item, not touch its siblings
    const arrayPath = "entities.0.location";
    render(
      <>
        <Location fieldPath={arrayPath} />
        <ValueProbe path="entities.0" />
      </>,
      {
        initialValues: {
          entities: [
            {
              type: "Complex substance of environmental origin",
              location: {
                latitude: 49.1951,
                longitude: 16.6068,
                altitude: 237,
              },
            },
          ],
        },
      }
    );
    await typeInto(inputs()[0], "");
    await typeInto(inputs()[1], "");
    await typeInto(inputs()[2], "");
    expect(probe()).toEqual({
      type: "Complex substance of environmental origin",
    });
  });

  it("shows the map link only once latitude and longitude are numbers", async () => {
    render(location(), {
      initialValues: { [PATH]: { latitude: 49.1951, altitude: 237 } },
    });
    expect(mapLink()).toBeUndefined();

    await typeInto(inputs()[1], "16.6068");
    const link = mapLink();
    expect(link).toBeDefined();
    expect(link.getAttribute("href")).toBe(mapUrl(49.1951, 16.6068));
  });

  it("the object-level error shows under the group header and survives an unrelated edit", async () => {
    renderWithUnrelated(location(), {
      initialErrors: { [PATH]: "Missing data for required field." },
    });
    expect(container.querySelector("h5.ui.header.red")).not.toBeNull();
    expect(container.textContent).toContain("Missing data for required field.");
    await editUnrelatedField(container);
    expect(container.textContent).toContain("Missing data for required field.");
  });

  it("shows per-field errors under their inputs; untouched ones stay after editing another field", async () => {
    render(location(), {
      initialValues: { [PATH]: { latitude: 95 } },
      initialErrors: {
        [PATH]: {
          latitude:
            "Must be greater than or equal to -90 and less than or equal to 90.",
          longitude: "Missing data for required field.",
          altitude: "Missing data for required field.",
        },
      },
    });
    expect(container.textContent).toContain(
      "Must be greater than or equal to -90 and less than or equal to 90."
    );

    // editing altitude clears the formik `errors` state and updates its own
    // value; the untouched latitude message must stay, and so must the
    // (identically worded) longitude message
    await typeInto(inputs()[2], "237");
    expect(container.textContent).toContain(
      "Must be greater than or equal to -90 and less than or equal to 90."
    );
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelectorAll(".field.error").length).toBeGreaterThan(
      0
    );
  });
});
