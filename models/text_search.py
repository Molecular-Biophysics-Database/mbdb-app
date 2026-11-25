"""Full-text search over the fields marked with copy_to in the model files."""

from __future__ import annotations

from oarepo_model.customizations import (
    PatchJSONFile,
    SetDefaultSearchFields,
)
from oarepo_model.datatypes.strings import KeywordDataType

_FIELD = "collected_default_search_fields"


class CopyToKeywordDataType(KeywordDataType):
    """Keyword honouring ``mapping.copy_to``, which oarepo-model ignores."""

    TYPE = "keyword"

    def create_mapping(self, element):
        mapping = super().create_mapping(element)
        copy_to = element.get("mapping", {}).get("copy_to")
        return {**mapping, "copy_to": copy_to} if copy_to else mapping


TEXT_SEARCH_TYPES = {"keyword": CopyToKeywordDataType}

TEXT_SEARCH_CUSTOMIZATIONS = [
    # not PatchIndexSettings: it would drop the analyzers already defined
    PatchJSONFile(
        "record-mapping",
        {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "word_prefix": {"tokenizer": "word_prefix", "filter": ["lowercase"]},
                    },
                    "tokenizer": {
                        "word_prefix": {
                            "type": "edge_ngram",
                            "min_gram": 3,
                            "max_gram": 20,
                            "token_chars": ["letter", "digit"],
                        },
                    },
                },
            },
            "mappings": {
                "properties": {
                    _FIELD: {
                        "type": "text",
                        "fields": {
                            # searched as typed: "poly" finds polymerase, not the reverse
                            "prefix": {"type": "text", "analyzer": "word_prefix", "search_analyzer": "standard"},
                        },
                    },
                },
            },
        },
    ),
    # vocabulary titles (organisms, chemicals) are text already
    SetDefaultSearchFields("id", _FIELD, f"{_FIELD}.prefix", "metadata.*.title.*"),
]
