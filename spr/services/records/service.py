from invenio_drafts_resources.services import RecordService

from common.services.records.service import AddWorkflowServiceMixin


class SprService(AddWorkflowServiceMixin, RecordService):
    """SprRecord service."""
