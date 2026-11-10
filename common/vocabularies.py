"""Vocabulary helpers of the mbdb models.

The search mapping for vocabulary custom fields (VOCABULARIES_CF) and the
marshmallow schema mixins registered in the model YAML through
``marshmallow_schema_mixins``.
"""

from __future__ import annotations

from typing import Any

import marshmallow
from flask import current_app
from invenio_search import current_search_client
from invenio_search.utils import build_alias_name
from invenio_vocabularies.records.api import Vocabulary


def init_vocabularies_custom_fields_mapping() -> None:
    """Add VOCABULARIES_CF fields to the (strict) vocabularies index mapping.

    Neither invenio nor oarepo creates this mapping, so without it indexing of any
    vocabulary item with custom_fields (e.g. chemicals) fails. Registered as an
    ``oarepo.cli.search.init`` entry point, so it runs on ``invenio index init``.
    """
    custom_fields = current_app.config.get("VOCABULARIES_CF", [])
    if not custom_fields:
        return
    current_search_client.indices.put_mapping(
        index=build_alias_name(Vocabulary.index._name),  # noqa: SLF001
        body={
            "properties": {
                "custom_fields": {
                    "type": "object",
                    "properties": {cf.name: cf.mapping for cf in custom_fields},
                }
            }
        },
    )


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

    A saved affiliation comes back from the API dereferenced (``id``, ``name``, ``identifiers``),
    and the deposit form sends it back as it got it. Invenio's ``AffiliationRelationSchema``
    declares ``identifiers`` dump-only, so loading it fails with "Unknown field."; an affiliation
    with an ``id`` is therefore reduced to ``{ id }`` (the relation dereferences the rest again).
    """

    def load(self, data: Any, **kwargs: Any) -> Any:
        """Create every missing affiliation before the relation schema loads."""
        if isinstance(data, dict) and isinstance(data.get("affiliations"), list):
            data = {
                **data,
                "affiliations": [
                    _affiliation_reference(ensure_affiliation_id(affiliation))
                    if isinstance(affiliation, dict)
                    else affiliation
                    for affiliation in data["affiliations"]
                ],
            }
        return super().load(data, **kwargs)


def _affiliation_reference(value: dict[str, Any]) -> dict[str, Any]:
    """Return ``{ id }`` for a vocabulary affiliation; a free-text one (no id) unchanged."""
    return {"id": value["id"]} if value.get("id") else value
