from oarepo_requests.resolvers.ui import (
    draft_record_entity_reference_ui_resolver,
    record_entity_reference_ui_resolver,
    user_entity_reference_ui_resolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_runtime.records.entity_resolvers import UserResolver

from bli.files.api import BliFileDraft
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
from common.requests.delete_record.types import DeleteRecordRequestType
from common.requests.publish_draft.types import PublishDraftRequestType

BLI_RECORD_RESOURCE_CONFIG = BliResourceConfig


BLI_RECORD_RESOURCE_CLASS = BliResource


BLI_RECORD_SERVICE_CONFIG = BliServiceConfig


BLI_RECORD_SERVICE_CLASS = BliService


BLI_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


BLI_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    BliResolver(record_cls=BliRecord, service_id="bli", type_key="bli"),
    BliDraftResolver(record_cls=BliDraft, service_id="bli", type_key="bli_draft"),
    BliFileDraftResolver(
        record_cls=BliFileDraft, service_id="bli_file_draft", type_key="bli_file_draft"
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "user": user_entity_reference_ui_resolver,
    "bli": record_entity_reference_ui_resolver,
    "bli_draft": draft_record_entity_reference_ui_resolver,
}


BLI_FILES_RESOURCE_CONFIG = BliFileResourceConfig


BLI_FILES_RESOURCE_CLASS = BliFileResource


BLI_FILES_SERVICE_CONFIG = BliFileServiceConfig


BLI_FILES_SERVICE_CLASS = BliFileService


BLI_DRAFT_FILES_RESOURCE_CONFIG = BliFileDraftResourceConfig


BLI_DRAFT_FILES_RESOURCE_CLASS = BliFileDraftResource


BLI_DRAFT_FILES_SERVICE_CONFIG = BliFileDraftServiceConfig


BLI_DRAFT_FILES_SERVICE_CLASS = BliFileDraftService
