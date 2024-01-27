from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from mst.records.api import MstDraft, MstRecord
from mst.services.files.permissions import MstFileDraftPermissionPolicy
from mst.services.files.schema import MstFileSchema
from mst.services.records.permissions import MstPermissionPolicy
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.results import RecordList


class MstFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MstRecord service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/mst/<pid_value>"

    base_permission_policy_cls = MstPermissionPolicy

    schema = MstFileSchema

    record_cls = MstRecord

    service_id = "mst_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mst"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/mst/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/mst/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/records/mst/{id}/files/{key}/content"),
            "self": FileLink("{+api}/records/mst/{id}/files/{key}"),
        }


class MstFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """MstDraft service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/mst/<pid_value>/draft"

    base_permission_policy_cls = MstFileDraftPermissionPolicy

    schema = MstFileSchema

    record_cls = MstDraft

    service_id = "mst_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "mst"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/mst/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/mst/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/records/mst/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/records/mst/{id}/draft/files/{key}"),
        }
