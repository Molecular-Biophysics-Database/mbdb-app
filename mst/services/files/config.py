from invenio_records_resources.services import FileLink, RecordLink
from oarepo_runtime.services.components import CustomFieldsComponent

from common.services.files import MstFileServiceConfigWithProcessors
from mst.records.api import MstDraft, MstRecord
from mst.services.files.schema import MstFileSchema
from mst.services.records.permissions import MstPermissionPolicy


class MstFileServiceConfig(MstFileServiceConfigWithProcessors):
    """MstRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/mst/<pid_value>"

    base_permission_policy_cls = MstPermissionPolicy

    schema = MstFileSchema

    record_cls = MstRecord

    service_id = "mst_file"

    components = [*MstFileServiceConfigWithProcessors.components, CustomFieldsComponent]

    model = "mst"
    allowed_mimetypes = []
    allowed_extensions = []
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
            "preview": FileLink("{+ui}/mst/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/records/mst/{id}/files/{key}"),
        }


class MstFileDraftServiceConfig(MstFileServiceConfigWithProcessors):
    """MstDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/mst/<pid_value>/draft"

    schema = MstFileSchema

    record_cls = MstDraft

    service_id = "mst_file_draft"

    components = [*MstFileServiceConfigWithProcessors.components, CustomFieldsComponent]

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
            "preview": FileLink("{+ui}/mst/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/records/mst/{id}/draft/files/{key}"),
        }
