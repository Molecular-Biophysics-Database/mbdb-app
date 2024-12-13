from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    LinksTemplate,
    RecordLink,
    pagination_links,
)
from oarepo_communities.services.components.default_workflow import (
    CommunityDefaultWorkflowComponent,
)
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_communities.services.links import CommunitiesLinks
from oarepo_doi.services.components import DoiComponent
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    OwnersComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_draft,
    has_file_permission,
    has_permission,
    has_published_record,
    is_published_record,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.records import pagination_links_html
from oarepo_vocabularies.authorities.components import AuthorityComponent
from oarepo_workflows.services.components.workflow import WorkflowComponent

from mst.records.api import MstDraft, MstRecord
from mst.services.records.permissions import MstPermissionPolicy
from mst.services.records.results import MstRecordItem, MstRecordList
from mst.services.records.schema import MstSchema
from mst.services.records.search import MstSearchOptions


class MstServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """MstRecord service config."""

    result_item_cls = MstRecordItem

    result_list_cls = MstRecordList

    PERMISSIONS_PRESETS = ["mbdb"]

    url_prefix = "/records/mst/"

    base_permission_policy_cls = MstPermissionPolicy

    schema = MstSchema

    search = MstSearchOptions

    record_cls = MstRecord

    service_id = "mst"

    search_item_links_template = LinksTemplate
    draft_cls = MstDraft
    search_drafts = MstSearchOptions

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [
            AuthorityComponent,
            DoiComponent,
            CommunityDefaultWorkflowComponent,
            #CommunityInclusionComponent,
            OwnersComponent,
            FilesComponent,
            DraftFilesComponent,
            CustomFieldsComponent,
            WorkflowComponent,
        ]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "mst"

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mst/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/records/mst/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/mst/{id}/edit", when=has_draft() & has_permission("update")
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/records/mst/{id}/files",
                    when=has_file_permission("list_files"),
                ),
                else_=RecordLink(
                    "{+api}/records/mst/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/records/mst/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/mst/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/records/mst/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/records/mst/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mst/{id}/requests"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mst/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/mst/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/mst/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/mst/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/records/mst/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mst/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/mst/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/mst/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/mst/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/mst/{?args*}"),
            **pagination_links_html("{+ui}/records/mst/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/mst/{?args*}"),
            **pagination_links_html("{+ui}/user/records/mst/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/mst/{id}/versions{?args*}"),
        }
