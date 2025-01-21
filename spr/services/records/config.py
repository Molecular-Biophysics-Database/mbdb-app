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

    search_item_links_template = LinksTemplate
    draft_cls = SprDraft
    search_drafts = SprSearchOptions

    @property
    def components(self):

        return process_service_configs(self) + [
            AuthorityComponent,
            DoiComponent,
            CommunityDefaultWorkflowComponent,
            # CommunityInclusionComponent,
            OwnersComponent,
            FilesComponent,
            DraftFilesComponent,
            CustomFieldsComponent,
            WorkflowComponent,
        ]

    model = "spr"

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/spr/{id}/requests/applicable"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/records/spr/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/spr/{id}/edit", when=has_draft() & has_permission("update")
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/records/spr/{id}/files",
                    when=has_file_permission("list_files"),
                ),
                else_=RecordLink(
                    "{+api}/records/spr/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/records/spr/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/spr/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/records/spr/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/records/spr/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/spr/{id}/requests"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/spr/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/spr/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/spr/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/spr/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/records/spr/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/records/spr/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/records/spr/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/spr/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/spr/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/records/spr/{?args*}"),
            **pagination_links_html("{+ui}/records/spr/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/records/spr/{?args*}"),
            **pagination_links_html("{+ui}/user/records/spr/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/records/spr/{id}/versions{?args*}"),
        }
