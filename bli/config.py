from oarepo_requests.resolvers.ui import (
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.resources.draft.types.resource import DraftRequestTypesResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_requests.services.draft.types.service import DraftRecordRequestTypesService

from bli.files.api import BliFile, BliFileDraft
from bli.files.requests.resolvers import BliFileDraftResolver
from bli.records.api import BliDraft, BliRecord
from bli.records.requests.resolvers import BliDraftResolver, BliResolver
from bli.resources.files.config import BliFileDraftResourceConfig, BliFileResourceConfig
from bli.resources.files.resource import BliFileDraftResource, BliFileResource
from bli.resources.records.config import BliResourceConfig
from bli.resources.records.resource import BliResource
from bli.services.files.config import BliFileDraftServiceConfig, BliFileServiceConfig
from bli.services.files.service import BliFileDraftService, BliFileService
from bli.services.records.config import BliServiceConfig
from bli.services.records.service import BliService

BLI_RECORD_RESOURCE_CONFIG = BliResourceConfig


BLI_RECORD_RESOURCE_CLASS = BliResource


BLI_RECORD_SERVICE_CONFIG = BliServiceConfig


BLI_RECORD_SERVICE_CLASS = BliService


OAREPO_PRIMARY_RECORD_SERVICE = {
    BliRecord: "bli",
    BliDraft: "bli",
    BliFile: "bli_file",
    BliFileDraft: "bli_file_draft",
}


BLI_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


BLI_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


BLI_ENTITY_RESOLVERS = [
    BliResolver(record_cls=BliRecord, service_id="bli", type_key="bli"),
    BliDraftResolver(record_cls=BliDraft, service_id="bli", type_key="bli_draft"),
    BliFileDraftResolver(
        record_cls=BliFileDraft, service_id="bli_file_draft", type_key="bli_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "bli": RecordEntityReferenceUIResolver("bli"),
    "bli_draft": RecordEntityDraftReferenceUIResolver("bli_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = []


BLI_REQUEST_TYPES_RESOURCE_CLASS = DraftRequestTypesResource


BLI_REQUEST_TYPES_SERVICE_CLASS = DraftRecordRequestTypesService


BLI_FILES_RESOURCE_CONFIG = BliFileResourceConfig


BLI_FILES_RESOURCE_CLASS = BliFileResource


BLI_FILES_SERVICE_CONFIG = BliFileServiceConfig


BLI_FILES_SERVICE_CLASS = BliFileService


BLI_DRAFT_FILES_RESOURCE_CONFIG = BliFileDraftResourceConfig


BLI_DRAFT_FILES_RESOURCE_CLASS = BliFileDraftResource


BLI_DRAFT_FILES_SERVICE_CONFIG = BliFileDraftServiceConfig


BLI_DRAFT_FILES_SERVICE_CLASS = BliFileDraftService
