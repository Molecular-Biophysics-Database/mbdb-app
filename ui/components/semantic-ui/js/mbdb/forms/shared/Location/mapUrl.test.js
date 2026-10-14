import { mapUrl } from "./mapUrl";

describe("mapUrl", () => {
  it("builds the OpenStreetMap marker URL at zoom 10", () => {
    expect(mapUrl(49.1951, 16.6068)).toBe(
      "https://www.openstreetmap.org/?mlat=49.1951&mlon=16.6068#map=10/49.1951/16.6068"
    );
  });
});
