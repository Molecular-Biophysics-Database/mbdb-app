from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_spr.records.api import MbdbSprRecord
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
            "self": RecordLink("{self.url_prefix}{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{self.url_prefix}{id}/files/{key}/commit"),
            "content": FileLink("{self.url_prefix}{id}/files/{key}/content"),
            "self": FileLink("{self.url_prefix}{id}/files/{key}"),
        }
