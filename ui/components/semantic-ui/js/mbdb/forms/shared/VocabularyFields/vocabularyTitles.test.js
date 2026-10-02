import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import axios from "axios";
import {
  rememberItem,
  rememberTitle,
  useVocabularyItem,
  useVocabularyTitle,
} from "./vocabularyTitles";

// The vocabulary GET goes through plain axios with Invenio's Accept header
// (mocked: no network in tests).
jest.mock("axios", () => ({ get: jest.fn() }));

// Renders the hook for (type, id) and exposes the current title.
const TitleProbe = ({ type, id }) => (
  <span data-testid="title">{useVocabularyTitle(type, id) ?? "…"}</span>
);
TitleProbe.propTypes = { type: PropTypes.string, id: PropTypes.string };

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  container = null;
});

const render = async (ui) => {
  await act(async () => {
    ReactDOM.render(ui, container);
  });
};

const shown = () =>
  container.querySelector('[data-testid="title"]').textContent;

describe("vocabularyTitles", () => {
  it("fetches the title of an unknown id once and caches it", async () => {
    axios.get.mockResolvedValue({
      data: { id: "taxid:1", title_l10n: "Bacillus subtilis" },
    });
    // two hooked components for the same id share one request
    await render(
      <>
        <TitleProbe type="organisms" id="taxid:1" />
        <TitleProbe type="organisms" id="taxid:1" />
      </>
    );
    expect(axios.get).toHaveBeenCalledTimes(1);
    expect(axios.get).toHaveBeenCalledWith(
      "/api/vocabularies/organisms/taxid%3A1",
      { headers: { Accept: "application/vnd.inveniordm.v1+json" } }
    );
    expect(container.textContent).toContain("Bacillus subtilis");

    // a later mount for the same id reads the cache, no new fetch; unmount
    // first so the hook re-runs instead of a same-props update
    ReactDOM.unmountComponentAtNode(container);
    await render(<TitleProbe type="organisms" id="taxid:1" />);
    expect(axios.get).toHaveBeenCalledTimes(1);
    expect(shown()).toBe("Bacillus subtilis");
  });

  it("fetches again for a different id", async () => {
    axios.get.mockResolvedValue({
      data: { id: "taxid:a", title_l10n: "Organism A" },
    });
    await render(<TitleProbe type="organisms" id="taxid:a" />);
    expect(axios.get).toHaveBeenCalledTimes(1);

    axios.get.mockResolvedValue({
      data: { id: "taxid:b", title_l10n: "Organism B" },
    });
    ReactDOM.unmountComponentAtNode(container);
    await render(<TitleProbe type="organisms" id="taxid:b" />);
    expect(axios.get).toHaveBeenCalledTimes(2);
    expect(shown()).toBe("Organism B");
  });

  it("never shows a stale title when the id changes before the fetch lands", async () => {
    let resolveB;
    axios.get.mockImplementation(
      () =>
        new Promise((resolve) => {
          resolveB = resolve;
        })
    );
    rememberTitle("organisms", "taxid:old", "Old organism");
    await render(<TitleProbe type="organisms" id="taxid:old" />);
    expect(shown()).toBe("Old organism");

    // id changes to one the cache does not know: while its fetch is in
    // flight the hook must show nothing, never the previous id's title
    await render(<TitleProbe type="organisms" id="taxid:new" />);
    expect(shown()).toBe("…");

    // even a failed fetch must not bring the old title back
    await act(async () => {
      resolveB({ data: null });
    });
    expect(shown()).toBe("…");
  });

  it("accepts a title object (title.en) when title_l10n is absent", async () => {
    axios.get.mockResolvedValue({
      data: { id: "bf:2", title: { en: "Serum" } },
    });
    await render(<TitleProbe type="body-fluids" id="bf:2" />);
    expect(shown()).toBe("Serum");
  });

  it("rememberTitle skips the fetch entirely", async () => {
    rememberTitle("organisms", "taxid:remembered", "Remembered title");
    await render(<TitleProbe type="organisms" id="taxid:remembered" />);
    expect(axios.get).not.toHaveBeenCalled();
    expect(shown()).toBe("Remembered title");
  });

  it("a failed lookup leaves the title unknown and does not cache the failure", async () => {
    axios.get.mockRejectedValue(new Error("404"));
    await render(<TitleProbe type="organisms" id="taxid:missing" />);
    expect(shown()).toBe("…");
    expect(axios.get).toHaveBeenCalledTimes(1);

    // a later mount retries (rejections are not cached); unmount first so
    // the effect actually runs again instead of a same-props update
    axios.get.mockResolvedValue({
      data: { id: "taxid:missing", title_l10n: "Now known" },
    });
    ReactDOM.unmountComponentAtNode(container);
    await render(<TitleProbe type="organisms" id="taxid:missing" />);
    expect(axios.get).toHaveBeenCalledTimes(2);
    expect(shown()).toBe("Now known");
  });
});

