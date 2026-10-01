import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Location } from "./Location";
import { mapUrl } from "./mapUrl";

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

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return (
    <span data-testid="probe">
      {v === undefined ? "null" : JSON.stringify(v)}
    </span>
  );
};
Probe.propTypes = { path: PropTypes.string.isRequired };

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

const location = () => (
  <>
    <Location fieldPath={PATH} />
    <Probe path={PATH} />
  </>
);

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);

// the three number inputs render in field order: latitude, longitude, altitude
const inputs = () => [...container.querySelectorAll('input[type="number"]')];

const type = async (el, value) => {
  el.value = value;
  await act(async () => {
    Simulate.change(el);
  });
};

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
    await type(inputs()[0], "49.1951");
    expect(probe()).toEqual({ latitude: 49.1951 });
  });

  it("clearing all three leaves the location key absent, never {}", async () => {
    render(location(), {
      initialValues: {
        [PATH]: { latitude: 49.1951, longitude: 16.6068, altitude: 237 },
      },
    });
    await type(inputs()[0], "");
    await type(inputs()[1], "");
    await type(inputs()[2], "");
    expect(probe()).toBeNull();
  });

  it("shows the map link only once latitude and longitude are numbers", async () => {
    render(location(), {
      initialValues: { [PATH]: { latitude: 49.1951, altitude: 237 } },
    });
    expect(mapLink()).toBeUndefined();

    await type(inputs()[1], "16.6068");
    const link = mapLink();
    expect(link).toBeDefined();
    expect(link.getAttribute("href")).toBe(mapUrl(49.1951, 16.6068));
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
    await type(inputs()[2], "237");
    expect(container.textContent).toContain(
      "Must be greater than or equal to -90 and less than or equal to 90."
    );
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelectorAll(".field.error").length).toBeGreaterThan(
      0
    );
  });
});
