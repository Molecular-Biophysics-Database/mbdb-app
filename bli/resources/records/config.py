import importlib_metadata
from flask_resources import ResponseHandler
from oarepo_runtime.resources.config import BaseRecordResourceConfig

from bli.resources.records.ui import BliUIJSONSerializer


class BliResourceConfig(BaseRecordResourceConfig):
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

    @property
    def error_handlers(self):
        entrypoint_error_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.bli_record.error_handlers"
        ):
            entrypoint_error_handlers.update(x.load())
        return {**super().error_handlers, **entrypoint_error_handlers}
