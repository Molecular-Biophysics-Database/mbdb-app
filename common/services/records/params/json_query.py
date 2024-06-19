from invenio_records_resources.services.records.params import ParamInterpreter

from luqum.tree import (
    SearchField,
    Word,
    Phrase,
    Range,
    AndOperation,
    OrOperation,
    Group,
    Not,
)
from luqum.elasticsearch import ElasticsearchQueryBuilder, SchemaAnalyzer


class JsonQueryParamInterpreter(ParamInterpreter):
    def apply(self, identity, search, params):
        """
        Applies the constructed query to the search object.
        """
        # Params["advanced_query_json"] contains the search JSON as a dictionary
        if params.get("advanced_query_json"):
            json_criteria = params["advanced_query_json"]
            schema = params.get("schema")

            # Parse the JSON criteria to construct the Luqum tree
            luqum_tree = self.construct_luqum_tree(json_criteria)

            schema_analyzer = SchemaAnalyzer(schema or {})

            es_builder = ElasticsearchQueryBuilder(
                **schema_analyzer.query_builder_options()
            )
            es_query = es_builder(luqum_tree)

            # Apply the constructed query to the search object
            search = search.query({"match_all": {es_query}})

        return search

    @staticmethod
    def construct_luqum_tree(json_criteria):
        """
        Constructs a Luqum tree from JSON criteria.
        """
        base = None
        stack = []
        current_op = None
        pending_not = False  # Flag to indicate the next field should be negated

        for item in json_criteria:
            if "field" in item:
                # Construct the basic search field
                field_value = item["value"]
                if isinstance(field_value, dict):
                    # Range value
                    field_obj = SearchField(
                        item["field"],
                        Range(
                            Word(field_value.get("from", "*")),
                            Word(field_value.get("to", "*")),
                        ),
                    )
                elif isinstance(field_value, str) and " " in field_value:
                    # Phrase value
                    field_obj = SearchField(item["field"], Phrase(f'"{field_value}"'))
                else:
                    # Word value
                    field_obj = SearchField(item["field"], Word(str(field_value)))

                if pending_not:
                    # Wrap the field with a Not operation
                    field_obj = Not(field_obj)
                    pending_not = False  # Reset the flag

                if current_op:
                    # Apply the current operation with the previous operation/base
                    new_base = current_op(base, field_obj) if base else field_obj
                    # Reset base to new operation
                    base = new_base
                    current_op = None
                else:
                    base = field_obj if base is None else AndOperation(base, field_obj)

            elif "operator" in item:
                # Set the current operation based on the operator
                operator = item["operator"].lower()
                if operator == "and":
                    current_op = AndOperation
                elif operator == "or":
                    current_op = OrOperation
                elif operator == "not":
                    # Set the flag to negate the next field
                    pending_not = True

            elif "bracket" in item:
                # Handle bracket operations
                if item["bracket"] == "start":
                    # If we encounter a start bracket, push the current base onto the stack
                    stack.append((current_op, base))
                    base = None
                    current_op = None
                elif item["bracket"] == "end":
                    # Once we hit an end bracket, we know that base contains the grouped operation
                    # Pop the last operation from the stack and apply the current base to it
                    op, last_base = stack.pop()
                    grouped = Group(base)
                    base = op(last_base, grouped) if last_base else grouped

        return base
