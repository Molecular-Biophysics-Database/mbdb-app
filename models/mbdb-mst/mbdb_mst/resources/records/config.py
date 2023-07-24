import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from mbdb_mst.resources.records.ui import MbdbMstUIJSONSerializer


class MbdbMstResourceConfig(RecordResourceConfig):
    """MbdbMstRecord resource config."""

    blueprint_name = "mbdb_mst"
    url_prefix = "/mbdb-mst/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mbdb_mst.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MbdbMstUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
