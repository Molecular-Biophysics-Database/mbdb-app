from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_spr.records.api import MbdbSprDraft, MbdbSprRecord
from mbdb_spr.services.files.permissions import MbdbSprFileDraftPermissionPolicy
from mbdb_spr.services.files.schema import MbdbSprFileSchema
from mbdb_spr.services.records.permissions import MbdbSprPermissionPolicy


class MbdbSprFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbSprRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-spr/<pid_value>"

    base_permission_policy_cls = MbdbSprPermissionPolicy

    schema = MbdbSprFileSchema

    record_cls = MbdbSprRecord

    service_id = "mbdb_spr_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_spr"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-spr/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-spr/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-spr/{id}/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-spr/{id}/files/{key}"),
        }


class MbdbSprFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbSprDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-spr/<pid_value>/draft"

    base_permission_policy_cls = MbdbSprFileDraftPermissionPolicy

    schema = MbdbSprFileSchema

    record_cls = MbdbSprDraft

    service_id = "mbdb_spr_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_spr"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-spr/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-spr/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-spr/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-spr/{id}/draft/files/{key}"),
        }
