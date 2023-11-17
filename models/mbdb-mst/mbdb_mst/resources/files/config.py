import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from mbdb_mst.resources.files.ui import (
    MbdbMstFileDraftUIJSONSerializer,
    MbdbMstFileUIJSONSerializer,
)


class MbdbMstFileResourceConfig(FileResourceConfig):
    """MbdbMstFile resource config."""

    blueprint_name = "mbdb_mst_file"
    url_prefix = "/mbdb-mst/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_mst.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbMstFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class MbdbMstFileDraftResourceConfig(FileResourceConfig):
    """MbdbMstFileDraft resource config."""

    blueprint_name = "mbdb_mst_file_draft"
    url_prefix = "/mbdb-mst/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_mst.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbMstFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
