from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from oarepo_runtime.services.components import CustomFieldsComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from itc.records.api import ItcDraft, ItcRecord
from itc.services.files.schema import ItcFileSchema
from itc.services.records.permissions import ItcPermissionPolicy


class ItcFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """ItcRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/itc/<pid_value>"

    base_permission_policy_cls = ItcPermissionPolicy

    schema = ItcFileSchema

    record_cls = ItcRecord

    service_id = "itc_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "itc"
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/itc/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/itc/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/records/itc/{id}/files/{key}/content"),
            "preview": FileLink("{+ui}/itc/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/records/itc/{id}/files/{key}"),
        }


class ItcFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """ItcDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/records/itc/<pid_value>/draft"

    schema = ItcFileSchema

    record_cls = ItcDraft

    service_id = "itc_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "itc"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/records/itc/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/records/itc/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/records/itc/{id}/draft/files/{key}/content"),
            "preview": FileLink("{+ui}/itc/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/records/itc/{id}/draft/files/{key}"),
        }
