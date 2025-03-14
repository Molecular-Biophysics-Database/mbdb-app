from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class MpService(AddWorkflowServiceMixin, SearchAllRecordsService):
    """MpRecord service."""
