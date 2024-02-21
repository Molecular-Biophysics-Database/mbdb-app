import importlib_metadata
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig

from mst.resources.records.ui import MstUIJSONSerializer


class MstResourceConfig(RecordResourceConfig):
    """MstRecord resource config."""

    blueprint_name = "mst"
    url_prefix = "/records/mst/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.mst.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                MstUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
