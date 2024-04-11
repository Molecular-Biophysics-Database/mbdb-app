from invenio_records_resources.services.records.params import ParamInterpreter


class AdvancedSearchParamInterpreterCls(ParamInterpreter):
    # TODO: implement this
    def apply(self, identity, search, params):
        """Evaluate the query str on the search."""
        # get the json from "facets"
        if "json" in params["facets"]:
            # convert to query
            search = search.query(query)

        return search