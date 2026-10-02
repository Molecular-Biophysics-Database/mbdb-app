"""Marshmallow schema mixins for vocabulary fields of the mbdb models.

Registered in the model YAML through ``marshmallow_schema_mixins``, for example::

    basic_information:
      type: vocabulary
      vocabulary-type: chemicals
      marshmallow_schema_mixins:
        - common.vocabularies.AutoCreateChemicalMixin
"""

from __future__ import annotations

import json
import uuid
from typing import Any

import marshmallow

CHEMICALS_VOCABULARY = "chemicals"
MANUAL_CHEMICAL_ID_PREFIX = "manual:"

# Namespace for the deterministic ids of manually entered chemicals. Do not change it:
# existing ids would no longer match their content.
_MANUAL_CHEMICAL_NAMESPACE = uuid.UUID("2f6c6b1e-6f0a-4d8e-9d0b-6a4f2c8e1b37")

# Keys of a chemical that are stored in the vocabulary item's custom fields
# (VOCABULARIES_CF in invenio.cfg).
_CUSTOM_FIELD_KEYS = ("chemical_formula", "molecular_weight", "additional_identifiers")


def manual_chemical_id(value: dict[str, Any]) -> str:
    """Return the vocabulary id for a manually entered chemical.

    The id is derived from the content, so saving the same manual chemical again (a second
    load of the same data, or a client that resends it) reuses one vocabulary item instead
    of creating duplicates.
    """
    content = {key: value.get(key) for key in ("title", *_CUSTOM_FIELD_KEYS)}
    canonical = json.dumps(content, sort_keys=True, ensure_ascii=False)
    return f"{MANUAL_CHEMICAL_ID_PREFIX}{uuid.uuid5(_MANUAL_CHEMICAL_NAMESPACE, canonical)}"


def _has_title(value: dict[str, Any]) -> bool:
    title = value.get("title")
    if isinstance(title, dict):
        return any(isinstance(text, str) and text.strip() for text in title.values())
    return isinstance(title, str) and bool(title.strip())


def ensure_chemical_id(value: dict[str, Any]) -> dict[str, Any]:
    """Return ``value`` with the ``id`` of a ``chemicals`` vocabulary item.

    A value with an ``id`` is returned unchanged. A value without one (a chemical entered by
    hand in the deposit form) gets the id of a vocabulary item created from its title and
    facts, or of the existing item with the same content. The input dict is not modified.
    """
    if value.get("id"):
        return value
    if not _has_title(value):
        raise marshmallow.ValidationError({"title": ["Missing data for required field."]})

    # Imported here: they need the application context, which exists at load time.
    from invenio_access.permissions import system_identity
    from invenio_pidstore.errors import PIDDoesNotExistError
    from invenio_vocabularies.proxies import current_service

    vocabulary_id = manual_chemical_id(value)
    try:
        current_service.read(system_identity, (CHEMICALS_VOCABULARY, vocabulary_id))
    except PIDDoesNotExistError:
        title = value["title"] if isinstance(value["title"], dict) else {"en": value["title"]}
        custom_fields = {key: value[key] for key in _CUSTOM_FIELD_KEYS if value.get(key) is not None}
        data: dict[str, Any] = {"id": vocabulary_id, "type": CHEMICALS_VOCABULARY, "title": title}
        if custom_fields:
            data["custom_fields"] = custom_fields
        current_service.create(system_identity, data)

    return {**value, "id": vocabulary_id}


class AutoCreateChemicalMixin(marshmallow.Schema):
    """Schema mixin for a ``chemicals`` vocabulary relation: creates missing chemicals.

    A chemical without ``id`` cannot be resolved as a vocabulary relation. Before loading, this
    mixin gives it the id of a vocabulary item created from the submitted data (see
    ``ensure_chemical_id``). The relation schema that follows in the MRO (``RelationSchema``)
    then loads it like any picked chemical: only the ``id`` is kept, and the other keys are
    copied from the vocabulary item on dereference.
    """

    def load(self, data: Any, **kwargs: Any) -> Any:
        if isinstance(data, dict):
            data = ensure_chemical_id(data)
        return super().load(data, **kwargs)
