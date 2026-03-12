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

from mp.records.api import MpDraft, MpRecord
from mp.services.files.schema import MpFileSchema
from mp.services.records.permissions import MpPermissionPolicy


class MpFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MpRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/mp/<pid_value>"

    base_permission_policy_cls = MpPermissionPolicy

    schema = MpFileSchema

    record_cls = MpRecord

    service_id = "mp_file"
    indexer_queue_name = "mp_file"
    max_files_count = 255

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "mp"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/mp/{id}/files",
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
                "{+api}/records/mp/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/mp/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/mp/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/mp/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}


class MpFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MpDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/mp/<pid_value>/draft"

    schema = MpFileSchema

    record_cls = MpDraft

    service_id = "mp_file_draft"
    indexer_queue_name = "mp_file_draft"
    max_files_count = 255

    search_item_links_template = LinksTemplate
    permission_action_prefix = "draft_"

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "mp"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/mp/{id}/draft/files",
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
                "{+api}/records/mp/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/mp/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/mp/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/mp/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}
