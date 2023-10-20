from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_bli.records.api import MbdbBliDraft, MbdbBliRecord
from mbdb_bli.services.files.permissions import MbdbBliFileDraftPermissionPolicy
from mbdb_bli.services.files.schema import MbdbBliFileSchema
from mbdb_bli.services.records.permissions import MbdbBliPermissionPolicy


class MbdbBliFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbBliRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-bli/<pid_value>"

    base_permission_policy_cls = MbdbBliPermissionPolicy

    schema = MbdbBliFileSchema

    record_cls = MbdbBliRecord

    service_id = "mbdb_bli_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_bli"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-bli/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-bli/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-bli/{id}/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-bli/{id}/files/{key}"),
        }


class MbdbBliFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbBliDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-bli/<pid_value>/draft"

    base_permission_policy_cls = MbdbBliFileDraftPermissionPolicy

    schema = MbdbBliFileSchema

    record_cls = MbdbBliDraft

    service_id = "mbdb_bli_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_bli"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-bli/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-bli/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-bli/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-bli/{id}/draft/files/{key}"),
        }
