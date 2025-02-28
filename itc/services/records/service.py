from invenio_rdm_records.services.services import RDMRecordService

from common.services.records.service import AddWorkflowServiceMixin


class ItcService(AddWorkflowServiceMixin, RDMRecordService):
    """ItcRecord service."""
