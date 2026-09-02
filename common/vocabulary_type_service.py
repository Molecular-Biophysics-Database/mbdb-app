from flask_babel.speaklater import LazyString
from oarepo_vocabularies.services.service import (
    VocabularyTypeService as BaseVocabularyTypeService,
)


def _resolve_lazy_strings(value):
    """Recursively replaces LazyString instances with their resolved str value.

    ``configure_vocabulary(...)`` entries in invenio.cfg use ``_(...)`` for
    translatable labels/descriptions, which produces LazyString objects that
    the JSON encoder cannot serialize.
    """
    if isinstance(value, LazyString):
        return str(value)
    if isinstance(value, dict):
        return {k: _resolve_lazy_strings(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_resolve_lazy_strings(v) for v in value]
    return value


class VocabularyTypeService(BaseVocabularyTypeService):
    """Vocabulary types service that returns only JSON-serializable metadata.

    The base implementation copies the raw ``configure_vocabulary(...)``
    config dict (including the ``authority`` AuthorityProvider *class*, and
    LazyString-valued translations) straight into the API response, which
    blows up JSON serialization.
    """

    def search(self, identity):
        result_list = super().search(identity)
        for item in result_list._results:
            item.pop("authority", None)
            for key, value in item.items():
                item[key] = _resolve_lazy_strings(value)
        return result_list
