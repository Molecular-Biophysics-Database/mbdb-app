from bli.records.api import BliDraft, BliRecord
from bli.records.requests.delete_record.types import DeleteRecordRequestType
from bli.records.requests.publish_draft.types import PublishDraftRequestType
from bli.records.requests.resolvers import BliDraftResolver, BliResolver
from bli.resources.files.config import BliFileDraftResourceConfig, BliFileResourceConfig
from bli.resources.files.resource import BliFileDraftResource, BliFileResource
from bli.resources.records.config import BliResourceConfig
from bli.resources.records.resource import BliResource
from bli.services.files.config import BliFileDraftServiceConfig, BliFileServiceConfig
from bli.services.files.service import BliFileDraftService, BliFileService
from bli.services.records.config import BliServiceConfig
from bli.services.records.service import BliService
from oarepo_runtime.records.entity_resolvers import UserResolver

BLI_RECORD_RESOURCE_CONFIG = BliResourceConfig


BLI_RECORD_RESOURCE_CLASS = BliResource


BLI_RECORD_SERVICE_CONFIG = BliServiceConfig


BLI_RECORD_SERVICE_CLASS = BliService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    BliResolver(record_cls=BliRecord, service_id="bli", type_key="bli"),
    BliDraftResolver(record_cls=BliDraft, service_id="bli", type_key="bli_draft"),
]


BLI_FILES_RESOURCE_CONFIG = BliFileResourceConfig


BLI_FILES_RESOURCE_CLASS = BliFileResource


BLI_FILES_SERVICE_CONFIG = BliFileServiceConfig


BLI_FILES_SERVICE_CLASS = BliFileService


BLI_DRAFT_FILES_RESOURCE_CONFIG = BliFileDraftResourceConfig


BLI_DRAFT_FILES_RESOURCE_CLASS = BliFileDraftResource


BLI_DRAFT_FILES_SERVICE_CONFIG = BliFileDraftServiceConfig


BLI_DRAFT_FILES_SERVICE_CLASS = BliFileDraftService
