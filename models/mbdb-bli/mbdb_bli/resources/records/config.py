import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from mbdb_bli.resources.records.ui import MbdbBliUIJSONSerializer


class MbdbBliResourceConfig(RecordResourceConfig):
    """MbdbBliRecord resource config."""

    blueprint_name = "mbdb_bli"
    url_prefix = "/mbdb-bli/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_bli.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbBliUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
