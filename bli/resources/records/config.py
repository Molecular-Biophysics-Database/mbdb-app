import importlib_metadata
from bli.resources.records.ui import BliUIJSONSerializer
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig


class BliResourceConfig(RecordResourceConfig):
    """BliRecord resource config."""

    blueprint_name = "bli"
    url_prefix = "/records/bli/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.bli.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                BliUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
