from invenio_i18n import lazy_gettext as _
from invenio_records_resources.services.records.facets import TermsFacet
from invenio_requests.proxies import current_request_type_registry
from invenio_requests.services.requests import facets


def _type_labels(type_ids):
    """Invenio's labels, and the types' own names for those it does not know (oarepo's)."""
    names = {type_.type_id: type_.name for type_ in current_request_type_registry}
    return {id_: facets.type._value_labels.get(id_) or names.get(id_, id_) for id_ in type_ids}


REQUESTS_FACETS = {
    "type": {
        "facet": TermsFacet(field="type", label=_("Type"), value_labels=_type_labels),
        "ui": {"field": "type"},
    },
    "status": {"facet": facets.status, "ui": {"field": "status"}},
}
