from invenio_drafts_resources.services import RecordService

from common.services.records.service import AddWorkflowServiceMixin


class ItcService(AddWorkflowServiceMixin, RecordService):
    """ItcRecord service."""
