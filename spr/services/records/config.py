from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent

from spr.records.api import SprDraft, SprRecord
from spr.services.records.permissions import SprPermissionPolicy
from spr.services.records.results import SprRecordItem, SprRecordList
from spr.services.records.schema import SprSchema
from spr.services.records.search import SprSearchOptions


class SprServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """SprRecord service config."""

    result_item_cls = SprRecordItem

    result_list_cls = SprRecordList

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
        DraftFilesComponent,
        FilesComponent,
        DataComponent,
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
            "requests": RecordLink("{+api}/records/spr/{id}/requests"),
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
