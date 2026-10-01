import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import axios from "axios";
import { rememberTitle, useVocabularyTitle } from "./vocabularyTitles";

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
      "/api/vocabularies/organisms/taxid%3A1"
    );
    expect(container.textContent).toContain("Bacillus subtilis");

    // a later mount for the same id reads the cache, no new fetch; unmount
    // first so the hook re-runs instead of a same-props update
    ReactDOM.unmountComponentAtNode(container);
    await render(<TitleProbe type="organisms" id="taxid:1" />);
    expect(axios.get).toHaveBeenCalledTimes(1);
    expect(shown()).toBe("Bacillus subtilis");
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
