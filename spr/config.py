from oarepo_requests.resolvers.ui import (
    FallbackEntityReferenceUIResolver,
    GroupEntityReferenceUIResolver,
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
    UserEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_runtime.records.entity_resolvers import GroupResolver, UserResolver

from common.requests.delete_record.types import DeleteRecordRequestType
from common.requests.publish_draft.types import PublishDraftRequestType
from spr.files.api import SprFileDraft
from spr.files.requests.resolvers import SprFileDraftResolver
from spr.records.api import SprDraft, SprRecord
from spr.records.requests.resolvers import SprDraftResolver, SprResolver
from spr.resources.files.config import SprFileDraftResourceConfig, SprFileResourceConfig
from spr.resources.files.resource import SprFileDraftResource, SprFileResource
from spr.resources.records.config import SprResourceConfig
from spr.resources.records.resource import SprResource
from spr.services.files.config import SprFileDraftServiceConfig, SprFileServiceConfig
from spr.services.files.service import SprFileDraftService, SprFileService
from spr.services.records.config import SprServiceConfig
from spr.services.records.service import SprService

SPR_RECORD_RESOURCE_CONFIG = SprResourceConfig


SPR_RECORD_RESOURCE_CLASS = SprResource


SPR_RECORD_SERVICE_CONFIG = SprServiceConfig


SPR_RECORD_SERVICE_CLASS = SprService


SPR_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


SPR_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    GroupResolver(),
    SprResolver(record_cls=SprRecord, service_id="spr", type_key="spr"),
    SprDraftResolver(record_cls=SprDraft, service_id="spr", type_key="spr_draft"),
    SprFileDraftResolver(
        record_cls=SprFileDraft, service_id="spr_file_draft", type_key="spr_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "user": UserEntityReferenceUIResolver("user"),
    "fallback": FallbackEntityReferenceUIResolver("fallback"),
    "group": GroupEntityReferenceUIResolver("group"),
    "spr": RecordEntityReferenceUIResolver("spr"),
    "spr_draft": RecordEntityDraftReferenceUIResolver("spr_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = ["created_by", "receiver", "topic"]


SPR_FILES_RESOURCE_CONFIG = SprFileResourceConfig


SPR_FILES_RESOURCE_CLASS = SprFileResource


SPR_FILES_SERVICE_CONFIG = SprFileServiceConfig


SPR_FILES_SERVICE_CLASS = SprFileService


SPR_DRAFT_FILES_RESOURCE_CONFIG = SprFileDraftResourceConfig


SPR_DRAFT_FILES_RESOURCE_CLASS = SprFileDraftResource


SPR_DRAFT_FILES_SERVICE_CONFIG = SprFileDraftServiceConfig


SPR_DRAFT_FILES_SERVICE_CLASS = SprFileDraftService
