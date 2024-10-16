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

from itc.records.api import ItcDraft, ItcRecord
from itc.services.records.permissions import ItcPermissionPolicy
from itc.services.records.results import ItcRecordItem, ItcRecordList
from itc.services.records.schema import ItcSchema
from itc.services.records.search import ItcSearchOptions


class ItcServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """ItcRecord service config."""

    result_item_cls = ItcRecordItem

    result_list_cls = ItcRecordList

    PERMISSIONS_PRESETS = ["mbdb"]

    url_prefix = "/records/itc/"

    base_permission_policy_cls = ItcPermissionPolicy

    schema = ItcSchema

    search = ItcSearchOptions

    record_cls = ItcRecord

    service_id = "itc"

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

    model = "itc"
    draft_cls = ItcDraft
    search_drafts = ItcSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink("{+api}/records/itc/{id}/draft"),
            "edit_html": RecordLink("{+ui}/itc/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}/files"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/itc/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/itc/{id}/latest"),
            "publish": RecordLink("{+api}/records/itc/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/itc/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}/requests"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/records/itc/{id}"),
                else_=RecordLink("{+api}/records/itc/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/itc/{id}"),
                else_=RecordLink("{+ui}/itc/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/records/itc/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/itc/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/itc/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/itc/{id}/versions{?args*}"),
        }
