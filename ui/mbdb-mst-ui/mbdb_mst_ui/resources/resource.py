from oarepo_ui.resources.resource import RecordsUIResource

from flask import g, request
from flask_resources import (
    resource_requestctx,
)
from invenio_records_resources.resources.records.resource import (
    request_read_args,
    request_view_args,
)

from oarepo_ui.resources.catalog import get_jinja_template
from oarepo_ui.proxies import current_oarepo_ui


class MbdbMstUIResource(RecordsUIResource):
    def _get_record(self, resource_requestctx, allow_draft=False):
        try:
            return super()._get_record(resource_requestctx, allow_draft=False)
        except:
            return super()._get_record(resource_requestctx, allow_draft=True)
