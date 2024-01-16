from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_requests.services.components import PublishDraftComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.results import RecordList
from spr.records.api import SprDraft, SprRecord
from spr.services.records.permissions import SprPermissionPolicy
from spr.services.records.schema import SprSchema
from spr.services.records.search import SprSearchOptions


class SprServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """SprRecord service config."""

    result_list_cls = RecordList

    PERMISSIONS_PRESETS = ["authenticated"]

    url_prefix = "/records/spr/"

    base_permission_policy_cls = SprPermissionPolicy

    schema = SprSchema

    search = SprSearchOptions

    record_cls = SprRecord

    service_id = "spr"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        PublishDraftComponent("publish_draft", "delete_record"),
        FilesComponent,
        DataComponent,
        DraftFilesComponent,
    ]

    model = "spr"
    draft_cls = SprDraft
    search_drafts = SprSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/records/spr/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/spr/{id}/files"),
                else_=RecordLink("{+api}/records/spr/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/spr/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/spr/{id}/latest"),
            "publish": RecordLink("{+api}/records/spr/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/spr/{id}"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/spr/{id}"),
                else_=RecordLink("{+api}/records/spr/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/spr/{id}"),
                else_=RecordLink("{+ui}/spr/{id}/edit"),
            ),
            "versions": RecordLink("{+api}/records/spr/{id}/versions"),
        }
