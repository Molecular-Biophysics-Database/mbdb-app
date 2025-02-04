from invenio_rdm_records.services.services import RDMRecordService

from common.services.records.service import AddWorkflowServiceMixin

class SprService(AddWorkflowServiceMixin, RDMRecordService):
    """SprRecord service."""