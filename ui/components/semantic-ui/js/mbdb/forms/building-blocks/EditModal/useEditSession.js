import { useState } from "react";
import cloneDeep from "lodash/cloneDeep";

// Snapshot-based editing of one item (guide §9). `read`/`restore`/`remove`
// are supplied by the caller, because an array item and an object key are
// read and removed differently. `openExisting` deep-clones the current value,
// so edits inside the modal never leak into the snapshot Cancel restores.
export const useEditSession = ({ read, restore, remove }) => {
  const [session, setSession] = useState(null); // { key, isNew, snapshot }
  return {
    session,
    openNew: (key) => setSession({ key, isNew: true, snapshot: null }),
    openExisting: (key, extra) =>
      setSession({
        key,
        isNew: false,
        snapshot: cloneDeep(read(key)),
        ...extra,
      }),
    cancel: () => {
      if (!session) return; // a second Escape/Cancel after close is a no-op
      if (session.isNew) remove(session.key);
      else restore(session.key, session.snapshot);
      setSession(null);
    },
    done: () => setSession(null),
  };
};
