from invenio_records_resources.services import SearchOptions as InvenioSearchOptions
from invenio_records_resources.services.records.params import QueryStrParam, PaginationParam, SortParam, FacetsParam

from .params.luqum_query_str_param import LuqumQueryStrParam


class MBDBSearchOptions(InvenioSearchOptions):
    params_interpreters_cls = [LuqumQueryStrParam, PaginationParam, SortParam, FacetsParam]
