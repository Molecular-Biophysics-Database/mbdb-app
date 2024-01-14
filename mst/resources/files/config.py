import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from mst.resources.files.ui import MstFileDraftUIJSONSerializer, MstFileUIJSONSerializer


class MstFileResourceConfig(FileResourceConfig):
    """MstFile resource config."""

    blueprint_name = "mst_file"
    url_prefix = "/records/mst/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.mst.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MstFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class MstFileDraftResourceConfig(FileResourceConfig):
    """MstFileDraft resource config."""

    blueprint_name = "mst_file_draft"
    url_prefix = "/records/mst/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.mst.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MstFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
