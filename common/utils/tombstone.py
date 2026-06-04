from flask import render_template, jsonify
from invenio_app_rdm.records_ui.views.records import not_found_error
from invenio_rdm_records.resources.serializers import UIJSONSerializer
from oarepo_runtime.i18n import lazy_gettext as _

def record_tombstone_error(error):
    """Tombstone page."""
    # the RecordDeletedError will have the following properties,
    # while the PIDDeletedError won't
    record = getattr(error, "record", None)
    if (record_ui := getattr(error, "result_item", None)) is not None:
        if record is None:
            record = record_ui._record

        record_ui = UIJSONSerializer().dump_obj(record_ui.to_dict())

    # render a 404 page if the tombstone isn't visible
    if not record.tombstone.is_visible:
        return not_found_error(error)

    # we only render a tombstone page if there is a record with a visible tombstone
    return (
        render_template(
            # changed only path to tombstone.html
            "tombstone.html",
            record=record_ui,
        ),
        410,
    )


def record_deleted_without_note_error_handler(e):
    """Return public tombstone API response without private tombstone note."""
    tombstone = e.record.tombstone.dump()
    tombstone.pop("note", None)

    response = jsonify(
        status=410,
        message=str(_("Record deleted")),
        tombstone=tombstone,
    )
    response.status_code = 410
    return response