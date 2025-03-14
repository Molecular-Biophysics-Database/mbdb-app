from invenio_rdm_records.services.services import RDMRecordService
from oarepo_runtime.services.service import SearchAllRecordsService

from common.services.records.service import AddWorkflowServiceMixin


class SprService(AddWorkflowServiceMixin, RDMRecordService, SearchAllRecordsService):
    """SprRecord service."""
