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


def _vocabulary_payload(value: dict[str, Any], vocabulary_id: str) -> dict[str, Any]:
    """Vocabulary item data for a manual chemical, in the shape create/update accept."""
    title = value["title"] if isinstance(value["title"], dict) else {"en": value["title"]}
    custom_fields = {key: value[key] for key in _CUSTOM_FIELD_KEYS if value.get(key) is not None}
    data: dict[str, Any] = {"id": vocabulary_id, "type": CHEMICALS_VOCABULARY, "title": title}
    if custom_fields:
        data["custom_fields"] = custom_fields
    return data


def _drop_deleted_chemical(vocabulary_id: str) -> None:
    """Remove a tombstoned auto-created chemical entirely, so it can be created again.

    A manually entered chemical has a deterministic pid (uuid5 of its content), so any
    harder vocabulary cleanup (index destroy, data reset, a soft delete at record level)
    lands it in a state every public entry point refuses: ``read`` raises
    ``PIDDeletedError``, service ``delete`` resolves through the same pid and fails the
    same way, and pidstore's own ``assign``/``create`` reject re-attaching a deleted pid
    (`PIDInvalidAction: you cannot assign objects to a deleted identifier`; and the
    `(pid_type, pid_value)` unique index blocks registering it anyway).

    There is no service-side revive either: `invenio_records` supports only soft
    deletes (`json IS NULL` on the vocabulary record row) and hard deletes
    (`Record.delete(force=True)`) — undeleting is not an operation. The sanctioned
    lifecycle for a safely-deleted vocabulary item is therefore: drop its pid row and
    its zombie record row, then let the caller create it fresh under the same
    deterministic id. That is what this does, at the pidstore/model level the service
    layer cannot reach.
    """
    from invenio_db import db
    from invenio_pidstore.models import PIDStatus, PersistentIdentifier
    from invenio_vocabularies.records.models import VocabularyMetadata

    tombstones = PersistentIdentifier.query.filter_by(
        pid_value=vocabulary_id, status=PIDStatus.DELETED
    ).all()
    # Records hooked to the tombstone pids (the empty-payload zombies of a soft delete;
    # nothing else by definition since the pid row blocked resolution of anything else).
    zombie_uuids = [t.object_uuid for t in tombstones if t.object_uuid]
    for tombstone in tombstones:
        db.session.delete(tombstone)
    if zombie_uuids:
        zombies = (
            db.session.query(VocabularyMetadata)
            .filter(VocabularyMetadata.id.in_(zombie_uuids))
            .all()
        )
        for zombie in zombies:
            db.session.delete(zombie)
    db.session.flush()


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
    from invenio_pidstore.errors import PIDDeletedError, PIDDoesNotExistError
    from invenio_vocabularies.proxies import current_service

    vocabulary_id = manual_chemical_id(value)
    payload = _vocabulary_payload(value, vocabulary_id)
    try:
        current_service.read(system_identity, (CHEMICALS_VOCABULARY, vocabulary_id))
    except PIDDeletedError:
        # The item existed before and got wiped: pidstore keeps a deleted tombstone for
        # its deterministic pid, which blocks resolving AND re-creating. Undelete does
        # not exist in the invenio model, so drop the tombstone and its zombie record,
        # then create the item again under the same deterministic id.
        _drop_deleted_chemical(vocabulary_id)
        current_service.create(system_identity, payload)
    except PIDDoesNotExistError:
        current_service.create(system_identity, payload)

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


def ensure_affiliation_id(value: dict[str, Any]) -> dict[str, Any]:
    """Return ``value`` with an ``id`` that resolves as an ``affiliations`` vocabulary item.

    The deposit form's affiliation picker searches the live ROR API, so a picked organization
    may not be in the local vocabulary dump yet. If the id does not resolve, the organization is
    fetched from ROR (``common.ror.get_ror``) and created, in the same shape the dump loads.
    The input dict is not modified.
    """
    if not value.get("id"):
        return value

    # Imported here: they need the application context, which exists at load time.
    from flask import current_app
    from invenio_access.permissions import system_identity
    from invenio_pidstore.errors import PIDDoesNotExistError
    from sqlalchemy.exc import NoResultFound

    from common.ror import RORError, RORNotFoundError, get_ror

    vocabulary_id = value["id"]
    # The affiliations vocabulary is Invenio's built-in one, with its own service.
    affiliations_service = current_app.extensions["invenio-vocabularies"].affiliations_service
    try:
        affiliations_service.read(system_identity, vocabulary_id)
        return value
    except (PIDDoesNotExistError, NoResultFound):
        pass

    try:
        payload = get_ror(vocabulary_id)
    except RORNotFoundError as e:
        raise marshmallow.ValidationError(
            {"affiliations": [f"Affiliation {vocabulary_id} is not in the ROR registry."]}
        ) from e
    except RORError as e:
        raise marshmallow.ValidationError(
            {"affiliations": [f"Could not fetch affiliation {vocabulary_id} from ROR."]}
        ) from e

    affiliations_service.create(system_identity, payload)
    return value


class AutoCreateAffiliationsMixin(marshmallow.Schema):
    """Schema mixin for a person: creates missing affiliations from ROR.

    The affiliation picker writes ``{ id }`` references to ROR organizations that may not be in the
    local ``affiliations`` vocabulary yet. Before loading, this mixin creates each missing item
    from the ROR API (see ``ensure_affiliation_id``), so the pid relation that follows in the
    MRO resolves like any dumped affiliation.
    """

    def load(self, data: Any, **kwargs: Any) -> Any:
        """Create every missing affiliation before the relation schema loads."""
        if isinstance(data, dict) and isinstance(data.get("affiliations"), list):
            data = {
                **data,
                "affiliations": [
                    ensure_affiliation_id(affiliation) if isinstance(affiliation, dict) else affiliation
                    for affiliation in data["affiliations"]
                ],
            }
        return super().load(data, **kwargs)
