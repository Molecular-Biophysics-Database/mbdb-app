from invenio_records_resources.services import (
    FileLink,
    FileServiceConfig,
    LinksTemplate,
    RecordLink,
)
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_file_permission,
    has_permission_file_service,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from itc.records.api import ItcDraft, ItcRecord
from itc.services.files.schema import ItcFileSchema
from itc.services.records.permissions import ItcPermissionPolicy


class ItcFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """ItcRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/itc/<pid_value>"

    base_permission_policy_cls = ItcPermissionPolicy

    file_schema = ItcFileSchema

    record_cls = ItcRecord

    service_id = "itc_file"
    indexer_queue_name = "itc_file"

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "itc"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/itc/{id}/files",
                when=has_permission_file_service("list_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def file_links_item(self):
        try:
            supercls_links = super().file_links_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "commit": FileLink(
                "{+api}/records/itc/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/itc/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/itc/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/itc/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}


class ItcFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """ItcDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/itc/<pid_value>/draft"

    file_schema = ItcFileSchema

    record_cls = ItcDraft

    service_id = "itc_file_draft"
    indexer_queue_name = "itc_file_draft"

    search_item_links_template = LinksTemplate
    permission_action_prefix = "draft_"

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "itc"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/itc/{id}/draft/files",
                when=has_file_permission("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def file_links_item(self):
        try:
            supercls_links = super().file_links_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "commit": FileLink(
                "{+api}/records/itc/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/itc/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/itc/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/itc/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}
