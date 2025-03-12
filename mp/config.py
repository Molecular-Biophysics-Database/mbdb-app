from oarepo_requests.resolvers.ui import (
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.resources.draft.types.resource import DraftRequestTypesResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_requests.services.draft.types.service import DraftRecordRequestTypesService

from mp.files.api import MpFile, MpFileDraft
from mp.files.requests.resolvers import MpFileDraftResolver
from mp.records.api import MpDraft, MpRecord
from mp.records.requests.resolvers import MpDraftResolver, MpResolver
from mp.resources.files.config import MpFileDraftResourceConfig, MpFileResourceConfig
from mp.resources.files.resource import MpFileDraftResource, MpFileResource
from mp.resources.records.config import MpResourceConfig
from mp.resources.records.resource import MpResource
from mp.services.files.config import MpFileDraftServiceConfig, MpFileServiceConfig
from mp.services.files.service import MpFileDraftService, MpFileService
from mp.services.records.config import MpServiceConfig
from mp.services.records.service import MpService

MP_RECORD_RESOURCE_CONFIG = MpResourceConfig


MP_RECORD_RESOURCE_CLASS = MpResource


MP_RECORD_SERVICE_CONFIG = MpServiceConfig


MP_RECORD_SERVICE_CLASS = MpService


OAREPO_PRIMARY_RECORD_SERVICE = {
    MpRecord: "mp",
    MpDraft: "mp",
    MpFile: "mp_file",
    MpFileDraft: "mp_file_draft",
}


MP_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


MP_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


MP_ENTITY_RESOLVERS = [
    MpResolver(record_cls=MpRecord, service_id="mp", type_key="mp"),
    MpDraftResolver(record_cls=MpDraft, service_id="mp", type_key="mp_draft"),
    MpFileDraftResolver(
        record_cls=MpFileDraft, service_id="mp_file_draft", type_key="mp_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "mp": RecordEntityReferenceUIResolver("mp"),
    "mp_draft": RecordEntityDraftReferenceUIResolver("mp_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = []


MP_REQUEST_TYPES_RESOURCE_CLASS = DraftRequestTypesResource


MP_REQUEST_TYPES_SERVICE_CLASS = DraftRecordRequestTypesService


MP_FILES_RESOURCE_CONFIG = MpFileResourceConfig


MP_FILES_RESOURCE_CLASS = MpFileResource


MP_FILES_SERVICE_CONFIG = MpFileServiceConfig


MP_FILES_SERVICE_CLASS = MpFileService


MP_DRAFT_FILES_RESOURCE_CONFIG = MpFileDraftResourceConfig


MP_DRAFT_FILES_RESOURCE_CLASS = MpFileDraftResource


MP_DRAFT_FILES_SERVICE_CONFIG = MpFileDraftServiceConfig


MP_DRAFT_FILES_SERVICE_CLASS = MpFileDraftService
