import { useEffect, useState } from "react";
import axios from "axios";

// Title cache for vocabulary values. The server stores just { id } in the
// record and its ui serialization carries no titles, so a freshly loaded
// draft would show the raw id in the dropdown. rememberTitle stores the
// title of every option the user picked during this session; for ids the
// cache does not know (a reload), useVocabularyTitle does one GET per id
// and caches the result. Module-level Maps: the cache survives remounts.

const titles = new Map();
const pending = new Map();

const cacheKey = (type, id) => `${type}/${id}`;

// The single item response carries title_l10n on newer oarepo and the
// localized title object otherwise.
const extractTitle = (record) =>
  record?.title_l10n ?? record?.title?.en ?? undefined;

export const rememberTitle = (type, id, title) => {
  if (type && id && typeof title === "string" && title !== "") {
    titles.set(cacheKey(type, id), title);
  }
};

// One in-flight request per id: concurrent hooks for the same id share it.
const fetchTitle = (type, id) => {
  const key = cacheKey(type, id);
  if (!pending.has(key)) {
    pending.set(
      key,
      axios
        .get(`/api/vocabularies/${type}/${encodeURIComponent(id)}`)
        .then((response) => {
          const title = extractTitle(response?.data);
          pending.delete(key);
          if (title !== undefined) titles.set(key, title);
          return title;
        })
        .catch(() => {
          // A failed title lookup shows the id; a later mount retries.
          pending.delete(key);
          return undefined;
        })
    );
  }
  return pending.get(key);
};

// The title for a vocabulary id, or undefined while it is not known yet.
// Reads the cache first; on a miss it fetches once and re-renders when the
// title lands.
export const useVocabularyTitle = (type, id) => {
  const [title, setTitle] = useState(
    id ? titles.get(cacheKey(type, id)) : undefined
  );

  useEffect(() => {
    if (!id) return undefined;
    const cached = titles.get(cacheKey(type, id));
    if (cached !== undefined) {
      setTitle(cached);
      return undefined;
    }
    let cancelled = false;
    fetchTitle(type, id).then((fetched) => {
      if (!cancelled && fetched !== undefined) setTitle(fetched);
    });
    return () => {
      cancelled = true;
    };
  }, [type, id]);

  return title;
};
