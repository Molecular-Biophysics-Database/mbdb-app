from invenio_records_resources.services.records.params import ParamInterpreter


class JsonQueryParamInterpreter(ParamInterpreter):
    def apply(self, identity, search, params):
        search = search.query({"match_none": {}})
        return search
