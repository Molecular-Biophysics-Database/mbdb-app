from oarepo_runtime.services.search import (
    I18nRDMDraftsSearchOptions,
    I18nRDMSearchOptions,
)

from .params.json_query import JsonQueryParamInterpreter


class RecordSearchOptions(I18nRDMSearchOptions):
    params_interpreters_cls = [
        *I18nRDMSearchOptions.params_interpreters_cls,
        JsonQueryParamInterpreter,
    ]


class DraftSearchOptions(I18nRDMDraftsSearchOptions):
    params_interpreters_cls = [
        *I18nRDMDraftsSearchOptions.params_interpreters_cls,
        JsonQueryParamInterpreter,
    ]
