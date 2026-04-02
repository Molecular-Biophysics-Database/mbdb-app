from oarepo_runtime.services.search import (
    I18nRDMDraftsSearchOptions,
    I18nRDMSearchOptions,
)

from .params.json_query import JsonQueryParamInterpreter

class ExcludeDeletedParamInterpreter:
    """Always exclude deleted/tombstoned records from search."""

    def __init__(self, search_options=None):
        self.search_options = search_options

    def apply(self, identity, search, params):
        search = search.exclude("term", state="deleted")
        search = search.exclude("exists", field="tombstone")
        return search

class RecordSearchOptions(I18nRDMSearchOptions):
    params_interpreters_cls = [
        ExcludeDeletedParamInterpreter,
        *I18nRDMSearchOptions.params_interpreters_cls,
        JsonQueryParamInterpreter,
    ]


class DraftSearchOptions(I18nRDMDraftsSearchOptions):
    params_interpreters_cls = [
        ExcludeDeletedParamInterpreter,
        *I18nRDMDraftsSearchOptions.params_interpreters_cls,
        JsonQueryParamInterpreter,
    ]
