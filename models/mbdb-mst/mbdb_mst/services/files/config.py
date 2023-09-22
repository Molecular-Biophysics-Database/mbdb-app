from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin

from mbdb_mst.records.api import MbdbMstDraft, MbdbMstRecord
from mbdb_mst.services.files.permissions import MbdbMstFileDraftPermissionPolicy
from mbdb_mst.services.files.schema import MbdbMstFileSchema
from mbdb_mst.services.records.permissions import MbdbMstPermissionPolicy


class MbdbMstFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbMstRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-mst/<pid_value>"

    base_permission_policy_cls = MbdbMstPermissionPolicy

    schema = MbdbMstFileSchema

    record_cls = MbdbMstRecord

    service_id = "mbdb_mst_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_mst"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-mst/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-mst/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-mst/{id}/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-mst/{id}/files/{key}"),
        }


class MbdbMstFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MbdbMstDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/mbdb-mst/<pid_value>/draft"

    base_permission_policy_cls = MbdbMstFileDraftPermissionPolicy

    schema = MbdbMstFileSchema

    record_cls = MbdbMstDraft

    service_id = "mbdb_mst_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mbdb_mst"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/mbdb-mst/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/mbdb-mst/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/mbdb-mst/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/mbdb-mst/{id}/draft/files/{key}"),
        }
