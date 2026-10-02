import { useEffect, useState } from "react";
import axios from "axios";

// Item cache for vocabulary values. The server stores just { id } in the
// record and its ui serialization carries no titles, so a freshly loaded
// draft would show the raw id in the dropdown. rememberItem stores the
// whole item ({ title, customFields }) of every option the user picked
// during this session; for ids the cache does not know (a reload),
// useVocabularyItem does one GET per id and caches the result.
// Module-level Maps: the cache survives remounts.
//
// The request needs Invenio's `Accept: application/vnd.inveniordm.v1+json`
// header: without it the item comes back with only `title.en` — no
// `title_l10n` and no `custom_fields`. Plain axios (already an app
// dependency) so this module keeps no import that Jest cannot load
// (the alias index would pull oarepo's forms package through fields.jsx).

const items = new Map();
const pending = new Map();

const cacheKey = (type, id) => `${type}/${id}`;

// The single item response carries title_l10n on newer oarepo and the
// localized title object otherwise; custom_fields may be absent entirely.
const extractItem = (record) => ({
  title: record?.title_l10n ?? record?.title?.en ?? undefined,
  customFields: record?.custom_fields ?? undefined,
});

// Merges into the cache entry without clobbering parts the caller does
// not pass (rememberTitle's entry must not wipe a fetched customFields).
export const rememberItem = (type, id, { title, customFields } = {}) => {
  if (!type || !id) return;
  const key = cacheKey(type, id);
  const stored = items.get(key) ?? {};
  items.set(key, {
    title: typeof title === "string" && title !== "" ? title : stored.title,
    customFields: customFields ?? stored.customFields,
  });
};

export const rememberTitle = (type, id, title) =>
  rememberItem(type, id, { title });

// One in-flight request per id: concurrent hooks for the same id share it.
const fetchItem = (type, id) => {
  const key = cacheKey(type, id);
  if (!pending.has(key)) {
    pending.set(
      key,
      axios
        .get(
          `/api/vocabularies/${encodeURIComponent(type)}/${encodeURIComponent(
            id
          )}`,
          { headers: { Accept: "application/vnd.inveniordm.v1+json" } }
        )
        .then((response) => {
          const item = extractItem(response?.data);
          pending.delete(key);
          if (item.title !== undefined || item.customFields !== undefined)
            rememberItem(type, id, item);
          return item;
        })
        .catch(() => {
          // A failed lookup shows the id; a later mount retries.
          pending.delete(key);
          return undefined;
        })
    );
  }
  return pending.get(key);
};

// The cached item for a vocabulary id ({ title, customFields }), both
// undefined while the item is not known yet. State is keyed by (type, id):
// on an id change the old id's item is never returned — the cache is read
// synchronously on every render and the state is applied only when its
// key still matches the current props.
export const useVocabularyItem = (type, id) => {
  const key = id ? cacheKey(type, id) : undefined;
  const [state, setState] = useState(() => ({
    key,
    item: key ? items.get(key) : undefined,
  }));

  useEffect(() => {
    if (!id) return undefined;
    const k = cacheKey(type, id);
    const cached = items.get(k);
    if (cached !== undefined) {
      setState({ key: k, item: cached });
      return undefined;
    }
    let cancelled = false;
    fetchItem(type, id).then((fetched) => {
      if (!cancelled && fetched !== undefined)
        setState({ key: k, item: fetched });
    });
    return () => {
      cancelled = true;
    };
  }, [type, id]);

  const item =
    state.key === key ? state.item : key ? items.get(key) : undefined;
  return { title: item?.title, customFields: item?.customFields };
};

// The title for a vocabulary id, or undefined while it is not known yet.
export const useVocabularyTitle = (type, id) =>
  useVocabularyItem(type, id).title;
