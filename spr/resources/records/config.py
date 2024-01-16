import importlib_metadata
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig
from spr.resources.records.ui import SprUIJSONSerializer


class SprResourceConfig(RecordResourceConfig):
    """SprRecord resource config."""

    blueprint_name = "spr"
    url_prefix = "/records/spr/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.spr.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                SprUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
