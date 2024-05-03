import importlib_metadata
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig

from itc.resources.records.ui import ItcUIJSONSerializer


class ItcResourceConfig(RecordResourceConfig):
    """ItcRecord resource config."""

    blueprint_name = "itc"
    url_prefix = "/records/itc/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.itc.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ItcUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
