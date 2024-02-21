import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from bli.resources.files.ui import BliFileDraftUIJSONSerializer, BliFileUIJSONSerializer


class BliFileResourceConfig(FileResourceConfig):
    """BliFile resource config."""

    blueprint_name = "bli_file"
    url_prefix = "/records/bli/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.bli.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                BliFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class BliFileDraftResourceConfig(FileResourceConfig):
    """BliFileDraft resource config."""

    blueprint_name = "bli_file_draft"
    url_prefix = "/records/bli/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.bli.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                BliFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
