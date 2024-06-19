from invenio_records_resources.services import SearchOptions as InvenioSearchOptions
from .params.json_query import JsonQueryParamInterpreter


class RecordSearchOptions(InvenioSearchOptions):
    params_interpreters_cls = [
        *InvenioSearchOptions.params_interpreters_cls,
        JsonQueryParamInterpreter,
    ]
