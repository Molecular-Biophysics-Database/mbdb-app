from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class SprService(AddWorkflowServiceMixin, SearchAllRecordsService):
    """SprRecord service."""
