import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from mbdb_spr.resources.records.ui import MbdbSprUIJSONSerializer


class MbdbSprResourceConfig(RecordResourceConfig):
    """MbdbSprRecord resource config."""

    blueprint_name = "mbdb_spr"
    url_prefix = "/mbdb-spr/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_spr.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbSprUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
