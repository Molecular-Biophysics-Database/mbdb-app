from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from bli.records.api import BliDraft, BliRecord
from bli.services.files.schema import BliFileSchema
from bli.services.records.permissions import BliPermissionPolicy


class BliFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """BliRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/bli/<pid_value>"

    base_permission_policy_cls = BliPermissionPolicy

    schema = BliFileSchema

    record_cls = BliRecord

    service_id = "bli_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "bli"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/bli/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/bli/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/records/bli/{id}/files/{key}/content"),
            "preview": FileLink("{+ui}/bli/files/{key}/preview"),
            "self": FileLink("{+api}/records/bli/{id}/files/{key}"),
        }


class BliFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """BliDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/bli/<pid_value>/draft"

    schema = BliFileSchema

    record_cls = BliDraft

    service_id = "bli_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "bli"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/bli/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/bli/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/records/bli/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/records/bli/{id}/draft/files/{key}"),
        }
