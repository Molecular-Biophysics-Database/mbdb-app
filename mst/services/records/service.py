from invenio_drafts_resources.services import RecordService

from common.services.records.service import AddWorkflowServiceMixin


class MstService(AddWorkflowServiceMixin, RecordService):
    """MstRecord service."""
