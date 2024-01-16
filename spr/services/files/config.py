from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.results import RecordList
from spr.records.api import SprDraft, SprRecord
from spr.services.files.permissions import SprFileDraftPermissionPolicy
from spr.services.files.schema import SprFileSchema
from spr.services.records.permissions import SprPermissionPolicy


class SprFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """SprRecord service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/spr/<pid_value>"

    base_permission_policy_cls = SprPermissionPolicy

    schema = SprFileSchema

    record_cls = SprRecord

    service_id = "spr_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "spr"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/spr/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/spr/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/records/spr/{id}/files/{key}/content"),
            "self": FileLink("{+api}/records/spr/{id}/files/{key}"),
        }


class SprFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """SprDraft service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/spr/<pid_value>/draft"

    base_permission_policy_cls = SprFileDraftPermissionPolicy

    schema = SprFileSchema

    record_cls = SprDraft

    service_id = "spr_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "spr"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/spr/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/spr/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/records/spr/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/records/spr/{id}/draft/files/{key}"),
        }
