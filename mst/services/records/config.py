from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from oarepo_communities.services.components.default_workflow import (
    CommunityDefaultWorkflowComponent,
)
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_communities.services.links import CommunitiesLinks
from oarepo_doi.services.components import DoiComponent
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import CustomFieldsComponent, OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
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

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        AuthorityComponent,
        DoiComponent,
        CommunityDefaultWorkflowComponent,
        #CommunityInclusionComponent,
        OwnersComponent,
        DraftFilesComponent,
        CustomFieldsComponent,
        FilesComponent,
        WorkflowComponent,
    ]

    model = "mst"
    draft_cls = MstDraft
    search_drafts = MstSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/mst/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink("{+api}/records/mst/{id}/draft"),
            "edit_html": RecordLink("{+ui}/mst/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/mst/{id}/files"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/mst/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/mst/{id}/latest"),
            "publish": RecordLink("{+api}/records/mst/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/mst/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/mst/{id}/requests"),
                else_=RecordLink("{+api}/records/mst/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/mst/{id}"),
                else_=RecordLink("{+api}/records/mst/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/mst/{id}"),
                else_=RecordLink("{+ui}/mst/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/records/mst/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/mst/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/mst/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/mst/{id}/versions{?args*}"),
        }