describe("vocabularyTitles items (customFields)", () => {
  // Renders useVocabularyItem and exposes title/customFields as JSON.
  const ItemProbe = ({ type, id }) => {
    const item = useVocabularyItem(type, id);
    return (
      <pre data-testid="item">
        {JSON.stringify({
          title: item.title ?? null,
          customFields: item.customFields ?? null,
        })}
      </pre>
    );
  };
  ItemProbe.propTypes = { type: PropTypes.string, id: PropTypes.string };

  const itemShown = () =>
    JSON.parse(container.querySelector('[data-testid="item"]').textContent);

  it("caches customFields from the GET together with the title", async () => {
    axios.get.mockResolvedValue({
      data: {
        id: "inchikey:WATER",
        title_l10n: "Water",
        custom_fields: { chemical_formula: "H2O" },
      },
    });
    await render(<ItemProbe type="chemicals" id="inchikey:WATER" />);
    expect(itemShown()).toEqual({
      title: "Water",
      customFields: { chemical_formula: "H2O" },
    });

    // cached: a later mount serves customFields without a new GET
    ReactDOM.unmountComponentAtNode(container);
    await render(<ItemProbe type="chemicals" id="inchikey:WATER" />);
    expect(axios.get).toHaveBeenCalledTimes(1);
    expect(itemShown()).toEqual({
      title: "Water",
      customFields: { chemical_formula: "H2O" },
    });
  });

  it("caches customFields remembered with the item", async () => {
    rememberItem("chemicals", "inchikey:KH2PO4", {
      title: "Potassium dihydrogen phosphate",
      customFields: { chemical_formula: "KH2PO4" },
    });
    await render(<ItemProbe type="chemicals" id="inchikey:KH2PO4" />);
    expect(axios.get).not.toHaveBeenCalled();
    expect(itemShown()).toEqual({
      title: "Potassium dihydrogen phosphate",
      customFields: { chemical_formula: "KH2PO4" },
    });
  });

  it("rememberTitle merges: it does not clobber remembered customFields", async () => {
    rememberItem("chemicals", "inchikey:MERGE", {
      customFields: { chemical_formula: "NaCl" },
    });
    rememberTitle("chemicals", "inchikey:MERGE", "Sodium chloride");
    await render(<ItemProbe type="chemicals" id="inchikey:MERGE" />);
    expect(itemShown()).toEqual({
      title: "Sodium chloride",
      customFields: { chemical_formula: "NaCl" },
    });
  });

  it("an item GET without custom_fields leaves customFields undefined", async () => {
    axios.get.mockResolvedValue({
      data: { id: "taxid:no-cf", title_l10n: "No facts" },
    });
    await render(<ItemProbe type="organisms" id="taxid:no-cf" />);
    expect(itemShown()).toEqual({ title: "No facts", customFields: null });
  });
});
