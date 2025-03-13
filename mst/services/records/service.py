from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class MstService(AddWorkflowServiceMixin, SearchAllRecordsService):
    """MstRecord service."""
