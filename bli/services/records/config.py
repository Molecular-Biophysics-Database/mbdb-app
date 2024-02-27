from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import ConditionalLink, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent

from bli.records.api import BliDraft, BliRecord
from bli.services.records.permissions import BliPermissionPolicy
from bli.services.records.results import BliRecordItem, BliRecordList
from bli.services.records.schema import BliSchema
from bli.services.records.search import BliSearchOptions


class BliServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig):
    """BliRecord service config."""

    result_item_cls = BliRecordItem

    result_list_cls = BliRecordList

    PERMISSIONS_PRESETS = ["authenticated"]

    url_prefix = "/records/bli/"

    base_permission_policy_cls = BliPermissionPolicy

    schema = BliSchema

    search = BliSearchOptions

    record_cls = BliRecord

    service_id = "bli"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        DataComponent,
        DraftFilesComponent,
        FilesComponent,
    ]

    model = "bli"
    draft_cls = BliDraft
    search_drafts = BliSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/records/bli/{id}/draft"),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/bli/{id}/files"),
                else_=RecordLink("{+api}/records/bli/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/records/bli/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/bli/{id}/latest"),
            "publish": RecordLink("{+api}/records/bli/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/records/bli/{id}"),
            "requests": RecordLink("{+api}/records/bli/{id}/requests"),
            "self": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/records/bli/{id}"),
                else_=RecordLink("{+api}/records/bli/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+ui}/bli/{id}"),
                else_=RecordLink("{+ui}/bli/{id}/edit"),
            ),
            "versions": RecordLink("{+api}/records/bli/{id}/versions"),
        }
