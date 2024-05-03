import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from itc.resources.files.ui import ItcFileDraftUIJSONSerializer, ItcFileUIJSONSerializer


class ItcFileResourceConfig(FileResourceConfig):
    """ItcFile resource config."""

    blueprint_name = "itc_file"
    url_prefix = "/records/itc/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.itc.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ItcFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class ItcFileDraftResourceConfig(FileResourceConfig):
    """ItcFileDraft resource config."""

    blueprint_name = "itc_file_draft"
    url_prefix = "/records/itc/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.itc.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ItcFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
