from itc.files.api import ItcFileDraft
from itc.files.requests.resolvers import ItcFileDraftResolver
from itc.records.api import ItcDraft, ItcRecord
from itc.records.requests.resolvers import ItcDraftResolver, ItcResolver
from itc.resources.files.config import ItcFileDraftResourceConfig, ItcFileResourceConfig
from itc.resources.files.resource import ItcFileDraftResource, ItcFileResource
from itc.resources.records.config import ItcResourceConfig
from itc.resources.records.resource import ItcResource
from itc.services.files.config import ItcFileDraftServiceConfig, ItcFileServiceConfig
from itc.services.files.service import ItcFileDraftService, ItcFileService
from itc.services.records.config import ItcServiceConfig
from itc.services.records.service import ItcService
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

ITC_RECORD_RESOURCE_CONFIG = ItcResourceConfig


ITC_RECORD_RESOURCE_CLASS = ItcResource


ITC_RECORD_SERVICE_CONFIG = ItcServiceConfig


ITC_RECORD_SERVICE_CLASS = ItcService


ITC_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


ITC_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    GroupResolver(),
    ItcResolver(record_cls=ItcRecord, service_id="itc", type_key="itc"),
    ItcDraftResolver(record_cls=ItcDraft, service_id="itc", type_key="itc_draft"),
    ItcFileDraftResolver(
        record_cls=ItcFileDraft, service_id="itc_file_draft", type_key="itc_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "user": UserEntityReferenceUIResolver("user"),
    "fallback": FallbackEntityReferenceUIResolver("fallback"),
    "group": GroupEntityReferenceUIResolver("group"),
    "itc": RecordEntityReferenceUIResolver("itc"),
    "itc_draft": RecordEntityDraftReferenceUIResolver("itc_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = ["created_by", "receiver", "topic"]


ITC_FILES_RESOURCE_CONFIG = ItcFileResourceConfig


ITC_FILES_RESOURCE_CLASS = ItcFileResource


ITC_FILES_SERVICE_CONFIG = ItcFileServiceConfig


ITC_FILES_SERVICE_CLASS = ItcFileService


ITC_DRAFT_FILES_RESOURCE_CONFIG = ItcFileDraftResourceConfig


ITC_DRAFT_FILES_RESOURCE_CLASS = ItcFileDraftResource


ITC_DRAFT_FILES_SERVICE_CONFIG = ItcFileDraftServiceConfig


ITC_DRAFT_FILES_SERVICE_CLASS = ItcFileDraftService
