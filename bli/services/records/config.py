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

from bli.records.api import BliDraft, BliRecord
from bli.services.records.permissions import BliPermissionPolicy
from bli.services.records.results import BliRecordItem, BliRecordList
from bli.services.records.schema import BliSchema
from bli.services.records.search import BliSearchOptions


class BliServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """BliRecord service config."""

    result_item_cls = BliRecordItem

    result_list_cls = BliRecordList

    PERMISSIONS_PRESETS = ["mbdb"]

    url_prefix = "/records/bli/"

    base_permission_policy_cls = BliPermissionPolicy

    schema = BliSchema

    search = BliSearchOptions

    record_cls = BliRecord

    service_id = "bli"

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

    model = "bli"
    draft_cls = BliDraft
    search_drafts = BliSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/bli/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/bli/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink("{+api}/records/bli/{id}/draft"),
            "edit_html": RecordLink("{+ui}/bli/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/bli/{id}/files"),
                else_=RecordLink("{+api}/records/bli/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/bli/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/bli/{id}/latest"),
            "publish": RecordLink("{+api}/records/bli/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/bli/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/bli/{id}/requests"),
                else_=RecordLink("{+api}/records/bli/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/bli/{id}"),
                else_=RecordLink("{+api}/records/bli/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/bli/{id}"),
                else_=RecordLink("{+ui}/bli/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/records/bli/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/bli/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/bli/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/bli/{id}/versions{?args*}"),
        }
