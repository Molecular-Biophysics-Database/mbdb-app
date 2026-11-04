import fs from "fs";
import path from "path";
import { REGISTRY } from "./registry";

// The registry must never disagree with reality (design Playground.md): an
// entry with `load` is shown as built, so its story file must exist. This
// guards the regression where an entry was left without a story (it then shows
// as "Not built yet" in the playground even though the block is built).
describe("playground registry", () => {
  it("has step, key and design on every entry", () => {
    for (const entry of REGISTRY) {
      expect(["string", "number"]).toContain(typeof entry.step);
      expect(typeof entry.key).toBe("string");
      expect(typeof entry.design).toBe("string");
    }
  });

  it("keys are unique", () => {
    const keys = REGISTRY.map((e) => e.key);
    expect(new Set(keys).size).toBe(keys.length);
  });

  it("every entry with load() has a <key>.story.jsx on disk", () => {
    for (const entry of REGISTRY) {
      if (!entry.load) continue;
      const file = path.join(__dirname, "stories", `${entry.key}.story.jsx`);
      expect(fs.existsSync(file)).toBe(true);
    }
  });
});
