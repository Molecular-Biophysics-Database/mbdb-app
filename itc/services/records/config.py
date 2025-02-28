from invenio_rdm_records.services.config import RDMRecordServiceConfig
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
from oarepo_runtime.services.records import pagination_links_html
from oarepo_vocabularies.authorities.components import AuthorityComponent
from oarepo_workflows.services.components.workflow import WorkflowComponent

from itc.records.api import ItcDraft, ItcRecord
from itc.services.records.permissions import ItcPermissionPolicy
from itc.services.records.results import ItcRecordItem, ItcRecordList
from itc.services.records.schema import ItcSchema
from itc.services.records.search import ItcDraftSearchOptions, ItcSearchOptions


class ItcServiceConfig(PermissionsPresetsConfigMixin, RDMRecordServiceConfig):
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

    search_item_links_template = LinksTemplate
    draft_cls = ItcDraft
    search_drafts = ItcDraftSearchOptions

    @property
    def components(self):
        return process_service_configs(
            self,
            AuthorityComponent,
            DoiComponent,
            CommunityDefaultWorkflowComponent,
            #CommunityInclusionComponent,
            CustomFieldsComponent,
            WorkflowComponent,
        )

    model = "itc"

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/itc/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/records/itc/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/itc/{id}/edit", when=has_draft() & has_permission("update")
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/records/itc/{id}/files",
                    when=has_file_permission("list_files"),
                ),
                else_=RecordLink(
                    "{+api}/records/itc/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/records/itc/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/itc/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/records/itc/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/records/itc/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/itc/{id}/requests"),
                else_=RecordLink("{+api}/records/itc/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/itc/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/itc/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/itc/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/itc/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/records/itc/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/itc/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/itc/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/itc/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/itc/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/itc/{?args*}"),
            **pagination_links_html("{+ui}/records/itc/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/itc/{?args*}"),
            **pagination_links_html("{+ui}/user/records/itc/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/itc/{id}/versions{?args*}"),
        }
