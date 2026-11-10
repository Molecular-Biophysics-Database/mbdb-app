import { randomUUID } from "./randomUUID";

describe("randomUUID", () => {
  const original = window.crypto;

  afterEach(() => {
    Object.defineProperty(window, "crypto", {
      value: original,
      configurable: true,
      writable: true,
    });
  });

  it("returns window.crypto.randomUUID() when available", () => {
    Object.defineProperty(window, "crypto", {
      value: { randomUUID: () => "12345678-1234-1234-1234-123456789012" },
      configurable: true,
      writable: true,
    });
    expect(randomUUID()).toBe("12345678-1234-1234-1234-123456789012");
  });

  it("throws a friendly error when crypto.randomUUID is missing", () => {
    Object.defineProperty(window, "crypto", {
      value: undefined,
      configurable: true,
      writable: true,
    });
    expect(() => randomUUID()).toThrow(
      "crypto.randomUUID() is not available (needs https or localhost)"
    );
  });
});
