from invenio_rdm_records.services.services import RDMRecordService
from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class ItcService(AddWorkflowServiceMixin, RDMRecordService, SearchAllRecordsService):
    """ItcRecord service."""
