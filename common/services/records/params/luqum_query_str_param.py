from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.params import QueryStrParam
from invenio_search import current_search


class LuqumQueryStrParam(QueryStrParam):
    config: SearchOptions

    def apply(self, identity, search, params):
        # mapping_name = self.config.mapping_name - for now, keep it on search options
        # mapping_file = current_search.mappings[mapping_name]
        # call luqum here
        # get processed query
        # update search
        # and remove this
        return super().apply(identity, search, params)