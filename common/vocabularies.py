"""Vocabulary helpers of the mbdb models.

The search mapping for vocabulary custom fields (VOCABULARIES_CF) and the
marshmallow schema mixins registered in the model YAML through
``marshmallow_schema_mixins``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import marshmallow
from flask import current_app
from invenio_rdm_records.services.schemas.metadata import FundingSchema
from invenio_search import current_search_client
from invenio_search.utils import build_alias_name
from invenio_vocabularies.records.api import Vocabulary

if TYPE_CHECKING:
    from collections.abc import Callable


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

    # Imported here, like everything below that needs the application context.
    from common.ror import RORError, RORNotFoundError, get_ror

    vocabulary_id = value["id"]
    try:
        _ensure_vocabulary_item("affiliations", vocabulary_id, get_ror)
    except RORNotFoundError as e:
        raise marshmallow.ValidationError(
            {"affiliations": [f"Affiliation {vocabulary_id} is not in the ROR registry."]}
        ) from e
    except RORError as e:
        raise marshmallow.ValidationError(
            {"affiliations": [f"Could not fetch affiliation {vocabulary_id} from ROR."]}
        ) from e
    return value


def _ensure_vocabulary_item(
    vocabulary: str, item_id: str, fetch: Callable[[str], dict[str, Any]]
) -> None:
    """Create an item of a built-in vocabulary (it has its own service) unless it exists."""
    from invenio_access.permissions import system_identity
    from invenio_pidstore.errors import PIDDoesNotExistError
    from sqlalchemy.exc import NoResultFound

    service = getattr(current_app.extensions["invenio-vocabularies"], f"{vocabulary}_service")
    try:
        service.read(system_identity, item_id)
    except (PIDDoesNotExistError, NoResultFound):
        service.create(system_identity, fetch(item_id))


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
        """Create every missing affiliation before the relation schema loads.

        An affiliation that can not be created is reported and left out; without ``valid_data``
        on the error, marshmallow would drop the whole person from a saved draft.
        """
        errors: list[str] = []
        if isinstance(data, dict) and isinstance(data.get("affiliations"), list):
            affiliations = []
            for affiliation in data["affiliations"]:
                if not isinstance(affiliation, dict):
                    affiliations.append(affiliation)
                    continue
                try:
                    affiliations.append(_affiliation_reference(ensure_affiliation_id(affiliation)))
                except marshmallow.ValidationError as e:
                    errors += e.normalized_messages()["affiliations"]
            data = {**data, "affiliations": affiliations}
            if errors and not affiliations:
                del data["affiliations"]
        try:
            loaded = super().load(data, **kwargs)
        except marshmallow.ValidationError as e:
            if not errors:
                raise
            messages = e.normalized_messages()
            messages.setdefault("affiliations", errors)
            raise marshmallow.ValidationError(messages, valid_data=e.valid_data) from e
        if errors:
            raise marshmallow.ValidationError({"affiliations": errors}, valid_data=loaded)
        return loaded


def _affiliation_reference(value: dict[str, Any]) -> dict[str, Any]:
    """Return ``{ id }`` for a vocabulary affiliation; a free-text one (no id) unchanged."""
    return {"id": value["id"]} if value.get("id") else value


def _ensure_funder(funder_id: str) -> None:
    from common.ror import RORError, RORNotFoundError, get_ror

    try:
        _ensure_vocabulary_item("funders", funder_id, get_ror)
    except RORNotFoundError as e:
        raise marshmallow.ValidationError(f"Funder {funder_id} is not in the ROR registry.") from e
    except RORError as e:
        raise marshmallow.ValidationError(f"Could not fetch funder {funder_id} from ROR.") from e


def _ensure_award(award_id: str) -> None:
    from common.openaire import OpenAIREError, OpenAIRENotFoundError, get_award

    def fetch(item_id: str) -> dict[str, Any]:
        payload = get_award(item_id)
        _ensure_funder(payload["funder"]["id"])  # the award refers to it
        return payload

    try:
        _ensure_vocabulary_item("awards", award_id, fetch)
    except OpenAIRENotFoundError as e:
        raise marshmallow.ValidationError(f"Award {award_id} is not in OpenAIRE.") from e
    except OpenAIREError as e:
        raise marshmallow.ValidationError(f"Could not fetch award {award_id} from OpenAIRE.") from e


class AutoCreateFundingSchema(FundingSchema):
    """Funding reference: creates a missing funder (from ROR) and award (from OpenAIRE).

    A custom award (number and title, no id) is loaded as it is.
    """

    def load(self, data: Any, **kwargs: Any) -> Any:
        """Create the missing items before the relations load; the unavailable ones are left out."""
        errors: dict[str, list[str]] = {}
        if isinstance(data, dict):
            data = dict(data)
            for key, ensure in (("funder", _ensure_funder), ("award", _ensure_award)):
                value = data.get(key)
                if not isinstance(value, dict) or not value.get("id"):
                    continue
                try:
                    ensure(value["id"])
                    # a saved reference comes back dereferenced, its other keys are not loadable
                    data[key] = {"id": value["id"]}
                except marshmallow.ValidationError as e:
                    errors[key] = e.messages
                    del data[key]
        try:
            loaded = super().load(data, **kwargs)
        except marshmallow.ValidationError as e:
            if not errors:
                raise
            messages = {**e.normalized_messages(), **errors}
            raise marshmallow.ValidationError(messages, valid_data=e.valid_data) from e
        if errors:
            raise marshmallow.ValidationError(errors, valid_data=loaded)
        return loaded
