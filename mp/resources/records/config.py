import importlib_metadata
from flask_resources import ResponseHandler
from oarepo_runtime.resources.config import BaseRecordResourceConfig

from mp.resources.records.ui import MpUIJSONSerializer


class MpResourceConfig(BaseRecordResourceConfig):
    """MpRecord resource config."""

    blueprint_name = "mp"
    url_prefix = "/records/mp/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.mp.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(MpUIJSONSerializer()),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }

    @property
    def error_handlers(self):
        entrypoint_error_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.mp_record.error_handlers"
        ):
            entrypoint_error_handlers.update(x.load())
        return {**super().error_handlers, **entrypoint_error_handlers}
