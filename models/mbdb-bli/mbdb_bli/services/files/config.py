from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_bli.records.api import MbdbBliRecord
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
