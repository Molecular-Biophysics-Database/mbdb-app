"""Facets on general_parameters, shared by the models."""

from __future__ import annotations

from invenio_i18n import lazy_gettext as _
from invenio_records_resources.services.records.facets import TermsFacet

_GP = "metadata.general_parameters"
_INFO = f"{_GP}.record_information"


def _facet(field, label, **kwargs):
    return {field: TermsFacet(field=field, label=label, **kwargs)}


def _iso_dates(values):
    """Label date buckets: the index returns them as 20260723."""
    return {v: f"{v[:4]}-{v[4:6]}-{v[6:]}" for v in values}


# oarepo-model generates no facets inside polymorphic fields (record_information,
# entities), and labels the method facet after its type; same set and order as
# the mbdb-app-rdm-12 dashboard
GENERAL_PARAMETERS_FACETS = {
    **_facet(f"{_GP}.method", _("Method")),
    **_facet(f"{_INFO}.access_rights", _("Access rights")),
    **_facet(f"{_INFO}.copyright", _("Copyright")),
    **_facet(f"{_INFO}.deposition_date", _("Deposition date"), value_labels=_iso_dates),
    **_facet(f"{_INFO}.license.name", _("License name")),
    **_facet(f"{_INFO}.publisher", _("Publisher")),
    **_facet(f"{_INFO}.resource_type", _("Resource type")),
    **_facet(f"{_INFO}.resource_type_general", _("Resource type general")),
    **_facet(f"{_INFO}.subject_category", _("Subject category")),
    **_facet(f"{_GP}.entities_of_interest.type", _("Type")),
}
