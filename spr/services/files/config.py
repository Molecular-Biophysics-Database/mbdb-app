from invenio_records_resources.services import (
    FileLink,
    FileServiceConfig,
    LinksTemplate,
    RecordLink,
)
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_file_permission,
    has_permission_file_service,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from spr.records.api import SprDraft, SprRecord
from spr.services.files.schema import SprFileSchema
from spr.services.records.permissions import SprPermissionPolicy


class SprFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """SprRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/spr/<pid_value>"

    base_permission_policy_cls = SprPermissionPolicy

    schema = SprFileSchema

    record_cls = SprRecord

    service_id = "spr_file"

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "spr"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/records/spr/{id}/files",
                when=has_permission_file_service("list_files"),
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/records/spr/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/spr/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/spr/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/spr/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }


class SprFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """SprDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/records/spr/<pid_value>/draft"

    schema = SprFileSchema

    record_cls = SprDraft

    service_id = "spr_file_draft"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "spr"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/records/spr/{id}/draft/files",
                when=has_file_permission("list_files"),
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/records/spr/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/records/spr/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/spr/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/records/spr/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
