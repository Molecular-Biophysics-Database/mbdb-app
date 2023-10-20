import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from mbdb_spr.resources.files.ui import (
    MbdbSprFileDraftUIJSONSerializer,
    MbdbSprFileUIJSONSerializer,
)


class MbdbSprFileResourceConfig(FileResourceConfig):
    """MbdbSprFile resource config."""

    blueprint_name = "mbdb_spr_file"
    url_prefix = "/mbdb-spr/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_spr.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbSprFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class MbdbSprFileDraftResourceConfig(FileResourceConfig):
    """MbdbSprFileDraft resource config."""

    blueprint_name = "mbdb_spr_file_draft"
    url_prefix = "/mbdb-spr/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_spr.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbSprFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
