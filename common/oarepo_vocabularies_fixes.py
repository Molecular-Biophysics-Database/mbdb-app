"""TEMPORARY: make the oarepo-vocabularies UI work with Invenio's dedicated vocabularies.

Affiliations, funders, awards and names (VOCABULARIES_CUSTOM_VOCABULARY_TYPES) have their
own services and endpoints (/api/affiliations, ...). oarepo-vocabularies (10.2.1) only
looks at the generic vocabularies service, so on /vocabularies/ they show count 0, their
search page is empty and their detail page is a 404. Invenio's own type listing handles
them (invenio_vocabularies/services/results.py: _custom_vocabulary_statistics).

Remove this module (and its lines in invenio.cfg) once fixed in oarepo-vocabularies.
"""

import inspect
from pathlib import Path

from flask import current_app, g, url_for
from invenio_records_resources.proxies import current_service_registry
from oarepo_vocabularies.services.service import VocabularyTypeService
from oarepo_vocabularies.ui.resources.config import InvenioVocabulariesUIResourceConfig
from oarepo_vocabularies.ui.resources.resource import InvenioVocabulariesUIResource


def custom_vocabulary_types():
    """Vocabulary types that have a dedicated service registered."""
    return [
        t
        for t in current_app.config.get("VOCABULARIES_CUSTOM_VOCABULARY_TYPES", [])
        if t in current_service_registry._services  # noqa: SLF001
    ]


def _custom_type(vocabulary_type):
    return vocabulary_type if vocabulary_type in custom_vocabulary_types() else None


class FixedVocabularyTypeService(VocabularyTypeService):
    """/vocabularies/ listing: add item counts of dedicated vocabularies, as Invenio does."""

    def _vocabulary_statistics(self):
        stats = super()._vocabulary_statistics()
        for vocabulary_type in custom_vocabulary_types():
            model_cls = current_service_registry.get(vocabulary_type).config.record_cls.model_cls
            stats[vocabulary_type] = stats.get(vocabulary_type, 0) + model_cls.query.count()
        return stats


class FixedVocabulariesUIResourceConfig(InvenioVocabulariesUIResourceConfig):
    """Search page of dedicated vocabularies uses /api/<type> and its sort/facet options."""

    template_folder = str(
        (Path(inspect.getfile(InvenioVocabulariesUIResourceConfig)).parent / "../templates").resolve()
    )

    def search_endpoint_url(self, identity, overrides=None, **kwargs):
        url = super().search_endpoint_url(identity, overrides=overrides, **kwargs)
        vocabulary_type = _custom_type((overrides or {}).get("vocabularyType"))
        if vocabulary_type:
            url = url.replace(f"/vocabularies/{vocabulary_type}", f"/{vocabulary_type}")
        return url

    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        vocabulary_type = _custom_type((overrides or {}).get("vocabularyType"))
        if vocabulary_type:
            api_config = current_service_registry.get(vocabulary_type).config
            kwargs.pop("endpoint", None)
            kwargs.pop("initial_filters", None)
        return super().search_app_config(identity, api_config, overrides=overrides, **kwargs)


class _WithVocabularyHtmlLink:
    """Links template adding the vocabulary_html link the detail templates expect."""

    def __init__(self, links_tpl, vocabulary_type):
        self._links_tpl = links_tpl
        self._vocabulary_type = vocabulary_type

    def expand(self, identity, obj):
        links = self._links_tpl.expand(identity, obj)
        links["vocabulary_html"] = url_for(
            "oarepo_vocabularies_ui.search", type=self._vocabulary_type, _external=True
        )
        return links


class FixedVocabulariesUIResource(InvenioVocabulariesUIResource):
    """Detail page reads dedicated vocabularies from their own service."""

    def _get_record(self, pid_value, *args, vocabulary_type=None, **kwargs):
        if _custom_type(vocabulary_type):
            item = current_service_registry.get(vocabulary_type).read(g.identity, pid_value)
            item._links_tpl = _WithVocabularyHtmlLink(item._links_tpl, vocabulary_type)  # noqa: SLF001
            return item
        return super()._get_record(pid_value, *args, vocabulary_type=vocabulary_type, **kwargs)
