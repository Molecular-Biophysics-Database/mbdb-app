from invenio_records_resources.services import FileLink, LinksTemplate, RecordLink
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_file_permission,
    has_permission_file_service,
)

from common.services.files.mst_metadata_extraction import (
    MstFileServiceConfigWithProcessors,
)
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
    indexer_queue_name = "mst_file"

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "mst"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/mst/{id}/files",
                when=has_permission_file_service("list_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def file_links_item(self):
        try:
            supercls_links = super().file_links_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "commit": FileLink(
                "{+api}/records/mst/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/mst/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/mst/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/mst/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}


class MstFileDraftServiceConfig(MstFileServiceConfigWithProcessors):
    """MstDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/mst/<pid_value>/draft"

    schema = MstFileSchema

    record_cls = MstDraft

    service_id = "mst_file_draft"
    indexer_queue_name = "mst_file_draft"

    search_item_links_template = LinksTemplate
    permission_action_prefix = "draft_"

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent)

    model = "mst"

    @property
    def file_links_list(self):
        try:
            supercls_links = super().file_links_list
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "self": RecordLink(
                "{+api}/records/mst/{id}/draft/files",
                when=has_file_permission("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def file_links_item(self):
        try:
            supercls_links = super().file_links_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "commit": FileLink(
                "{+api}/records/mst/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/mst/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/mst/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/mst/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
        return {k: v for k, v in links.items() if v is not None}
