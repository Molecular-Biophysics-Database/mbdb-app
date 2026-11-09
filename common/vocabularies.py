"""Search mapping for vocabulary custom fields (VOCABULARIES_CF)."""

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
