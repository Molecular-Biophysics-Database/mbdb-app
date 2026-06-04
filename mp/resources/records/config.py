import importlib_metadata
from flask_resources.serializers.json import JSONSerializer
from invenio_records_resources.resources.records.headers import etag_headers
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.resources.config import BaseRecordResourceConfig
from oarepo_runtime.resources.responses import ExportableResponseHandler
from invenio_rdm_records.services.errors import RecordDeletedException
from common.utils.tombstone import record_deleted_without_note_error_handler
from mp.resources.records.ui import MpUIJSONSerializer


class MpResourceConfig(BaseRecordResourceConfig):
    """MpRecord resource config."""

    blueprint_name = "mp"
    url_prefix = "/records/mp/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.mp.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/json": ExportableResponseHandler(
                export_code="json",
                name=_("Native JSON"),
                serializer=JSONSerializer(),
                headers=etag_headers,
            ),
            "application/vnd.inveniordm.v1+json": ExportableResponseHandler(
                export_code="ui_json",
                name=_("Native UI JSON"),
                serializer=MpUIJSONSerializer(),
            ),
            **entrypoint_response_handlers,
        }

    @property
    def error_handlers(self):
        entrypoint_error_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mp_record.error_handlers"
        ):
            entrypoint_error_handlers.update(x.load())
        return {
            **super().error_handlers,
            **entrypoint_error_handlers,
            RecordDeletedException: record_deleted_without_note_error_handler,
        }

    @property
    def request_body_parsers(self):
        entrypoint_request_bodyparsers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mp_record.request_bodyparsers"
        ):
            entrypoint_request_bodyparsers.update(x.load())
        return {
            **super().request_body_parsers,
            **entrypoint_request_bodyparsers,
        }
