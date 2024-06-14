from oarepo_requests.resolvers.ui import (
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService

from mst.files.api import MstFileDraft
from mst.files.requests.resolvers import MstFileDraftResolver
from mst.records.api import MstDraft, MstRecord
from mst.records.requests.resolvers import MstDraftResolver, MstResolver
from mst.resources.files.config import MstFileDraftResourceConfig, MstFileResourceConfig
from mst.resources.files.resource import MstFileDraftResource, MstFileResource
from mst.resources.records.config import MstResourceConfig
from mst.resources.records.resource import MstResource
from mst.services.files.config import MstFileDraftServiceConfig, MstFileServiceConfig
from mst.services.files.service import MstFileDraftService, MstFileService
from mst.services.records.config import MstServiceConfig
from mst.services.records.service import MstService

MST_RECORD_RESOURCE_CONFIG = MstResourceConfig


MST_RECORD_RESOURCE_CLASS = MstResource


MST_RECORD_SERVICE_CONFIG = MstServiceConfig


MST_RECORD_SERVICE_CLASS = MstService


MST_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


MST_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_ENTITY_RESOLVERS = [
    MstResolver(record_cls=MstRecord, service_id="mst", type_key="mst"),
    MstDraftResolver(record_cls=MstDraft, service_id="mst", type_key="mst_draft"),
    MstFileDraftResolver(
        record_cls=MstFileDraft, service_id="mst_file_draft", type_key="mst_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "mst": RecordEntityReferenceUIResolver("mst"),
    "mst_draft": RecordEntityDraftReferenceUIResolver("mst_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = []


MST_FILES_RESOURCE_CONFIG = MstFileResourceConfig


MST_FILES_RESOURCE_CLASS = MstFileResource


MST_FILES_SERVICE_CONFIG = MstFileServiceConfig


MST_FILES_SERVICE_CLASS = MstFileService


MST_DRAFT_FILES_RESOURCE_CONFIG = MstFileDraftResourceConfig


MST_DRAFT_FILES_RESOURCE_CLASS = MstFileDraftResource


MST_DRAFT_FILES_SERVICE_CONFIG = MstFileDraftServiceConfig


MST_DRAFT_FILES_SERVICE_CLASS = MstFileDraftService
