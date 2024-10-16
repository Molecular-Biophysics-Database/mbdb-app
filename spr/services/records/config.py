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

from spr.records.api import SprDraft, SprRecord
from spr.services.records.permissions import SprPermissionPolicy
from spr.services.records.results import SprRecordItem, SprRecordList
from spr.services.records.schema import SprSchema
from spr.services.records.search import SprSearchOptions


class SprServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """SprRecord service config."""

    result_item_cls = SprRecordItem

    result_list_cls = SprRecordList

    PERMISSIONS_PRESETS = ["mbdb"]

    url_prefix = "/records/spr/"

    base_permission_policy_cls = SprPermissionPolicy

    schema = SprSchema

    search = SprSearchOptions

    record_cls = SprRecord

    service_id = "spr"

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

    model = "spr"
    draft_cls = SprDraft
    search_drafts = SprSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/spr/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink("{+api}/records/spr/{id}/draft"),
            "edit_html": RecordLink("{+ui}/spr/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/spr/{id}/files"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/spr/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/spr/{id}/latest"),
            "publish": RecordLink("{+api}/records/spr/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/spr/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/spr/{id}/requests"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/spr/{id}"),
                else_=RecordLink("{+api}/records/spr/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/spr/{id}"),
                else_=RecordLink("{+ui}/spr/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/records/spr/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/spr/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/spr/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/spr/{id}/versions{?args*}"),
        }
