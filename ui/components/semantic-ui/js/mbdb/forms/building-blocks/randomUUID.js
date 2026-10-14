// crypto.randomUUID() exists on https/localhost, which covers every mbdb
// environment (design/DefaultsAndIds). Tests must provide it; jsdom only
// has it in secure contexts.
export const randomUUID = () => {
  if (!window.crypto?.randomUUID) {
    throw new Error(
      "crypto.randomUUID() is not available (needs https or localhost)"
    );
  }
  return window.crypto.randomUUID();
};
