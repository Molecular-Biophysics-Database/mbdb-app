import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from spr.resources.files.ui import SprFileDraftUIJSONSerializer, SprFileUIJSONSerializer


class SprFileResourceConfig(FileResourceConfig):
    """SprFile resource config."""

    blueprint_name = "spr_file"
    url_prefix = "/records/spr/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.spr.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                SprFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class SprFileDraftResourceConfig(FileResourceConfig):
    """SprFileDraft resource config."""

    blueprint_name = "spr_file_draft"
    url_prefix = "/records/spr/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.spr.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                SprFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
