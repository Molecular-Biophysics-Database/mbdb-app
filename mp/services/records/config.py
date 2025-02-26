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

from mp.records.api import MpDraft, MpRecord
from mp.services.records.permissions import MpPermissionPolicy
from mp.services.records.results import MpRecordItem, MpRecordList
from mp.services.records.schema import MpSchema
from mp.services.records.search import MpDraftSearchOptions, MpSearchOptions


class MpServiceConfig(PermissionsPresetsConfigMixin, RDMRecordServiceConfig):
    """MpRecord service config."""

    result_item_cls = MpRecordItem

    result_list_cls = MpRecordList

    PERMISSIONS_PRESETS = ["mbdb"]

    url_prefix = "/records/mp/"

    base_permission_policy_cls = MpPermissionPolicy

    schema = MpSchema

    search = MpSearchOptions

    record_cls = MpRecord

    service_id = "mp"

    search_item_links_template = LinksTemplate
    draft_cls = MpDraft
    search_drafts = MpDraftSearchOptions

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

    model = "mp"

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mp/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/mp/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/records/mp/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/mp/{id}/edit", when=has_draft() & has_permission("update")
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/records/mp/{id}/files",
                    when=has_file_permission("list_files"),
                ),
                else_=RecordLink(
                    "{+api}/records/mp/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/records/mp/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/mp/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/records/mp/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/records/mp/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mp/{id}/requests"),
                else_=RecordLink("{+api}/records/mp/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mp/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/mp/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/mp/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/mp/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/records/mp/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/mp/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/mp/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/mp/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/mp/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/mp/{?args*}"),
            **pagination_links_html("{+ui}/records/mp/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/mp/{?args*}"),
            **pagination_links_html("{+ui}/user/records/mp/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/mp/{id}/versions{?args*}"),
        }
