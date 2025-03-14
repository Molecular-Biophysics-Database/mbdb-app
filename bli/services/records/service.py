from invenio_rdm_records.services.services import RDMRecordService
from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class BliService(AddWorkflowServiceMixin, RDMRecordService, SearchAllRecordsService):
    """BliRecord service."""
