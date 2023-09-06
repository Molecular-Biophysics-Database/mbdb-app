import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from mbdb_bli.resources.files.ui import (
    MbdbBliFileDraftUIJSONSerializer,
    MbdbBliFileUIJSONSerializer,
)


class MbdbBliFileResourceConfig(FileResourceConfig):
    """MbdbBliFile resource config."""

    blueprint_name = "mbdb_bli_file"
    url_prefix = "/mbdb-bli/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_bli.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbBliFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class MbdbBliFileDraftResourceConfig(FileResourceConfig):
    """MbdbBliFileDraft resource config."""

    blueprint_name = "mbdb_bli_file_draft"
    url_prefix = "/mbdb-bli/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_bli.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbBliFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
